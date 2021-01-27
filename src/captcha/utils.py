import os
import numpy as np
from cairosvg import svg2png
from PIL import Image

IMAGE_SPLIT_RANGES = [
    [15, 45],
    [45, 75],
    [70, 100],
    [100, 130]
]


def svg_to_vec(svg_img):
    svg2png(bytestring=svg_img, write_to='captcha.png')
    img = Image.open('captcha.png').convert('RGBA')
    arr = np.array(img)
    os.remove('captcha.png')

    single_channel_bw_arr = np.array(np.sum(arr, axis=2) > 0, dtype=np.int)
    return single_channel_bw_arr


def split_image(img_vec):
    splits = []
    for i in range(len(IMAGE_SPLIT_RANGES)):
        split_i = img_vec[:, IMAGE_SPLIT_RANGES[i][0]:IMAGE_SPLIT_RANGES[i][1]]
        split_i = split_i.reshape((-1,))
        splits.append(split_i)
    return splits
