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
pprint(file_reader(file_name), width=120, indent=1, sort_dicts=False)



