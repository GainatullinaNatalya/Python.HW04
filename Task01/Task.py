# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

with open('file.txt', 'r', encoding='utf-8') as file:
	list1 = file.read().split()
	print(list1)
list2 = list(filter(lambda word: 'а' not in word and 'б' not in word and 'в' not in word, list1))
print(list2)