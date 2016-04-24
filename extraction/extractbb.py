import xml.etree.ElementTree as ET
import os
import sys
import glob

import dlib
from skimage import io

if len(sys.argv) != 2:
    print(
        "Give the path to the examples/faces directory as the argument to this "
        "program. For example, if you are in the python_examples folder then "
        "execute this program by running:\n"
        "    ./train.py ../examples/faces")
    exit()
f = sys.argv[1]

tree = ET.parse(f)
root = tree.getroot()
for child in root:
	if child.tag == 'images':
		for image in child:
			imageFile = os.path.join(f, image.attrib['file'])
			boxElem = image.find('box')
			left = boxElem.attrib['left']
			top = boxElem.attrib['top']
			width = boxElem.attrib['width']
			height = boxElem.attrib['height']

			# load img
			img = io.imread(f)
