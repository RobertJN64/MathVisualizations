import matplotlib.pyplot as plt

#eq = x^2 + 3x + 6.25 = 0

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

xcoords = []
ycoords = []
zcoords = []
for imag in range(-50, 50):
    imag = imag / 10
    for i in range(-50, 50):
        i = i/10
        xval = complex(i, imag)

        zval = xval ** 2 + 3 * xval + 6.25

        if abs(zval.imag) < 100:
            xcoords.append(i)
            zcoords.append(zval.real)
            ycoords.append(imag)

ax.scatter(xcoords, ycoords, zcoords)

plt.show()