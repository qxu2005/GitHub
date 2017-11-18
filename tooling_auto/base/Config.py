from xml.dom import minidom
import os
import sys
from Context import Context
class Config:
	'''Represents base Config.'''
	
	xmldoc = ""
	root = ""
	
	@staticmethod
	def init():
		"""
		@summary:  init xml 
		"""
		Config.xmldoc = minidom.parse(Context.GetContext('configpath'))

		
	@staticmethod
	def getValue(tag,attribute):	
		"""
		@summary: get attribute value from tag
		@param tag: tag name
		@param attribute: attribute name
		
		"""
		try:
			itemlist = Config.xmldoc.getElementsByTagName(tag) 
			return itemlist[0].attributes[attribute].value.encode('utf-8')
		except:
			return None
		
	
		
		