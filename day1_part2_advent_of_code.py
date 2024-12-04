location_ID1 = []
#initilize list 1
with open("lists.txt") as myfile:
    for line in myfile.readlines():
        location_ID1.append(int(line.split()[0]))
#read the first string from the file, convert to a int, and append it to its list

location_ID2 = []
with open("lists.txt") as myfile:
    for line in myfile.readlines():
        location_ID2.append(int(line.split()[1]))

sorted_list1 = sorted(location_ID1)
sorted_list2 = sorted(location_ID2)
#sort each list so that they are numerically rising

result = []

for i in sorted_list1:
   result.append((sorted_list2.count(i) * i))
#for each item in list 1, count occurences of it in list 2, multiply the occurences by the number, and append to result

print(result)

sum = 0
for i in result:
    sum += abs(i)
    #add up all the numbers
print(sum)
