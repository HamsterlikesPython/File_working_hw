from pprint import pprint

file_name = 'cook_book.txt'
cook_book = {}
def file_reader(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        ingr_list_keys = ['ingredient_name', 'quantity', 'measure']
        ingr_dict = {}
        for line in file:
            dish = line.strip()
            quantity = file.readline()
            ingredients = []
            list_help = []
            for ingredient in range(int(quantity)):
                ingredient = file.readline()
                ingredients.append(ingredient.strip())
                for ing in ingredients:
                    ingred = ing.split(' | ')
                    ingr_dict = dict(zip(ingr_list_keys, ingred))
                list_help.append(ingr_dict)
                cook_book[dish] = list_help
            file.readline()
    return cook_book
#pprint(file_reader(file_name), width=120, indent=1, sort_dicts=False)

def get_shop_list_by_dishes(person_count, *dishes):
    file_reader(file_name)
    by_dishes_dict = {}
    for dish in dishes:
        if dish in cook_book:
            for i in range(len(cook_book[dish])):
                ingredient = cook_book[dish][i]['ingredient_name']
                if ingredient not in by_dishes_dict:
                    by_dishes_dict.setdefault(cook_book[dish][i]['ingredient_name'], {'measure': cook_book[dish][i]['measure'], 'quantity': int(cook_book[dish][i]['quantity']) * person_count})
                else:
                    by_dishes_dict.setdefault(cook_book[dish][i]['ingredient_name'],
                                              {'measure': cook_book[dish][i]['measure'],
                                               'quantity': int(cook_book[dish][i]['quantity']) * person_count})
                    by_dishes_dict[ingredient]['quantity'] += int(cook_book[dish][i]['quantity'])
    return by_dishes_dict

pprint(get_shop_list_by_dishes(3, 'Омлет',), width=50, indent=1, sort_dicts=False)
# если проверять на (1, 'Омлет', 'Омлет'), то непонятно, правильно ли расчёт в строке 39.
pprint(get_shop_list_by_dishes(1, 'Омлет', 'Омлет', 'Омлет'), width=50, indent=1, sort_dicts=False)
pprint(get_shop_list_by_dishes(1, 'Омлет', 'Фахитос', ), width=70, indent=1, sort_dicts=False)
