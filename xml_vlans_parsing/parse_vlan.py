#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET

#tree = ET.parse('vlan5.xml')

xml = ET.fromstring('vlan5.xml')

print(xml.find('./Worksheet').attrib['ss:Name'])
#root = tree.getroot()
#print (root.tag)
#print (root.attrib)

#print(root[5][0][0].text)

#for child in root:
#	print (child.attrib)

