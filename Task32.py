# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

list1 = input('Введите последовательность чмсел через пробел: ').split()
list2 = []
for i in list1:
    if list1.count(i) == 1:
        list2.append(i)
print(*list2)