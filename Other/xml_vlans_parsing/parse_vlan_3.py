import xml.dom.minidom

dom = xml.dom.minidom.parse("vlan8.xml")
dom.normalize()

#Choose the Excel page
WorksheetVLAN=dom.getElementsByTagName("Worksheet")[0]
#print("name="+WorksheetVLAN.getAttribute("ss:Name"))


#Choose a filled cell 
#for n in range (1):
filled_cell="s18"
for n in range (25):
	Cell=dom.getElementsByTagName("Cell")[n]
	#if a cell ss:StyleID="s18" then the cell is filled. if ss:StyleID="s17" then empty
	if Cell.getAttribute("ss:StyleID") == filled_cell:
	#print("StyleID="+Cell.getAttribute("ss:StyleID"))
	#option1 for Number
	
	#print(Cell.firstChild.firstChild.nodeValue)
	#option2 for Number
		Data=Cell.getElementsByTagName('Data')[0]
		#print(Data.firstChild.nodeValue)
		Font0=Cell.getElementsByTagName('Font')[0]
		Font1=Cell.getElementsByTagName('Font')[1]
		print(Data.firstChild.nodeValue +","+Font0.firstChild.nodeValue+Font1.firstChild.nodeValue)

print('========')

#Data = dom.getElementsByTagName('Data')
#print (Data[4].firstChild.nodeValue)
"""
for n in range (20):
	Cell=dom.getElementsByTagName("Cell")[n]
	print("StyleID="+Cell.getAttribute("ss:StyleID"))
	"""