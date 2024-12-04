def is_increasing(report):
    return all(report[i] < report[i + 1] for i in range(len(report) - 1))
    #return the bool of checking every index compared to the following index for the length of the array -1 and ensure everything is increasing

def is_decreasing(report):
    return all(report[i] > report[i + 1] for i in range(len(report) - 1))
    #return the bool of checking every index compared to the following index for the length of the array -1 and ensure everything is decreasing

def check_difference(report):
    return all(1 <= abs(report[i] - report[i + 1]) <= 3 for i in range(len(report) - 1))
    #return the bool of comparing the absolute value of index minus index + 1 position and ensure it is between 1 and 3 for the length of the array

def can_be_fixed(report, condition_check):
    for i in range(len(report)):
        temp_report = report[:i] + report[i + 1:]
        #create a temporary array which is everything to the left of the index added with everything to the right of the next position, this essentially "deletes" the next position in the array
        if condition_check(temp_report) and check_difference(temp_report):
            #for each of those temporary arrays check if the array is valid, and if it is, perform the check_difference function on the temporary array
            return True
    return False


def main():
    safe_reports = 0
    #start the safe report counter

    with open("numbers.txt") as reports:
        for line_number, report in enumerate(reports.readlines(), start=1):
            #open the text file and save the lines to the report value and the start value to line_number
            levels = list(map(int, report.split()))
            #split the report as an int, map it to the list and save this array as levels
            print(f"Report {line_number}: {levels}")
            #print where we are at and the array itself
            if (is_increasing(levels) or is_decreasing(levels)) and check_difference(levels):
                #check if the array is either increasing or decreasing, if one of these is true, check to see if the level difference is valid
                print(f"Report {line_number} is safe without changes.")
                safe_reports += 1
            elif can_be_fixed(levels, is_increasing) or can_be_fixed(levels, is_decreasing):
                #if it fails any of that, check if the array can be fixed in an increasing manner, or if it can be fixed in a decreasing manner
                print(f"Report {line_number} is safe with one removal.")
                safe_reports += 1
            else:
                print(f"Report {line_number} is unsafe.")

    print(f"Total safe reports: {safe_reports}")

main()
