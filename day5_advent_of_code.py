import re

rules = []
updates = []
#start our empty lists
with open("numbers.txt") as file:
    for line in file:
        if "|" in line:
            #if the line has a pipe in it, we want to add it our rules array
            rules.append([int(x) for x in line.strip().split("|")])
            #for each complete string thats been split, convert to an int, strip the extra chars and new lines, and append it
        elif line.strip():
            #if the line has a comma in it, we want to add it to our updates array
            updates.append([int(x) for x in line.strip().split(",")])
            #for each complete string thats been split, convert to an int, strip the extra chars and new lines, and append it

def is_correct_order(update, rules):
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            #take index 1 of the rule line we are on, check if it is in the update array that has been passed, AND check if rule[1] is also in that array  
            if update.index(rule[0]) > update.index(rule[1]):
                #if previous was true, check where index 1 is positioned in the array, if it is higher than index 2 in the rule set, it is out of order  
                return False
                #as soon as one incorrect check is found, the loop exits, preventing the rest from being checked
    return True
    #if at least the second if statement for every rule returned False on this update line, all checks passed

middle_pages = []
for update in updates:
    if is_correct_order(update, rules):
        #pass the update list along with the entire rules arrays, perform the checks and if everything passes proceed to the next check
        middle_index = len(update) // 2
        #find the middle index
        middle_pages.append(update[middle_index]) 
        #add it to the middle index array to count later

result = sum(middle_pages)
#add the middle pages of all the correctly ordered updates
print("Correctly-ordered updates:", [update for update in updates if is_correct_order(update, rules)])
print("Middle page numbers of correctly-ordered updates:", middle_pages)
print("Sum of middle page numbers:", result)
