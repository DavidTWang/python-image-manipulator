from PIL import Image, ImageDraw, ImageFont
import argparse


# Opens an image at the given path
def open_image(path):
    image = None
    try:
        image = Image.open(path)
    except Exception as e:
        print("Image not found")
        print(e)
        return
    return image


def main(args):
    # Parse optional font
    if(args.font is None):
        args.font = "fonts/impact.ttf"

    # Open the image
    image = open_image(args.image).convert('RGBA')
    # Store the width and height of the image
    width, height = image.size
    # Create the font object
    fnt = ImageFont.truetype(args.font, args.fontsize)
    # Create image mask object
    mask = Image.new('1', (width, height), '#000000')
    draw = ImageDraw.Draw(mask)
    # Get size of text
    txtw, txth = draw.textsize(args.text, fnt)

    # Parse optional positions
    if(args.xpos is None):
        args.xpos = (width-txtw) / 2
    if(args.ypos is None):
        args.ypos = (height-txth) / 2

    # Draw the text on the image mask
    draw.text((args.xpos, args.ypos), args.text, font=fnt, fill='#ffffff')
    # Select all areas on the mask that are white (the text)
    mask = mask.point(lambda i: i == 0)
    # Paste the transparent mask over the image
    image.paste((0, 0, 0, 0), (0, 0), mask)

    # Save image
    image.save("result.png")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("image", help="Image to use for overlay")
    parser.add_argument("text", help="Text to display")
    parser.add_argument("fontsize", type=int, help="Font size")
    parser.add_argument("-f", "--font", help="Font to use. Default=\"Impact.ttf\"")
    parser.add_argument("-x", "--xpos", type=int, help="X position to place text. Defaults to center of image.")
    parser.add_argument("-y", "--ypos", type=int, help="Y position to place text. Defaults to center of image.")
    args = parser.parse_args()

    main(args)
