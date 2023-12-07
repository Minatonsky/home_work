def read_employees_from_file(path):
    employee_list = []
    file = open(path, 'r')
    while True:
        line = file.readline()
        if not line:
            break  # Вихід з циклу, коли досягнуте кінець файлу
        employee_list.append(line.rstrip('\n'))
    file.close()
    return employee_list


print(read_employees_from_file('test2.txt'))




