import xml.etree.ElementTree as etree
from xml.dom.minidom  import Document
import sys, getopt
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import socket

def GenerateXMLResult(dict,outputfile):
	total_tests = 0
	total_failures = 0
				
	doc = Document()
	root = doc.createElement('testsuites')
	root.setAttribute('name', 'automation')
	doc.appendChild(root)
		
		
	for suitename in sorted(dict.iterkeys()):
		current_suite_failures = 0
		testsuite = doc.createElement('testsuite')
		testsuite.setAttribute('name', suitename)
		root.appendChild(testsuite)
			
		testcases = dict[suitename]
		testsuite.setAttribute('tests', str(len(testcases)))
		total_tests = total_tests + len(testcases)
			
		for testcasename in sorted(testcases.iterkeys()):
			testcase = doc.createElement('testcase')
			testcase.setAttribute('name', testcasename)
			testcase.setAttribute('time', str(0))
			testsuite.appendChild(testcase)
			result = testcases[testcasename]
			if result != 'pass':
				current_suite_failures += 1
				total_failures += 1
				failure = doc.createElement('failure')
				testcase.appendChild(failure)
				failure.setAttribute('message', result)
				failure.setAttribute('type', 'verification failed')
					
		
		
		
		testsuite.setAttribute('errors', str(0))
		testsuite.setAttribute('failures', str(current_suite_failures))
			
	root.setAttribute('errros', str(0))
	root.setAttribute('failures', str(total_failures))
	root.setAttribute('tests', str(total_tests))
	doc.writexml(open(outputfile, 'w'),indent="",addindent=" ",newl='\n')
 
	doc.unlink()


def parseGunitXml(filename):

	tree = etree.parse(filename)
	
	root = tree.getroot()
	
	result = {}
	list_testcase = tree.findall('testcase')

	for child in list_testcase:
		tokens =  child.attrib['name'].split('.')
		key = tokens[0]
		if  not result.has_key(key):
			result[key] = 'pass'
	
		if len(list(child.iter("failure"))) >0:
			for visit_element in child.iter("failure"):
				if result[key] == 'pass':
					result[key] = visit_element.attrib['message']
				else:
					result[key] = result[key] + visit_element.attrib['message'] +"::"
					
		if len(list(child.iter("error"))) >0:
			for visit_element in child.iter("error"):
				if result[key] == 'pass':
					result[key] = visit_element.attrib['message']
				else:
					result[key] = result[key] + visit_element.attrib['message'] +"::"
			
	testsuites = {}

	testsuites[root.attrib['name']] = result
	
	return testsuites

	
def sendEmail(allresult,to_list,timestamp):
	info ="Host:" + socket.gethostname()  +  "    TimeStamp:" + timestamp + "\n" + "Os:" + sys.platform
	
	for key in sorted(allresult.iterkeys()):
            info = info + 'TestSuite: '+ key + '\n\n'
            testresult = allresult[key]
            
            for testkey in sorted(testresult.iterkeys()):
                if testresult[testkey] == 'pass':
                    info = info + testkey + ": Pass\n\n" 
                else:
                    info = info + testkey + ": Failed\n" + testresult[testkey] + "\n\n"

	msg = MIMEMultipart('alternative')
	msg['Subject'] = 'Squish  Sanity Automation'
	msg['From'] = 'squishTest'
	msg['To'] = ",".join(to_list)
	part = MIMEText(info, 'plain')
	msg.attach(part)
	s = smtplib.SMTP('sapcrm-smtp.rim.net')
	s.sendmail('squishTest',to_list, msg.as_string())
	s.quit()
	
def main(argv):
	email= r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}'
	to_list=[]
	inputfile = ''
	outputfile = ''
	timestamp = ''
	input_flag = False
	output_flag = False
	timestamp_flag = False
	try:
		opts, args = getopt.getopt(argv,"hi:o:e:t:")
	except getopt.GetoptError:
		print 'parse.py -i <inputfile> -o <outputfile> -e<email list> -t<time stamp>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'parse.py -i <inputfile> -o <outputfile> -e<email list> -t<time stamp>'
			sys.exit()
		elif opt == "-i":
			inputfile = arg
			input_flag = True
		elif opt  == "-o":
			outputfile = arg
			output_flag = True
		elif opt == "-t":
			timestamp = arg
			timestamp_flag = True
		elif opt == "-e":
			id_list = arg.split(',')
			p = re.compile(email)
        
			for item in id_list:
				m = p.search(item)
				if m:
					to_list.append(item)
				else:
					to_list.append(item+'@blackberry.com') 
			
	if  not input_flag or not output_flag or not timestamp_flag :
		print 'parse.py -i <inputfile> -o <outputfile> -e<email list> -t<time stamp>'
		sys.exit()
	
	result_list = parseGunitXml(inputfile)
	GenerateXMLResult(result_list,outputfile)
	if len(to_list) >0 :
		sendEmail(result_list,to_list,timestamp)
	
if __name__ == "__main__":
   main(sys.argv[1:])
