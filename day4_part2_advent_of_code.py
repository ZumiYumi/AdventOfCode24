def create_array(rows, columns):
    return [[0 for i in range(columns)] for j in range(rows)]

def main():
    crossword = ""
    rows = 0
    columns = 0
    with open("numbers.txt") as file:
        for line in file.readlines():
            crossword += line.strip()
            columns = len(line.strip())
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


    for row in range(1, rows-1):
        #cut the last row off so we don't have to worry about out of bounds
        for col in range(1, columns-1):
            #cut the last column off so no out of bounds
            if empty_array[row][col] == 'A':
                    #check for pattern where MM is aligned left
                    if (empty_array[row-1][col-1] == 'M' and
                        empty_array[row+1][col+1] == 'S' and
                        empty_array[row-1][col+1] == 'M' and
                        empty_array[row+1][col-1] == 'S'):
                        XMAS_found += 1
                    #check for pattern where MM is aligned right
                    if (empty_array[row-1][col-1] == 'S' and
                        empty_array[row+1][col+1] == 'M' and
                        empty_array[row-1][col+1] == 'S' and
                        empty_array[row+1][col-1] == 'M'):
                        XMAS_found += 1
                    #check for pattern where MM is aligned bottom
                    if (empty_array[row-1][col-1] == 'M' and
                        empty_array[row+1][col+1] == 'S' and
                        empty_array[row-1][col+1] == 'S' and
                        empty_array[row+1][col-1] == 'M'):
                        XMAS_found += 1
                    #check for pattern where MM is aligned top
                    if (empty_array[row-1][col-1] == 'S' and
                        empty_array[row+1][col+1] == 'M' and
                        empty_array[row-1][col+1] == 'M' and
                        empty_array[row+1][col-1] == 'S'):
                        XMAS_found += 1

    print(f"I found this many XMASs: {XMAS_found}")

main()
