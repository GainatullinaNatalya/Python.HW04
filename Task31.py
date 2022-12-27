# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N

N = int(input('Введите число N: '))
list_dig = []
i = 2
while i <= N:
    if N % i == 0:
        list_dig.append(i)
        N //= i
    else:
        i += 1
print(*list_dig)
