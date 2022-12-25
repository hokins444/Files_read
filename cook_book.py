import pprint

def get_shop_list_by_dishes(dishes, person_count):
  with open('recipe_book.txt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
      dish_name = line.strip()
      count_ingredients = int(file.readline())
      ingredients = []
      for ing in range(count_ingredients):
        ingredient = file.readline().strip()
        ingredient_name, quantity, measure = ingredient.split(' | ')
        ingredients.append({
          'ingredient_name': ingredient_name,
          'quantity': quantity,
          'measure': measure
        })
      file.readline()
      cook_book[dish_name] = ingredients
      # print(f'cook_book = {cook_book}')
  shop_list_by_dishes = {}
  for all_dish in dishes:
    if all_dish in cook_book.keys():
      for every_ingredients in cook_book[all_dish]:
        key = every_ingredients['ingredient_name']
        if key in shop_list_by_dishes.keys():
          shop_list_by_dishes[key]['quantity'] += int(every_ingredients['quantity']) * person_count
        else:
          mes = every_ingredients['measure']

          shop_list_by_dishes[key] = {'quantity': int(every_ingredients['quantity']) * person_count, 'measure': mes}

  return (shop_list_by_dishes)


print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
