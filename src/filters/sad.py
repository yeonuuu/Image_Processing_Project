from PIL import Image
from datetime import datetime
from filters.change_image import apply_filter


def sad(image_path):

    pixelToChange = []

    # Open image even grayscale and convert it to RGBA

    img = Image.open(image_path)
    rbgimg = Image.new("RGBA", img.size)
    rbgimg.paste(img)
    treshold = 180
    # Do your algorithm

    # This loop get all RGBA value for all pixel.
    for i in range(rbgimg.size[0]):
        for j in range(rbgimg.size[1]):
            r, g, b, a = rbgimg.getpixel((i, j))
            grayscale = int((r + g + b) / 3)
            rbgimg.putpixel((i, j), (grayscale, grayscale, grayscale))
    for i in range(rbgimg.size[0]):
        for j in range(rbgimg.size[1]):
            r, g, b, a = rbgimg.getpixel((i, j))
            if r > treshold:
                rbgimg.putpixel((i, j), (255, 255, 255))
            else:
                rbgimg.putpixel((i, j), (0, 0, 0))
            # Example of adding to the list a new pixel that has to change
            # with its value.

    # Save output.
    dateString = datetime.now().strftime("%m%d%Y%H-%M-%S")
    rbgimg.save("./outputs/output_sad" + dateString + ".png")
