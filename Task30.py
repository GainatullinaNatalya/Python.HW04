# Вычислить число c заданной точностью d
import math
pi = math.pi
d = input('Введите число, задающее точность отображения числа Пи: ')

n = len(d[2:])
print(round(pi, n))