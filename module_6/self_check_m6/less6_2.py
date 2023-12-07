employee_list = [['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']]
path = 'test2.txt'

def write_employees_to_file(employee_list, path):
    file = open(path, 'w')
    for sub_list in employee_list:
        for item in sub_list:
            file.write(item + '\n')

    file.close()
write_employees_to_file(employee_list, path)