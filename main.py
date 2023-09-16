cook_book = {}
b1 = {}

# with open('recipes.txt', encoding='Utf=8') as f:
#     data = f.read()
#
# print(data)

# Пример 2 - читаем построчно
# with open('recipes.txt', encoding='Utf=8') as f:
#     print(f.readline().strip())
#     print(f.readline().strip())
#     print(f.readline().strip())
#     print(f.readline() == '')
#     print(f.readline() is None)


# Пример 3 - читаем строки (все) - читается все,  но записывается в список
# with open('recipes.txt', encoding='Utf=8') as f:
#     lines = f.readlines()
#     print(type(lines))
#     print(len(lines))
#     print(type(int(lines[1])))
#     print(int(lines[1]) == 3)
#     print(type(lines[1]))
cook_list = []
l1 =[]
l2 =[]
# Пример 4 - читаем итеративно
with open('recipes.txt', encoding='Utf=8') as file:
    for line in file:
        cook_list.append(line.strip())
print(cook_list)


# cook_book = {
#   'Омлет': [
#     {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
#     {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
#     {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
#     ],
#   'Утка по-пекински': [
#     {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
#     {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
#     {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
#     {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
#     ],
#   'Запеченный картофель': [
#     {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
#     {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
#     {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
#     ]
#   }
q = 0
d = 1
n = 1
while q <= len(cook_list):
    c = int(cook_list[d]) + n - 1
    print(c, '-c1')
    print(n, '-n0')
    print(q, 'q1')
    while n <= c:
        n += 1
        print(n, 'n1')
        l2 = cook_list[n].split()
        print(l2)
        b1 = {'ingredient_name': l2[0], 'quantity': l2[2], 'measure': l2[4]}
        l1.append(b1)
    cook_book[cook_list[q]] = l1
    l1 = []
    # # b1 = {}
    # print(b1)
    q += int(cook_list[d]) + 3
    d += int(cook_list[d]) + 3
    print(d, '-d')
    n += 3
    # c = c+d
    print(q, 'q2')
    print()


# print(l1, '-l1')
# print(l2, '-l2')
# print(b1, '-b1')
print('cook_book = ', cook_book, '-!!!!!')
