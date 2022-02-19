from tkinter import W, image_names
import cv2
import argparse
import glob
import csv
import os

# 
# Type this into Terminal if you open this with VScode
# python blur_detection.py -i images -t 100 //100 is for threshold
# P.S. if you run to in error check the directory if it correct
# 

# Argument reciver
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--images', required=True,)
ap.add_argument('-t', '--threshold', type=float)
args = vars(ap.parse_args())

# Path
# Warning You need to change paht and images path to your directory
path = "/Users/Allumile/Desktop/facial_expressions/images/"
images = [cv2.imread(file) for file in glob.glob("/Users/Allumile/Desktop/facial_expressions/images/*.jpg".format(args['images']))]

# Counting
index_arr = 0

# Creating csv and header
header = ['name', 'res', 'count']
f = open('not_blur.csv', 'w')
w = csv.writer(f)
w.writerow(header)

# Array of picture name
arr = os.listdir('/Users/Allumile/Desktop/facial_expressions/images')

# Loop through images and check if it blur or not
for image in images:
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	fm = cv2.Laplacian(gray, cv2.CV_64F).var()
	text = "Not Blurry"

	if fm < args["threshold"]:
		text = "Blurry"

	if text == "Not Blurry":
		w.writerow([arr[index_arr], text])

	
	cv2.putText(image, "{}: {:.2f}".format(text, fm), (10, 30),
	cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
	cv2.imshow("Image", image)
	#cv2.waitKey(0)	# Comment this if you don't want image to display

	index_arr += 1

f.close()
