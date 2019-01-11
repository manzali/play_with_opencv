# import the necessary packages
import os
import numpy as np
import cv2

from os import listdir
from os.path import isfile, join

def detect(filename, dir_in, dir_out):
	# load the input image
	image = cv2.imread(join(dir_in, filename))

	# convert image to grayscale
	image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	# adjust the contrast of the gray image
	equalized = cv2.equalizeHist(image)
	#cv2.imwrite(join(dir_out, "equalized.png"), equalized)

	ret, thresh_img = cv2.threshold(equalized,70,255,cv2.THRESH_BINARY)
	#cv2.imwrite(join(dir_out, "thresh.png"), thresh_img)

	height, width = thresh_img.shape[:2]
	#blank_image = np.zeros((height,width,3), np.uint8)
	blank_image = cv2.cvtColor(equalized, cv2.COLOR_GRAY2RGB)
	im2, contours, hierarchy = cv2.findContours(thresh_img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	for cnt in contours:
		epsilon = 0.05*cv2.arcLength(cnt,True)
		approx = cv2.approxPolyDP(cnt,epsilon,True)
		if len(approx) == 4:
			# square
			x,y,w,h = cv2.boundingRect(approx)
			ratio = abs(w / h)
			#print (str(x) + " , " + str(y) + " , " + str(w) + " , " + str(h))
			#print (str(ratio))
			if ratio > 0.9 and ratio < 1.1:
				cv2.drawContours(blank_image, [approx], 0, (0,255,0), 3)
	
	cv2.imwrite(join(dir_out, filename), blank_image)


###################
#  START PROGRAM  #
###################


# cerate output dir if it doesn't exist
output_dir = "output"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# cerate contours dir if it doesn't exist
#cont_dir = "contours"
#if not os.path.exists(cont_dir):
#    os.makedirs(cont_dir)

	
#mypath = "frames"
#onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

#for f in onlyfiles:
#	detect(f, mypath, cont_dir)

detect("frame.png", ".", "output")
