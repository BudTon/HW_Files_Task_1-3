cook_list = []

with open('recipes.txt', encoding='Utf=8') as file:
    for line in file:
        cook_list.append(line.strip())

cook_book = {}
book_dict = {}
one_dish_list =[]
line_list =[]
num_name_dish = 0
ingredients_num = 1
num_line_ingredients = 1

while num_name_dish <= len(cook_list):
    num_line_end_ingredients = int(cook_list[ingredients_num]) + num_line_ingredients - 1
    while num_line_ingredients <= num_line_end_ingredients:
        num_line_ingredients += 1
        line_list = cook_list[num_line_ingredients].split('|')
        book_dict = {'ingredient_name': line_list[0], 'quantity': line_list[1], 'measure': line_list[2]}
        one_dish_list.append(book_dict)
    cook_book[cook_list[num_name_dish]] = one_dish_list
    one_dish_list = []
    num_name_dish += int(cook_list[ingredients_num]) + 3
    ingredients_num += int(cook_list[ingredients_num]) + 3
    num_line_ingredients += 3

print('cook_book = ', cook_book)
