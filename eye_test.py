import PIL.Image

__author__ = 'sufianlatif'

import webbrowser
import pyscreenshot
import time
from PIL import Image


def getGridSize(image):
    assert isinstance(image, PIL.Image.Image)
    width = image.size[0]
    tmp = 10
    size = 0
    i = 0
    while i < width:
        while i < width and image.getpixel((i, tmp)) != (255, 255, 255):
            i += 1
        size += 1
        while i < width and image.getpixel((i, tmp)) == (255, 255, 255):
            i += 1
    return size


def getCellCenters(image):
    n = getGridSize(image)
    gap = 4
    cellSize = int((image.size[0] - (n - 1) * gap) / n)
    stops = [(2 * i + 1) * cellSize / 2 + i * gap for i in range(n)]
    print stops
    points = [[(x, y) for x in stops] for y in stops]
    return points

url = 'https://www.igame.com/eye-test/?fbs=32'

# webbrowser.open_new(url)
# time.sleep(10)

# im=pyscreenshot.grab(bbox = (647, 286, 983, 622))
im = Image.open('7.png')
getCellCenters(im)
