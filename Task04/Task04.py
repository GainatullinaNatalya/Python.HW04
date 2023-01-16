# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# сжатие
with open('file1.txt', 'r', encoding='utf-8') as file:
	list1 = file.read().split()
	print(list1)

list2 = ''
elem = ''
count = 1

for x in list1:
    if x != elem:
        if elem:
            list2 += str(count) + elem
        count = 1
        elem = x
    else:
        count += 1
else:
    list2 += str(count) + elem
    print(list2)

data = open('file2.txt', 'w', encoding='utf-8')
data.writelines(list2)
data.close

# восстановление
with open('file2.txt', 'r', encoding='utf-8') as file:
	list1 = file.read().split()
	print(list1)

list3 = ''
count = ''

for x in list2:
    if x.isdigit():
        count += x
    else:
        list3 += x * int(count)
        count = ''
print(*list3, sep=' ')

data = open('file3.txt', 'w', encoding='utf-8')
data.writelines(list3)
data.close
