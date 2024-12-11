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

def fix_order(update, rules):
    is_fixed = False
    while True:
        swap_made = False
        for rule in rules:
            if rule[0] in update and rule[1] in update:
                rule_0_index = update.index(rule[0])
                rule_1_index = update.index(rule[1])
                if rule_0_index > rule_1_index:
                    #if the position of rule 0 is to the right of rule 1, do this
                    update[rule_0_index], update[rule_1_index] = update[rule_1_index], update[rule_0_index]
                    #swap them
                    is_fixed = True
                    swap_made = True
        if not swap_made:
            break
    return update, is_fixed

middle_pages = []
incorrect_updates = []

for update in updates:
    #for each update list in updates array
    if not is_correct_order(update, rules):
        #if it is in an incorrect order
        corrected_update, fixed = fix_order(update, rules)
        #run the fix order function passing update, and rules to it, return the updated update to corrected_update, and the fixed status
        if fixed:
            incorrect_updates.append(corrected_update)
            #append this fixed list to the incorrect updates list    
            middle_index = len(corrected_update) // 2
            #find the middle index
            if len(corrected_update) % 2 == 0:
                #if the middle index is even, do this
                middle_value = (corrected_update[middle_index - 1] + corrected_update[middle_index]) // 2
                #this is the way to find the middle value from a list that is even length
            else:
                middle_value = (corrected_update[middle_index])
                #its odd so it'll work
            middle_pages.append(middle_value) 
            #add it


result = sum(middle_pages)
#add the middle pages of all the correctly ordered updates
print("Incorrectly-ordered updates:", incorrect_updates)
print("Middle page numbers of correctly-ordered updates:", middle_pages)
print("Sum of middle page numbers:", result)
