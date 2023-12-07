
dict = {'andry':'uyro18890D', 'steve':'oppjM13LL9e'}

def save_credentials_users(path, users_info):

    with open(path,'wb') as file:
        for key, value in users_info.items():
            # Об'єднати username та password розділені двокрапкою і додати символ нового рядка
            user_data = f"{key}:{value}\n"
            # Перетворити рядок в байти та записати в файл
            binary_dict = user_data.encode()
            file.write(binary_dict)

    return binary_dict

save_credentials_users('test10', dict)