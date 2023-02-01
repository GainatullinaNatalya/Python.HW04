# Надо написать функцию choose_coffee(preference1, preference2,..., preferenceN), которая
# возвращает напиток, который можно приготовить из имеющихся продуктов (ingredients). На
# вход функция принимает заранее неизвестное количество предпочтений посетителя. Все
# напитки перечислены в порядке убывания предпочтений и гарантированно не повторяются.
# Бариста готовит наиболее предпочитаемый напиток из доступных.

def choose_coffee(*args):
    for i in args:
        if i == 'Эспрессо':
            if ingredients[0] >= 1:
                ingredients[0] -= 1
                return i
        if i == 'Капучино':
            if ingredients[0] >= 1 and ingredients[1] >= 3:
                ingredients[0] -= 1
                ingredients[1] -= 3
                return i
        if i == 'Маккиато':
            if ingredients[0] >= 2 and ingredients[1] >= 1:
                ingredients[0] -= 2
                ingredients[1] -= 1
                return i
        if i == 'Кофе по-венски':
            if ingredients[0] >= 1 and ingredients[2] >= 2:
                ingredients[0] -= 1
                ingredients[2] -= 2
                return i
        if i == 'Латте Маккиато':
            if ingredients[0] >= 1 and ingredients[1] >= 2 and ingredients[2] >= 1:
                ingredients[0] -= 1
                ingredients[1] -= 2
                ingredients[2] -= 1
                return i
        if i == 'Кон Панна':
            if ingredients[0] >= 1 and ingredients[2] >= 1:
                ingredients[0] -= 1
                ingredients[2] -= 1
                return i
    return 'К сожалению, не можем предложить Вам напиток'


ingr1 = int(input('Количество кофе: '))
ingr2 = int(input('Количество молока: '))
ingr3 = int(input('Количество сливок: '))
ingredients = [ingr1, ingr2, ingr3]
print(choose_coffee('Капучино', 'Кон Панна', 'Кофе по-венски'))
print(choose_coffee('Эспрессо', 'Маккиато', 'Капучино'))
print(choose_coffee('Эспрессо', 'Маккиато', 'Капучино', 'Кон Панна', 'Кофе по-венски'))
