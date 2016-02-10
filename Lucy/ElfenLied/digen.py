from numpy import radians, cos
from numpy.random import uniform

def gendi(amplitude=1, samples=360):
    n = amplitude / 10 ** (13 / 20)
    return [{
        'abscissa': j,
        'noise': uniform(-n, n),
        'ordinate': uniform(-n, n) + amplitude * cos(radians(j))
        }
            for j in range(samples)]

