import base64

list = ['andry:uyro18890D', 'steve:oppjM13LL9e']
def encode_data_to_base64(data):
    list_binary = []
    for line in data:
        line_byte = line.encode('utf-8')
        base64_bytes = base64.b64encode(line_byte)
        base64_line = base64_bytes.decode('utf-8')
        list_binary.append(base64_line)
    return list_binary


print(encode_data_to_base64(list))