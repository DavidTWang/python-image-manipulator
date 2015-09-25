from PIL import Image
import sys


def open_image(path):
	image = None
	try:
		image = Image.open(path)
	except Exception as e:
		print("Image not found")
		print(e)
		return
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
	
 	# check the size of images if it not same, exit
	if sourceImg.size != destImg.size:
		print("The source image and destination image size should be same")
		exit(1)

	# check alpha value
	if alpha < 0 or alpha > 1:
		print("Alpha value should be >=0 or <=1")
		exit(1)

	####################################################################
	# # blend function that takes two images and alpha
	# The size of two images should be same to implement blend function.
	# The last parameter 'alpha' is the blending ratio 
	# which determines the influence of each input image in the output
	# if alpha is 0.0, a copy of the first image is returned.
	# if alpha is 1.0, a copy of the second image is returned. 

	fImage = Image.blend(sourceImg, destImg, alpha)
	
	####################################################################
	
	# show and save the image
	fImage.show()
	fImage.save("blend_result.jpg")
	fImage.close()


if __name__ == '__main__':
	main(sys.argv[1:])