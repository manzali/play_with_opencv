# import the necessary packages
import os
import numpy as np
import cv2

from os import listdir
from os.path import isfile, join

def apply_gray(image):
	# convert image to grayscale
	return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def apply_blur(image):
	# blur the image with an aperture of X
	return cv2.medianBlur(image, 7)

def dynamic_threshold(image):
	# apply dynamic threshold
	return cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,3)

def binary_threshold(image):
	# apply bynary threshold
	return cv2.threshold(image,70,255,cv2.THRESH_BINARY)

def equalize(image):
	# adjust the contrast of the image
	return cv2.equalizeHist(image)

def subtract(img1, img2):
	# subtract img2 to img1
	return cv2.subtract(img1,img2)

def write_img(image, dir_out, name):
	# write image inside dir_out
	cv2.imwrite(join(dir_out, name), image)

def detect(image, dir_out):

	image = apply_gray(image)

	write_img(image, dir_out, "gray.png")

	image = apply_blur(image)

	thresh = dynamic_threshold(image)

	write_img(thresh, dir_out, "thresh.png")

	image = subtract(thresh, image)

	write_img(image, dir_out, "diff.png")

	# https://www.analyticsvidhya.com/blog/2019/03/opencv-functions-computer-vision-python/

	# instantiate sift object, calculate keypoints and their orientation
	#sift = cv2.xfeatures2d.SIFT_create()
	#keypoints,descriptors = sift.detectAndCompute(thresh,None)

	#instantiate surf object, calculate keypoints and their orientation
	#surf = cv2.xfeatures2d.SURF_create(800)
	#keypoints,descriptors = surf.detectAndCompute(thresh,None)

	# plot keypoints on the image
	#with_keypoints = cv2.drawKeypoints(gray, keypoints, outImage = None)
	#cv2.imwrite(join(dir_out, "sift.png"), with_keypoints)





	# adjust the contrast of the gray image
	#equalized = cv2.equalizeHist(image)
	#cv2.imwrite(join(dir_out, "equalized.png"), equalized)

	# apply threshold
	#ret, thresh_img = cv2.threshold(equalized,70,255,cv2.THRESH_BINARY)
	#cv2.imwrite(join(dir_out, "threshold.png"), thresh_img)

	# find cages
	#height, width = thresh_img.shape[:2]
	#blank_image = np.zeros((height,width,3), np.uint8)
	#contours, hierarchy = cv2.findContours(thresh_img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	#for cnt in contours:
	#	epsilon = 0.05*cv2.arcLength(cnt,True)
	#	approx = cv2.approxPolyDP(cnt,epsilon,True)
	#	if len(approx) == 4:
	#		# square
	#		x,y,w,h = cv2.boundingRect(approx)
	#		ratio = abs(w / h)
	#		#print (str(x) + " , " + str(y) + " , " + str(w) + " , " + str(h))
	#		#print (str(ratio))
	#		if ratio > 0.9 and ratio < 1.1:
	#			cv2.drawContours(blank_image, [approx], 0, (0,255,0), 3)
	#cv2.imwrite(join(dir_out, "squares.png"), blank_image)

	#
	#


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

# load the input image
image = cv2.imread(join(".", "frame.png"))
# call detect function
detect(image, "output")
