from PIL import Image
from datetime import datetime
from filters.change_image import apply_filter


def fear(image_path):

    pixelToChange = []

    # Open image even grayscale and convert it to RGBA

    img = Image.open(image_path)
    rbgimg = Image.new("RGBA", img.size)
    rbgimg.paste(img)

    # Do your algorithm

    # This loop get all RGBA value for all pixel.
    for i in range(rbgimg.size[0]):
        for j in range(rbgimg.size[1]):
            r, g, b, a = rbgimg.getpixel((i, j))

            # Example of adding to the list a new pixel that has to change
            # with its value.
            newA = (i + j % 255) + 1
            pixelToChange.append({"x": i, "y": j, "RGBA": (r, g, b, newA)})

    # Apply the changes

    rbgimg = apply_filter(pixelToChange, rbgimg)

    # Save output.
    dateString = datetime.now().strftime("%m%d%Y%H-%M-%S")
    rbgimg.save("./outputs/output_fear" + dateString + ".png")
