import cv2
import sys
import glob
import argparse
import csv
import os

# 
# Type this into Terminal if you open this with VScode or run in cmd
# python blur_detection.py -i
# P.S. if you run to in error check the directory if it correct
# 

# Path
path = "/Users/Allumile/Desktop/facial_expressions/images/"
cascPath = "haarcascade_frontalface_default.xml" # Don't touch this

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# Read the image
# Warning You need to change paht and images path to your directory #
images = [cv2.imread(file) for file in glob.glob("/Users/Allumile/Desktop/facial_expressions/images/*.jpg".format('images'))]
arr = os.listdir('/Users/Allumile/Desktop/facial_expressions/images')

# Counting
usable = 0
index_arr = 0

# Creating csv and header
f = open('usable_face.csv', 'w')
wr = csv.writer(f)
header = ['name', 'width', 'height']
wr.writerow(header)

# Array of picture name
arr = os.listdir('/Users/Allumile/Desktop/facial_expressions/images')

# Loop all the picture
for image in images:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=1,
        minSize=(250, 250),
        flags = cv2.CASCADE_SCALE_IMAGE
    )

    # Only allow one face to pass
    if len(faces) == 1:
        usable += 1
    
        #print("Found {0} faces!".format(len(faces)))
        
        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
            wr.writerow([arr[index_arr], w, h])

        cv2.imshow("Faces found", image)
        cv2.waitKey(0) # Comment this if you don't want image to display
    
    index_arr += 1

#print(usable)
wr.writerow([usable])