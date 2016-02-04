from numpy import radians, cos
from numpy.random import uniform

def gendi(amplitude, samples=360):
    n = amplitude / 10 ** (13 / 20)
    return [{
        'abscissa': j,
        'noise': uniform(-n, n),
        'ordinate': uniform(-n, n) + amplitude * cos(radians(j))
        }
            for j in range(samples)]

def entry_db(funcreturn, modelname):
    '''Заполнение БД при помощи модели modelname списком словарей funcreturn'''
    for dictionary in funcreturn:
        modelname(**dictionary).save()
    return 0

