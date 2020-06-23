import numpy
import pylab
import random
import time
from cycler import cycler
from typing import List
import matplotlib
from matplotlib import animation
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt


def position_list(n: int) -> List[List[int]]:

    x = numpy.zeros(n)
    y = numpy.zeros(n)

    for i in range(1, n):
        val = random.randint(1, 4)
        if val == 1:
            x[i] = x[i - 1] + 1
            y[i] = y[i - 1]
        elif val == 2:
            x[i] = x[i - 1] - 1
            y[i] = y[i - 1]
        elif val == 3:
            x[i] = x[i - 1]
            y[i] = y[i - 1] + 1
        else:
            x[i] = x[i - 1]
            y[i] = y[i - 1] - 1

    return [x, y]


colours = []
for name in matplotlib.colors.cnames.items():
    colours.append(name)
for color in colours:
    pos = position_list(random.randint(1, 10) * 1000)
    pylab.plot(pos[0], pos[1], color=color[0])
    


pylab.show()