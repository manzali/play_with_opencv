# import the necessary packages
import os
import numpy as np
import cv2

directory = "output"
if not os.path.exists(directory):
    os.makedirs(directory)

# construct a edge detection filter
edge_kernel = np.array((
	[-1, -1, -1],
	[-1, 8, -1],
	[-1, -1, -1]))

# load the input image
image = cv2.imread("image.jpg")

# convert image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite("output/gray_image.jpg", gray_image)

# apply edge detection filter to the gray image
edges = cv2.filter2D(gray_image, -1, edge_kernel)
cv2.imwrite("output/edges.jpg", edges)

# adjust the contrast of the gray image
equalized = cv2.equalizeHist(gray_image)
cv2.imwrite("output/equalized.jpg", equalized)

denoised_equalized = cv2.fastNlMeansDenoising(equalized, None, 9, 13)
cv2.imwrite("output/denoised_equalized.jpg", denoised_equalized)

# apply edge detection filter to the gray image
denoised_edges = cv2.filter2D(denoised_equalized, -1, edge_kernel)
cv2.imwrite("output/denoised_edges.jpg", denoised_edges)