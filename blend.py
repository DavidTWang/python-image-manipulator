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
	if(len(argv) != 2):
		print("Invalid number of arguments. Requires two images path/filename1 path/filename2.")
		sys.exit(2)
	else:
		filename1 = argv[0]
		filename2 = argv[1]

	# open images
	image1 = open_image(filename1)
	image2 = open_image(filename2)

	fImage = Image.blend(image1, image2, 0.5)
	fImage.show()


if __name__ == '__main__':
	main(sys.argv[1:])