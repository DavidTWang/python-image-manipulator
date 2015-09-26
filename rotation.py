from PIL import Image
import PIL.ImageOps
import sys

#Grab an image and rotate it by what the user specified
def rotate():
	#Asks for user input about what degree they would want to rotate the image by
	imageChosen = raw_input("Image to rotate: ")
	rdegrees = input('Degrees of rotation: ')
	rdeg = int(rdegrees)
	#Grab the image
	im = Image.open("images/"+imageChosen)
	#The .rotate has 3 parameters: angle, resample, and expand
	#In this case, we use angle and expand
	#Angle is the degrees the user wants the image rotated and expand increases the size of 
	#the image so that it can show the whole image when rotating with wierd numbers
	rotatedim = im.rotate(rdeg, expand=1)
	rotatedim.save("rotated" + imageChosen + ".jpg")
#Main
rotate()