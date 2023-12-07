def get_recipe(path, search_id):
    recipe = None
    with open(path, 'r') as file:
        for line in file:
            parts = line.strip().split(',')

            if len(parts) >= 3:
                id, name, ingredients = parts[0], parts[1], parts[2:]

                if id == search_id:
                    recipe = {
                        "id": id,
                        "name": name,
                        "ingredients": ingredients
                    }
                    break

        return recipe
print(get_recipe('test6.txt', '60b90c4613067a15887e1ae5'))