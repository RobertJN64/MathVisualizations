import matplotlib.pyplot as pyplot

def getPoints(r, a=1, start=0.5):
    x = start
    points = []
    for counter in range(0, 100):
        points.append(x)
        x = r * x * (a - x)
        if x < 0:
            x = 0
    return points

def getUnique(points):
    validpoints = []
    for p in points[50:]:
        found = False
        for point in validpoints:
            if abs(p - point) < 0.001:
                found = True
        if not found:
            validpoints.append(p)
    return validpoints

def plot2D():
    fig = pyplot.figure()
    plt = fig.add_subplot()
    for i in range(500, 2500):
        r = i/500
        points = getUnique(getPoints(r))
        plt.plot([r]*len(points), points, 'bo', markersize=0.5)
    plt.set_ylim(0,1)
    pyplot.show()

def plotOneCurve(r):
    fig = pyplot.figure()
    plt = fig.add_subplot()
    points = getPoints(r)
    plt.plot(points)
    plt.set_ylim(0, 1)
    pyplot.show()

def plot3Dr():
    fig = pyplot.figure()
    plt = fig.add_subplot(projection='3d')

    for i in range(11, 50):
        r = i / 10
        points = getPoints(r)
        plt.scatter(range(0,100), [r]*100, points)

    pyplot.show()