import cv2
import numpy as np
import os
from PIL import Image
recognizer = cv2.face.LBPHFaceRecognizer_create()
path='dataSet'
def getImagesWithID(path):
	imagePaths=[os.path.join(path,f)for f in os.listdir(path)]
	print(imagePaths)
getImagesWithID(path)
