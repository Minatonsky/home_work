def is_equal_string(utf8_string, utf16_string):
    try:
        utf8_decoded = utf8_string.decode('utf-8')
        utf16_decoded = utf16_string.decode('utf-16')
        return utf8_decoded == utf16_decoded
    except UnicodeDecodeError:
        # Якщо виникає помилка декодування, то рядки не можуть бути однаковими
        return False


# Є два рядки у різних кодуваннях - "utf-8" та "utf-16". Нам необхідно зрозуміти, чи дорівнюються рядки між собою.
# Реалізуйте функцію is_equal_string(utf8_string, utf16_string), яка повертає True, якщо рядки дорівнюють собі, і False — якщо ні.