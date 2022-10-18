from math import pi


def deg_to_gms(deg, formats='string'):
    '''
    :param deg: Градусы в десятичном представлении
    :param formats: Формат конечных данных - форматированнная строгка
    :return: Градусы, минуты, секунды - по умолчанию в формате ГГ° ММ′ СС″
    '''
    degr = int(deg)
    min = int((deg-degr)*60)
    sec = (((deg-degr)*60)-min)*60
    sec= round(sec, 5)
    answer = f'{degr}° {min}′ {sec}″'
    return answer

def gms_to_deg(degr, min, sec):
    '''
    :param degr: Градусы в формате ГГ
    :param min: Минуты в формате ММ
    :param sec: Секунды в формате СС
    :return: Градусы в десятичном представлении
    '''
    deg = degr + min/60 + sec/3600
    return deg


def deg_to_rad(deg):
    '''
    :param deg: Градусы в десятичном представлении
    :return: Градусы в радианах
    '''
    rad = deg *180*pi
    return rad


def rad_to_deg(rad):
    '''
    :param rad: Градусы в радианах
    :return: Градусы в десятичном представлении
    '''
    deg = rad/(180*pi)
    return deg

print(deg_to_gms(36.97))
print(gms_to_deg(36, 58, 12.0))
print(deg_to_rad(36.97))
print(rad_to_deg(deg_to_rad(36.97)))
