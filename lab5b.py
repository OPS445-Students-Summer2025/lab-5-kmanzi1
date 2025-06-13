#!/usr/bin/env python3
# Author ID: 183250232

def read_file_string(file_name):
    """Reads the entire contents of a file and returns it as a string."""
    with open(file_name, 'r') as file:
        return file.read()

def read_file_list(file_name):
    """Reads a file and returns its contents as a list of lines, stripping new-line characters."""
    with open(file_name, 'r') as file:
        return [line.strip() for line in file.readlines()]

def append_file_string(file_name, string_of_lines):
    """Appends a string of lines to the end of a file."""
    with open(file_name, 'a') as file:
        file.write(string_of_lines)

def write_file_list(file_name, list_of_lines):
    """Writes a list of lines to a file, each item as a separate line."""
    with open(file_name, 'w') as file:
        file.writelines(f"{line}\n" for line in list_of_lines)

def copy_file_add_line_numbers(file_name_read, file_name_write):
    """Reads from one file and writes to another, adding line numbers to each line."""
    with open(file_name_read, 'r') as infile, open(file_name_write, 'w') as outfile:
        for index, line in enumerate(infile.readlines(), start=1):
            outfile.write(f"{index}:{line.strip()}\n")

if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']

    append_file_string(file1, string1)
    print(read_file_string(file1))

    write_file_list(file2, list1)
    print(read_file_string(file2))

    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))