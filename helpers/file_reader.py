'''
Utilities for AoC challenges
'''


def read_file_get_lines(day):
    file = open('input_files/day' + str(day), 'r')
    return file.readlines()
