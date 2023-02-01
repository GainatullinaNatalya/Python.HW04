# Напишите функцию encrypt_caesar(msg, shift), которая кодирует сообщение шифром
# Цезаря и возвращает его. Шифр Цезаря заменяет каждую букву в тексте на букву, которая
# отстоит в алфавите на некоторое фиксированное число позиций.

alf1 = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
alf2 = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


def encrypt_caesar(msg, shift):
    result = ''
    for x in msg:
        if x in alf1:
            ind = alf1.index(x)
            result += alf1[ind + shift]
        elif x in alf2:
            ind = alf2.index(x)
            result += alf2[ind + shift]
        else:
            result += x
    return result


def decrypt_caesar(msg, shift):
    result = ''
    for x in msg:
        if x in alf1:
            ind = alf1.index(x)
            result += alf1[ind - shift]
        elif x in alf2:
            ind = alf2.index(x)
            result += alf2[ind - shift]
        else:
            result += x
    return result

shift = int(input('Введите сдвиг: '))
msg = input('Введите сообщение: ')
#print(encrypt_caesar(msg, shift))
print(decrypt_caesar(msg, shift))

