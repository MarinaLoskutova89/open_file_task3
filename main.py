# Task3
import os
from pathlib import Path

path = os.getcwd()
directory = [f for f in os.listdir(path) if f.endswith('.txt')]
def get_size_doc(files_name):
    document_size = {}
    sorted_document = {}
    for name in files_name:
        with open(f'{name}', encoding='utf-8') as file:
            lines = len([line.strip() for line in file if line.strip() != ''])
        document_size[name] = lines
    sorted_doc = sorted(document_size, key=document_size.get)
    for w in sorted_doc:
        sorted_document[w] = document_size[w]
    return sorted_document

def write_new_file(file_name):
    with open(f'{file_name}', 'w', encoding='utf-8') as file:
        directory_dict = get_size_doc(directory)
        list_key = []
        list_value = []
        for key, value in directory_dict.items():
            list_key.append(key)
            list_value.append(value)
        for i in range(len(list_key)):
            with open(f'{list_key[0]}', 'a', encoding='utf-8') as second, open(f'{list_key[i+1]}', encoding='utf-8') as first:
                data = first.read()
                second.write(f'{list_key[i+1]} \n')
                second.write(f'{list_value[i+1]} \n')
                second.write(f'{data} \n')
                second.write('\n')


write_new_file('new file.txt')
