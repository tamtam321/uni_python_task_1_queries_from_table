import numpy as np

# Fájl beolvasás
with open("dataset.csv", "r") as rf:
    tmp_np_list = np.array(rf.read().splitlines())

# Címkék törlése
tmp_np_list = np.delete(tmp_np_list, 0)

product_list = []
product_name = []
product_type = []
product_status = []
product_platform = []
product_price = []

# ";" eltávolítása és termék adatok szétválasztása
for i in range(len(tmp_np_list)):
    product_list.append(tmp_np_list[i].split(";"))

for product in product_list:
    product_name.append(product[0])
    product_type.append(product[1])
    product_status.append(product[2])
    product_platform.append(product[3])
    product_price.append(product[4])

#print(tmp_np_list)
print(product_list)
print(product_name)
print(product_type)
print(product_status)
print(product_platform)
print(product_price)

# Árak int típusra alakítva
product_price_int = [int(e) for e in product_price]

print(product_price_int)
print("Max price: ", max(product_price_int))

# Raktáron lévő játékok árainak eltárolása int-ben
product_game_in_store_price_list = \
    [int(product[4]) for product in product_list if product[1] == "Jatek" and product[2] == "Raktaron"]

print("game prices: ", product_game_in_store_price_list)
print("Max game price: ", max(product_game_in_store_price_list))

# Raktáron lévő játékok neveinek és árainak eltárolása dictionaryben
product_game_in_store_price_dict = \
    {product[0]: int(product[4]) for product in product_list if product[1] == "Jatek" and product[2] == "Raktaron"}

print(product_game_in_store_price_dict)

# A legdrágább raktáron lévő játék keresés
most_exp_game = {}

for k, v in product_game_in_store_price_dict.items():
    if v == max(product_game_in_store_price_list):
        most_exp_game[k] = v

print("\n___________Task 'A' result______________")
print("The most expensive game: ")
for i in most_exp_game:
    print(i, ": ", most_exp_game[i])
print()

# Használt játékok árainak medián számolása
used_game_price_list = []

# Kigyűjtöm a használt játékoknak az árait egy listába
for product in product_list:
    if "hasznalt" in product[0] and product[1] == "Jatek":
        used_game_price_list.append(int(product[4]))

# sorba rendezés
used_game_price_list.sort()
print(used_game_price_list)

# Medián számolás
used_game_price_median = -1

if len(used_game_price_list) % 2 == 0:
    numb1 = used_game_price_list[(len(used_game_price_list) // 2) - 1]
    numb2 = used_game_price_list[(len(used_game_price_list) // 2)]
    used_game_price_median = (numb1 + numb2) / 2
else:
    used_game_price_median = used_game_price_list[(len(used_game_price_list) // 2) - 1]

print("\n___________Task 'B' result______________")
print("Median of used games price: ", used_game_price_median)
print()

# Platformhoz tartozó termékszám raktáron számolás
platform_product_quantity_dict = {}

# Megszámolom, hogy raktáron az adott platformhoz hány termék van
for i in range(len(product_platform)):
    if product_status[i] == "Raktaron":
        if product_platform[i] in platform_product_quantity_dict:
            platform_product_quantity_dict[product_platform[i]] += 1
        else:
            platform_product_quantity_dict[product_platform[i]] = 1

print("\n___________Task 'C' result______________")
print("Quantity of products for each platform in store:")
for k, v in platform_product_quantity_dict.items():
    print(k, ":", v)
print()
