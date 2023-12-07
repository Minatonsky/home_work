def add_employee_to_file(record, path):
    file = open(path, 'a')
    file.write(record + '\n')
    file.close()

add_employee_to_file('Drake Mikelsson,33', 'test2.txt')
