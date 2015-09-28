from PIL import Image
import sys


def open_image(path):
	image = None
	try:
		image = Image.open(path)
	except Exception as e:
		print("Image not found")
		exit(1)
	return image


def main(argv):
	if(len(argv) != 3):
		print("Invalid number of arguments. Requires two images and alpha. path/filename1 path/filename2 alpha.")
		sys.exit(1)
	else:
		filename1 = argv[0]
		filename2 = argv[1]
		alpha = float(argv[2])


	# open images
	sourceImg = open_image(filename1)
	destImg = open_image(filename2)
	
	# check alpha value
	if alpha < 0 or alpha > 1:
		print("Alpha value should be >=0 or <=1")
		exit(1)

	# create a result image
	result = Image.new("RGB", sourceImg.size)

 	# check the size of images if it not same, exit
	if sourceImg.size != destImg.size:
		print("The source image and destination image size should be same")
		exit(1)

	##############################################################################
	# blending algorithm
	#
	# loop through all the pixels in source image and dest image.
	# when it loops through, store source image pixel and dest image pixel in a  
	# certain position (i,j).
	# Calculate the result pixel value for the location by:
	#		result = image1 * (1.0 - alpha) + image2 * alpha
	# if alpha is equal to 1: only dest image shows up
	# if alpha is equal to 0: only source image shows up.
	#
	##############################################################################

	# srcPixels = list(sourceImg.getdata())
	# destPixels = list(destImg.getdata())
	# finalPixels = list(result.getdata())

	# count = 0
	# for pixels in srcPixels:
	# 	srcR = pixels[0]
	# 	srcG = pixels[1]
	# 	srcB = pixels[2]
	# 	dstR = destPixels[count][0]
	# 	dstG = destPixels[count][1]
	# 	dstB = destPixels[count][2]

	# 	finalR = int(srcR * (1-alpha)) + int(dstR * alpha)
	# 	finalG = int(srcG * (1-alpha)) + int(dstG * alpha)
	# 	finalB = int(srcB * (1-alpha)) + int(dstB * alpha)

	# 	finalPixels[count] = (finalR, finalG, finalB)

	# 	count = count + 1

	# result.putdata(finalPixels)
	
	# result.save("blend_result.jpg")
	# result.show()



	for i in range(0, result.width):
		for j in range(0, result.height):
			s = sourceImg.getpixel((i,j))
			d = destImg.getpixel((i,j))
			
			r = int(s[0] * (1-alpha)) + int(d[0] * alpha)
			g = int(s[1] * (1-alpha)) + int(d[1] * alpha)
			b = int(s[2] * (1-alpha)) + int(d[2] * alpha)

			result.putpixel((i,j), (r,g,b))

	result.save("blend_result.jpg")
	result.show()


	# # check alpha value
	# if alpha < 0 or alpha > 1:
	# 	print("Alpha value should be >=0 or <=1")
	# 	exit(1)

	# ####################################################################
	# # # blend function that takes two images and alpha
	# # The size of two images should be same to implement blend function.
	# # The last parameter 'alpha' is the blending ratio 
	# # which determines the influence of each input image in the output
	# # if alpha is 0.0, a copy of the first image is returned.
	# # if alpha is 1.0, a copy of the second image is returned. 

	# fImage = Image.blend(sourceImg, destImg, alpha)
	
	# ####################################################################
	
	# # show and save the image
	# fImage.show()
	# fImage.save("blend_result.jpg")
	# fImage.close()


if __name__ == '__main__':
	main(sys.argv[1:])









