from PIL import Image
from sys import stdout

xsize = 1000
ysize = 1000

xstart = -2
xend = 2
ystart = -2
yend = 2


def inFractal(num):
    points = []
    x = 0
    for i in range(0, 10):
        x = x ** 2 + num
        for prevnum in points:
            if abs(prevnum - x) < 0.05:
                return len(points)
        points.append(x)
    return 0

colors = [(0,0,0),
          (255,0,0),
          (255,128,0),
          (255,255,0),
          (0,255,0),
          (0,0,255),
          (255,0,255)]

def drawAndSave():
    i = Image.new("RGB", (xsize,ysize))

    for xpos in range(0, xsize):
        stdout.write('\r' + str(round(xpos*100/xsize,3)) + "%")
        for ypos in range(0, ysize):
            truex = (xpos / xsize) * (xend - xstart) - xend
            truey = (ypos / ysize) * (yend - ystart) - yend

            l = inFractal(truex + truey * 1j)
            if l >= len(colors):
                color = colors[-1]
            else:
                color = colors[l]

            i.putpixel((xpos,ypos), color)


    i.save("test.png")