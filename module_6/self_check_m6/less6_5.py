def get_cats_info(path):
    cat_list = []
    with open(path, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) == 3:
                # Розпакування частин
                id, name, age = parts
                # Створення словника та додавання його до списку
                data_dict = {"id": id, "name": name, "age": age}
                cat_list.append(data_dict)

        return cat_list



print(get_cats_info('test5.txt'))