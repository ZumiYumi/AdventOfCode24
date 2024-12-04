
location_ID1 = []
with open("lists.txt") as myfile:
    for line in myfile.readlines():
        location_ID1.append(int(line.split()[0]))

location_ID2 = []
with open("lists.txt") as myfile:
    for line in myfile.readlines():
        location_ID2.append(int(line.split()[1]))

#sort each list so that they are numerically rising

sorted_list1 = sorted(location_ID1)
sorted_list2 = sorted(location_ID2)
result = []

for i in range(len(sorted_list1)):
    result.append(sorted_list1[i] - sorted_list2[i])

print(result)

sum = 0
for i in result:
    sum += abs(i)
print(sum)
