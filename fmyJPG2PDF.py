from fpdf import FPDF
import os

pdf = FPDF()
# imagelist is the list with all image filenames

def getImageList():
	#imageList = str()
	#imageList = ""
	imageList = []
	for (dirpath, dirnames, filenames) in os.walk('.'):
		imageList.extend(filenames)
		break
	#imageList = str(fileList)
	return [ f for f in imageList if f.endswith('.jpg') ]

imageList = getImageList()

for image in imageList:
	pdf.add_page()
	pdf.image( image, 5, 5, 0, 0)
pdf.output("ImagePDFtest", "F")


# mageima:
