#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.dom.minidom

dom = xml.dom.minidom.parse("vlan88.xml")
dom.normalize()

#Value for a filled cell ss:StyleID="s18"
filled_cell="s18"
j = 0
for n in range (0,95):
	Cell=dom.getElementsByTagName("Cell")[n]
	j=j+1
	#if a cell ss:StyleID="s18" then the cell is filled, if ss:StyleID="s17" then empty
	if Cell.getAttribute("ss:StyleID") == filled_cell:
		#Get a cell number
		Data=Cell.getElementsByTagName('Data')[0]
		#print("ok")
		#Get a value for Comment's Author
		Font0=Cell.getElementsByTagName('Font')[0]
		#Get a value for Comment
		Font1=Cell.getElementsByTagName('Font')[1]
		#Write a cell number + Comment's Author + Comment
		print(Data.firstChild.nodeValue +","+Font0.firstChild.nodeValue+Font1.firstChild.nodeValue+",Active")

print('========')

#Data = dom.getElementsByTagName('Data')
#print (Data[4].firstChild.nodeValue)
"""
for n in range (20):
	Cell=dom.getElementsByTagName("Cell")[n]
	print("StyleID="+Cell.getAttribute("ss:StyleID"))
	"""