def total_salary(path):
    total = 0.0
    file = open(path, 'r')

    while True:
        line = file.readline()
        if not line:
            break  # Вихід з циклу, коли досягнуте кінець файлу

        parts = line.split(',')
        if len(parts) == 2:
            salary = float(parts[1].strip())
            total += salary

    file.close()
    return total


result = total_salary('test.txt')
print(f"Загальна заробітна плата розробників: {result}")
