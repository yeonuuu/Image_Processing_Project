from PIL import Image
from datetime import datetime

def angry(image_path):

    # Open image even grayscale and convert it to RGBA

    img = Image.open(image_path)
    rbgimg = Image.new("RGBA", img.size)
    rbgimg.paste(img)

    # Do your algorithm


    # This loop get all RGBA value for all pixel.
    for i in range(rbgimg.size[0]):
        for j in range(rbgimg.size[1]):
            r, g, b, a = rbgimg.getpixel((i, j))
            print(r, g , b, a)


    # Save output.
    dateString = datetime.now().strftime("%m%d%Y%H-%M-%S")
    rbgimg.save('./output_angry' + dateString + '.png')