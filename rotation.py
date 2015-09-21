from PIL import Image
import PIL.ImageOps
import sys

#Grab an image and rotate it by what the user specified
def rotate():
	#Asks for user input about what degree they would want to rotate the image by
	rdegrees = input('How much would you like to rotate the image by?: ')
	rdeg = int(rdegrees)
	#Grab the image
	im = Image.open("ak.jpg")
	#Rotate the image depending on what number the user inputted and increase the size of the image to compensate weird numbers
	rotatedim = im.rotate(rdeg, expand=1)
	rotatedim.save("rotatedak.jpg")
#Main
rotate()