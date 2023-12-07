import re


def sanitize_file(source, output):
    with open(source, 'r') as file:
        for line in file:
            cleaned_line = re.sub(r'\d', '',line)
    with open(output, 'w') as file:
        file.write(cleaned_line)


sanitize_file('test7.txt', 'output.txt')


