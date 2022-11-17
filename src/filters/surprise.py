from PIL import Image
from datetime import datetime

def surprise(image_path):

    pixelToChange =  []

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

            pixelToChange.append({
                'x': i,
                'y': j,
                'RGBA': (100, 100, 100, 255)
            })

    # Apply the changes

    for newPixel in pixelToChange:
        rbgimg.putpixel(
            [newPixel['x'], newPixel['y']],
            newPixel['RGBA']
        )

    # Save output.
    dateString = datetime.now().strftime("%m%d%Y%H-%M-%S")
    rbgimg.save('./output_surprise' + dateString + '.png')