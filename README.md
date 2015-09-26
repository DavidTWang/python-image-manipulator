# python-image-manipulator
A simple image manipulator in Python

Includes 3 programs:
1. rotation.py - Rotate an image
2. blend.py - Blend two images together
3. text_overlay.py - Overlay an image on text

The programs can be found in the root directory of this archive
Two folders are provided for testing purposes:
    - Images - Contains several images that can be used for testing.
    - Font - For the text overlay program, two free fonts.

# How to run: Text overlay
python text_overlay.py [image path] [text] [font size]
For more information such as optional variables, please use
python text_overlay.py --help

# How to run: Blend
in the terminal, type:
	python blend.py images/source.jpg image/dest.jpg 0.5

images/source.jpg 		- give the first image
image/dest.jpg 			- give the second image
0.5						- the value can be between 0 and 1 in float

** the size of source image and dest image should be SAME.
