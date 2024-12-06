import re

def create_array(rows, columns):
    return [[0 for i in range(columns)] for j in range(rows)]


def main():
    crossword = ""
    rows = 0
    with open("numbers.txt") as file:
        for line in file.readlines():
            crossword = crossword + line.strip()
            columns = len(line) 
            rows += 1
        print(crossword)
        print(f"There are this many rows: {rows}")
        print(f"There are this many columns: {columns}")
    empty_array = create_array(rows, columns)
    index = 0
    XMAS_found = 0
    for i in range(rows):
        for j in range(columns):
            empty_array[i][j] = crossword[index]
            index += 1
    print(empty_array)
    

    for row in range(len(empty_array)):
        for element in range(len(empty_array[row])):

            #check right   
            if element + 3 < len(empty_array[row]):
                if empty_array[row][element] == 'X' and empty_array[row][element + 1] == 'M' and  empty_array[row][element + 2] == 'A' and empty_array[row][element + 3] == 'S':
                    XMAS_found += 1
            #check left
            if element - 3 >= 0:
                if empty_array[row][element] == 'X' and empty_array[row][element - 1] == 'M' and  empty_array[row][element - 2] == 'A' and empty_array[row][element - 3] == 'S':
                    XMAS_found += 1
            #check down
            if row + 3 < len(empty_array):
                if empty_array[row][element] == 'X' and empty_array[row + 1][element] == 'M' and  empty_array[row + 2][element] == 'A' and empty_array[row + 3][element] == 'S':
                    XMAS_found += 1
            #check up
            if row - 3  >= 0:
                if empty_array[row][element] == 'X' and empty_array[row - 1][element] == 'M' and  empty_array[row - 2][element] == 'A' and empty_array[row - 3][element] == 'S':
                    XMAS_found += 1
            #check down right
            if element + 3 < len(empty_array[row]) and row + 3 < len(empty_array):
                if empty_array[row][element] == 'X' and empty_array[row + 1][element + 1] == 'M' and  empty_array[row + 2][element + 2] == 'A' and empty_array[row + 3][element + 3] == 'S':
                    XMAS_found += 1
            #check up left
            if element - 3 >= 0 and row - 3 >= 0:
                if empty_array[row][element] == 'X' and empty_array[row - 1][element - 1] == 'M' and  empty_array[row - 2][element - 2] == 'A' and empty_array[row - 3][element - 3] == 'S':
                    XMAS_found += 1
            #check up right
            if element + 3 <= len(empty_array[row]) and row - 3 >=0:
                if empty_array[row][element] == 'X' and empty_array[row - 1][element + 1] == 'M' and  empty_array[row - 2][element + 2] == 'A' and empty_array[row - 3][element + 3] == 'S':
                    XMAS_found += 1
            #check down left
            if row + 3 <= len(empty_array) and element - 3 >= 0:
                if empty_array[row][element] == 'X' and empty_array[row + 1][element - 1] == 'M' and  empty_array[row + 2][element - 2] == 'A' and empty_array[row + 3][element - 3] == 'S':
                    XMAS_found += 1


    print(f"I found this many XMASs {XMAS_found}")
main()
