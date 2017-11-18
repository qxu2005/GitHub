#include "applicationui.hpp"
#include <bb/cascades/Application>
#include <bb/cascades/QmlDocument>
#include <bb/cascades/AbstractPane>
#include <iostream.h>

using namespace bb::cascades;

ApplicationUI::ApplicationUI(bb::cascades::Application *app) :
		QObject(app) {
	
	
	//QString
    	QString qString0 = "Hello";
    	const QString * qString1 = new QString("This is a string");
    	QString* qString2 = &qString0;

    	//QByteArray
    	QByteArray qbytearry0("and");
    	qbytearry0.prepend("rock "); // x == "rock and"
    	qbytearry0.append(" roll"); // x == "rock and roll"
    	qbytearry0.replace(5, 3, "&");

    	QByteArray* qByteAarry1 = new QByteArray();
    	qByteAarry1->append(" QByteArray");
    	QByteArray* qByteAarry2 = &qbytearry0;

    	//QList
    	QList<QString> qlist0;
    	qlist0.append("one");
    	qlist0.append("two");
    	qlist0.append("three");

    	QList<QString>* qList1 = new QList<QString>;
    	qList1->append("1");
    	QList<QString>* qList2 = &qlist0;
    	qList1->append("q list");


    	//QStringList
    	QStringList qstringlist0;
    	qstringlist0 << "Bill Murray" << "John Doe" << "Bill Clinton";
    	// result: ["Bill Murray", "Bill Clinton"]
    	QStringList* qStringList1 = new QStringList(qstringlist0.filter("Bill"));
    	QStringList* qStringList2 = &qstringlist0;


    	//QQueue
    	QQueue<int> qqueue0;
    	qqueue0.enqueue(1);
    	qqueue0.enqueue(2);
    	qqueue0.enqueue(3);
    	QQueue<int>* qQueue1 = new QQueue<int>;
    	qQueue1->enqueue(10);
    	QQueue<int>* qQueue2 = &qqueue0;

    	//QVector
    	QVector<QString> qvector0(0);
    	qvector0.append("one");
    	qvector0.append("two");
    	qvector0.append("three");

    	QVector<QString> *qVector1 = new QVector<QString>(10, "default");
    	qVector1->insert(0, "qvector");
    	QVector<QString>* qVector2 = &qvector0;

    	//QStack
    	QStack<int> qstack0;
    	qstack0.push(1);
    	qstack0.push(2);
    	qstack0.push(3);

    	QStack<QString>* qstack1 = new QStack<QString>();
    	qstack1->push("q stack");
    	QStack<int>* qstack2 = &qstack0;

    	//QLinkedList
    	QLinkedList<QString> qlinkedlist0;
    	qlinkedlist0.append("one");
    	qlinkedlist0.append("two");
    	qlinkedlist0.append("three");
    	QLinkedList<QString>* qlinkedlist1 = new QLinkedList<QString>;
    	QLinkedList<QString>* qlinkedlist2 = &qlinkedlist0;

    	//QMap
    	QMap<QString, int> qmap0;
    	qmap0["one"] = 1;
    	qmap0["three"] = 3;
    	QMap<QString, int>* qmap1 = new QMap<QString, int>;
    	qmap1->operator []("qstring") = 0;
    	QMap<QString, int> *qmap2 = &qmap0;
    	qmap1->operator []("seven") = 7;
    	qmap1->insert("twelve", 12);

    
    	//QMultiMap
    	QMultiMap<QString, int> qmutimap0, *qmutimap1, *qmutimap2;
    	qmutimap0.insert("plenty", 100);
    	qmutimap0.insert("plenty", 2000);
    	qmutimap1 = new QMultiMap<QString, int>;
    	qmutimap1->insert("qmultipap", 0);
    	qmutimap2 = &qmutimap0;
    	qmutimap2->operator +(qmutimap0);

    	//QHash
    	QHash<QString, int> qhash0;
    	qhash0["one"] = 1;
    	qhash0["three"] = 3;
    	qhash0["seven"] = 7;
    	qhash0.insert("twelve", 12);
    	int num1 = qhash0["thirteen"];
    	int num2 = qhash0.value("thirteen");
    	QHash<QString, int> *qhash1 = new QHash<QString, int>;
    	qhash1->operator []("qhash") = 0;
    	QHash<QString, int> *qhash2 = &qhash0;


    	//QMultiHash - hash1.size() == 2; hash2.size() == 1; hash3.size() == 3
    	QMultiHash<QString, int> qmultihash0, *qmultihash1, *qmultihash2;
    	qmultihash0.insert("plenty", 100);
    	qmultihash0.insert("plenty", 2000);
    	qmultihash0.insert("plenty", 5000);
    	qmultihash1 = new QMultiHash<QString, int>(qmultihash0);
    	qmultihash2 = &qmultihash0;

    	//QDate
    	QDate qdate0(1995, 5, 17); // May 17, 1995
    	QDate* qdate1 = new QDate(1995, 5, 20); // May 20, 1995
    	qdate0.daysTo(*qdate1); // returns 3
    	qdate1->daysTo(qdate0); // returns -3
    	QDate *qdate2 = &qdate0;



    	//QTime
    	QTime qtime0(14, 0, 0); // n == 14:00:00
    	qtime0.addSecs(70); // t == 14:01:10
    	qtime0.addSecs(-70); // t == 13:58:50
    	qtime0.addSecs(10 * 60 * 60 + 5); // t == 00:00:05
    	qtime0.addSecs(-15 * 60 * 60); // t == 23:00:00
    	QTime* qtime1 = new QTime(14, 0, 0);
    	QTime* qtime2 = &qtime0;

    	//QDateTime // dateTime is 1 January 1998 00:01:02
    	QDateTime dateTime0 = QDateTime::fromString("M1d1y9800:01:02",
    			"'M'M'd'd'y'yyhh:mm:ss");
    	QDateTime* dateTime1 = new QDateTime(QDateTime::currentDateTime());
    	QDateTime* dateTime2 = &dateTime0;

    	//QUrl
    	QUrl url0 = QUrl::fromEncoded("http://qt.nokia.com/List%20of%20holidays.xml");
    	QUrl* url1 = new QUrl();
    	url1->setHost("www.google.com");
    	QUrl* url2 = &url0;

    	//QSet and QSetIterator
    	QSet<QString> qset0;
    	qset0.insert("one");
    	QSet<QString> *qset1 = new QSet<QString>;
    	qset1->insert("three");
    	qset1->insert("seven");
    	QSet<QString> *qset2 = &qset0;

    	QString s = "";
    	QSetIterator<QString> qsetiterator0(qset0);
    	while (qsetiterator0.hasNext())
    		s = s + qsetiterator0.next();

    	//QChar
    	QChar myChar0('7');
    	QChar* myChar1 = new QChar('u');
    	int i1 = myChar0.digitValue();
    	int i2 = myChar1->digitValue();
    	QChar* myChar2 = &myChar0;

    	qDebug() << "*********";

    	delete myChar1;
    	delete qset1;
    	delete url1;
    	delete dateTime1;
    	delete qtime1;
    	delete qdate1;
    	delete qmultihash1;
    	delete qhash1;
    	delete qmutimap1;
    	delete qmap1;
    	delete qlinkedlist1;
    	delete qstack1;
    	delete qVector1;
    	delete qQueue1;
    	delete qStringList1;
    	delete qList1;
    	delete qByteAarry1;
    	delete qString1;
	
	
	
	QmlDocument *qml = QmlDocument::create("asset:///main.qml").parent(this);
	AbstractPane *root = qml->createRootObject<AbstractPane>();
	app->setScene(root);
}


void ApplicationUI::onSystemLanguageChanged()
{

}
