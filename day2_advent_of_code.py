with open("numbers.txt") as reports:
    line = 0
    safe = 0
    #create my line and safe report counters
    for report in reports.readlines():
        #go line by line in numbers.txt

        temporary_report = list(map(int, report.split()))
        #intialize a list to store values in it
        
        print(f"Report {line + 1}: {temporary_report}")
        #tell me what line we are and what's in the list

        increasing = all(temporary_report[i] < temporary_report[i + 1] for i in range(len(temporary_report) - 1 ))
        #store a bool, for every value in temporary report, compare it to the next one for the length of the array - 1 to see if it is consistently less so we don't get an index error

        descreasing = all(temporary_report[i] > temporary_report[i + 1] for i in range(len(temporary_report) - 1 ))
        #store a bool, for every value in temporary report, compare it to the next one for the length of the array - 1 to see if it is consistently more so we don't get an index error

        size_of_difference = all( 0 < abs(temporary_report[i] - temporary_report[i + 1]) < 4 for i in range(len(temporary_report) - 1))
        #store a bool, for every value in the temporary report, compare the difference of i - i + 1, for the length of the report - 1 so we don't get an index error

        if (increasing or descreasing) and size_of_difference:
            #if increasing or decreasing is true, check if size of difference is true as well

            safe += 1 
            #add to the safe counter
        line += 1
                
print(f"This many reports are safe {safe}")
