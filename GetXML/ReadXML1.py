#-*- coding: -8 -*-
import xml.etree.ElementTree as ET



tree = ET.ElementTree(file='Login.xml')

for child in tree.iter():

    print child.tag, child.attrib