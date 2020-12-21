import itertools
import pathlib

path = pathlib.Path('.').parent / "inputs/21.txt"
with open(path, "r") as f:
    food_list_as_string = f.read()
    food_list = food_list_as_string.splitlines()

dict_of_possibilities = {}
all_ingredients = []

for item in food_list:
    # every line has a contains
    ingredients, allergenes = item.split(" (contains ")
    allergenes = allergenes[:-1].split(", ")
    ingredients = ingredients.split(" ")
    all_ingredients += ingredients
    ingredients = set(ingredients)
    for aller in allergenes:
        value = dict_of_possibilities.get(aller, None)
        if value is not None:
            dict_of_possibilities[aller] = dict_of_possibilities[aller].intersection(ingredients)
        else:
            dict_of_possibilities[aller] = ingredients


# p1
# ingredients_with_allerg = set()
# for k, v in dict_of_possibilities.items():
#     ingredients_with_allerg.update(v)

# count = len([x for x in all_ingredients if x not in ingredients_with_allerg])

# print(count)


dict_of_possibilities = {k: v for k, v in sorted(dict_of_possibilities.items(), key=lambda x: len(x[1]))}


list_of_possibilities = list(dict_of_possibilities.items())

list_of_allergenes = []

for i in range(len(list_of_possibilities)):
    allergy, possible_ingr = list_of_possibilities[0]
    for all, ingr in list_of_possibilities[1:]:
        if list(possible_ingr)[0] in ingr:
            ingr.remove(list(possible_ingr)[0])
    list_of_allergenes.append(list_of_possibilities[0])
    list_of_possibilities = list_of_possibilities[1:]
    list_of_possibilities = list(sorted(list_of_possibilities, key= lambda x: len(x[1])))


listt = [next(iter(x[1])) for x in sorted(list_of_allergenes, key=lambda x: x[0])]

ingredients_with_allerg = ",".join(listt)
print(ingredients_with_allerg)




# count = 0
# for item in list_of_good_ingredients:
#     count += food_list_as_string.count(item)

# print(count)