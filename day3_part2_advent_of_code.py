import re

def main():
    text = ""
    #intialize a text variable as a string
    times = []
    #initialize a times array
    sum = 0
    #start a counter for the number we need to find

    with open("numbers.txt") as multiplication:
        for line in multiplication.readlines():
            text = text + line
            #create a string variable containing the file's contents
            
    while True:
        #start the loop
        found_dont = text.find("don't()")
        #find the first don't()

        found_do = text.find("do()", found_dont + len("don't()"))
        #find the first do()

        if found_dont != -1 and found_do != -1:
            #if found
            text = text[:found_dont] + text[found_do + len("do()"):]
            #cut up the text from the RIGHT of the DON'T, then add the text back from the next DO
        elif found_dont != -1:
            text = text[:found_dont]
            #if we end on a DON'T, cut the rest of it out then stop the loop
            break
        else:
            break
            #if we end on a DO, stop the loop

    mul = re.findall("mul\([0-9]+,[0-9]+\)", text)
    #save an array of all the occurences of that were given to us by the text, they wanted us to find exactly mul([0-9]+,[0-9]+)

    for i in mul:
        times = times + re.findall("[0-9]+", i)
        #for each string in the mul array, add [0-9]+ to the times array. This is essentially making it easier for us to work with for data manipulation

    for i in range(len(times) -1):
        #for each item in the length of the array -1 so we don't have an index error
        if i % 2 == 0:
            #if that item modulo'd by 2 is 0, which means "is it even?"
            sum += int(times[i]) * int(times[i + 1])
            #multiple it by the number next to it, and add it to sum

    print(sum)
main()
