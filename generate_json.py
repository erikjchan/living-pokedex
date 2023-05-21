import csv
import json

def get_img_src(pokemon_name, pokemon_image):
    img_src = 'https://img.pokemondb.net/sprites/home/normal/'
    if pokemon_image:
        img_src += pokemon_image + '.png'
    elif '(M)' in pokemon_name:
        img_src += pokemon_name.lower()[:-4] + '.png'
    elif '(F)' in pokemon_name:
        img_src += pokemon_name.lower()[:-4] + '-f.png'
    elif 'n ' in pokemon_name:
        img_src += pokemon_name.lower().split()[1] + '-' + pokemon_name.lower().split()[0] + '.png'
    elif ' ' in pokemon_name:
        img_src += pokemon_name.lower().replace(' ', '-') + '.png'
    else:
        img_src += pokemon_name.lower() + '.png'
    return img_src


pokemon_dict = {}

with open(r'pokemondata - Normal.csv', encoding='utf-8') as csvf:
    csvReader = csv.DictReader(csvf)
    index = 0
    for row in csvReader:
        box_number = int(index / 30) + 1
        if box_number not in pokemon_dict:
            pokemon_dict[box_number] = []
        pokemon = {}
        pokemon['number'] = row['number']
        pokemon['name'] = row['name']
        pokemon['image'] = get_img_src(row['name'],row['image'])
        pokemon_dict[box_number].append(pokemon)
        index += 1

with open(r'pokemondata - Regional.csv', encoding='utf-8') as csvf:
    csvReader = csv.DictReader(csvf)
    index = 0
    for row in csvReader:
        box_number = int(index / 30) + 44
        if box_number not in pokemon_dict:
            pokemon_dict[box_number] = []
        pokemon = {}
        pokemon['number'] = row['number']
        pokemon['name'] = row['name']
        pokemon['image'] = get_img_src(row['name'],row['image'])
        pokemon_dict[box_number].append(pokemon)
        index += 1

with open(r'pokemondata - Gigantamax.csv', encoding='utf-8') as csvf:
    csvReader = csv.DictReader(csvf)
    index = 0
    for row in csvReader:
        box_number = int(index / 30) + 46
        if box_number not in pokemon_dict:
            pokemon_dict[box_number] = []
        pokemon = {}
        pokemon['number'] = row['number']
        pokemon['name'] = row['name']
        pokemon['image'] = get_img_src(row['name'],row['image'])
        pokemon_dict[box_number].append(pokemon)
        index += 1

with open('set-pokemon.js', 'w', encoding='utf-8') as jsonf:
    jsonf.write(json.dumps(pokemon_dict, indent=4))
with open('set-pokemon.js') as f:
    lines = f.readlines()
    lines[0] = 'var pokemonList = ' + lines[0]
with open('set-pokemon.js', 'w') as f:
    f.writelines(lines)
