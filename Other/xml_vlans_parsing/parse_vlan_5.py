#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.dom.minidom

dom = xml.dom.minidom.parse("vlan8.xml")
dom.normalize()

#Value for a filled cell ss:StyleID="s18"
yellow_cell="s18"
Font01=""
#n - VLAN number
for n in range (4093,4096):
	Cell=dom.getElementsByTagName("Cell")[n]
	#if a cell ss:StyleID="s18" then the cell is yellow, if ss:StyleID="s17" then green
	if Cell.getAttribute("ss:StyleID") == yellow_cell:
		#Get a cell number
		Data=Cell.getElementsByTagName('Data')[0]
		try:
			#Get a value for Comment's Author
			Font0=Cell.getElementsByTagName('Font')[0]
			#Get a value for Comment
			Font1=Cell.getElementsByTagName('Font')[1]
			Font01=Font0.firstChild.nodeValue+Font1.firstChild.nodeValue
			#print(type(Font01))
			#unicode_Font01 = Font01.decode("utf-8")
			#print(len(unicode_Font01))
			#Write a cell number + Comment's Author + Comment
			print(Data.firstChild.nodeValue +","+Font01+",Active,RTK Laboratory Reutov")
		except:
			print(Data.firstChild.nodeValue+ ",No name,Active,RTK Laboratory Reutov")
print('========')

#Data = dom.getElementsByTagName('Data')
#print (Data[4].firstChild.nodeValue)
"""
for n in range (20):
	Cell=dom.getElementsByTagName("Cell")[n]
	print("StyleID="+Cell.getAttribute("ss:StyleID"))
	"""