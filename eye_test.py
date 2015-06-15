__author__ = 'sufianlatif'

import webbrowser
import pyscreenshot
import time
from PIL import Image
import random
from PyWinMouse import Mouse


def getGridSize(image):
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
    points = [[(x, y) for x in stops] for y in stops]
    return points


def findTheChosenOne(image):
    gridSize = getGridSize(image)
    centers = getCellCenters(image)
    n = gridSize * gridSize
    for i in range(n):
        x, y = i / gridSize, i % gridSize
        color = image.getpixel(centers[x][y])

        tmp1 = random.randint(0, n - 1)
        while tmp1 == i:
            tmp1 = random.randint(0, n - 1)
        x1, y1 = tmp1 / gridSize, tmp1 % gridSize
        color1 = image.getpixel(centers[x1][y1])

        tmp2 = random.randint(0, n - 1)
        while tmp2 == i or tmp2 == tmp1:
            tmp2 = random.randint(0, n - 1)
        x2, y2 = tmp2 / gridSize, tmp2 % gridSize
        color2 = image.getpixel(centers[x2][y2])

        if color != color1 and color != color2:
            return centers[x][y]
    return None


url = 'https://www.igame.com/eye-test/?fbs=32'

webbrowser.open_new(url)
time.sleep(10)

startX = 647
startY = 286
width = 336
height = 336

while True:
    im = pyscreenshot.grab(bbox = (startX, startY, startX + width, startY + height))
    # im = Image.open('7.png')
    # im.show()
    x, y = findTheChosenOne(im)
    mouse = Mouse()
    mouse.move_mouse(startX + x, startY + y)
    mouse.left_click()
    time.sleep(1)
