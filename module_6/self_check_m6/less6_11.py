def get_credentials_users(path):
    try:
        with open(path, 'rb') as file:
            # Читаємо байтовий файл та декодуємо його у рядки
            lines = file.read().decode('utf-8').split('\n')
            # Видаляємо порожні рядки (останній може бути порожнім через символ нового рядка в кінці файлу)
            lines = [line for line in lines if line]
            return lines
    except Exception as e:
        print(f"Помилка при отриманні даних: {e}")
        return []


print(get_credentials_users('test10'))