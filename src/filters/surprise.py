from PIL import Image
from datetime import datetime
import numpy as np

def median(img, img_arr):
    r = np.mean(img_arr[:, 0])
    g = np.mean(img_arr[:, 1])
    b = np.mean(img_arr[:, 2])
    for data in img_arr:
        img[data[3]][data[4]] = [r, g, b]


def buckets(img, img_arr, depth):
    if len(img_arr) == 0:
        return
    if depth == 0:
        median(img, img_arr)
        return
    r = np.max(img_arr[:, 0]) - np.min(img_arr[:, 0])
    g = np.max(img_arr[:, 1]) - np.min(img_arr[:, 1])
    b = np.max(img_arr[:, 2]) - np.min(img_arr[:, 2])
    space_with_highest_range = 0
    if g >= r and g >= b:
        space_with_highest_range = 1
    elif b >= r and b >= g:
        space_with_highest_range = 2
    elif r >= b and r >= g:
        space_with_highest_range = 0
    img_arr = img_arr[img_arr[:, space_with_highest_range].argsort()]
    median_index = int((len(img_arr) + 1) / 2)
    buckets(img, img_arr[0:median_index], depth - 1)
    buckets(img, img_arr[median_index:], depth - 1)


def surprise(image_path):
    img = Image.open(image_path)
    rbgimg = Image.new("RGBA", img.size)
    rbgimg.paste(img)
    rbgimg = np.array(rbgimg)
    rbgimg = rbgimg[:, :, :3]
    flattened_img_array = []
    for rindex, rows in enumerate(rbgimg):
        for cindex, color in enumerate(rows):
            flattened_img_array.append([color[0], color[1], color[2], rindex, cindex])
    flattened_img_array = np.array(flattened_img_array)
    buckets(rbgimg, flattened_img_array, 4)
    rbgimg = Image.fromarray(rbgimg)
    dateString = datetime.now().strftime("%m%d%Y%H-%M-%S")
    rbgimg.save("./outputs/output_surprise" + dateString + ".png")
