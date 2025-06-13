#!/usr/bin/env python3
# Author ID: 183250232

def read_file_string(file_name):
    
    with open(file_name, 'r') as file:
        return file.read()

def read_file_list(file_name):
    
    with open(file_name, 'r') as file:
        return [line.strip() for line in file.readlines()]

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))