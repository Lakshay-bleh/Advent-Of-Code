f=open("AdventOfCode\Day 2\input-day2.txt")
x=f.read()

def is_safe_report(report):
    # Check if the report is either all increasing or all decreasing
    increasing = True
    decreasing = True
    for i in range(1, len(report)):
        diff = abs(report[i] - report[i - 1])
        if diff < 1 or diff > 3:  # Check if the difference is within the allowed range
            return False
        
        if report[i] > report[i - 1]:
            decreasing = False
        elif report[i] < report[i - 1]:
            increasing = False
    
    # Report is safe if it is either all increasing or all decreasing
    return increasing or decreasing

def count_safe_reports(data):
    safe_reports = 0
    for line in data:
        # Convert each line into a list of integers (levels)
        report = list(map(int, line.split()))
        
        # Check if the report is safe without removal
        if is_safe_report(report):
            safe_reports += 1
        else:
            # If not safe, check by removing one level at a time
            found_safe_by_removal = False
            for i in range(len(report)):
                # Create a new report by removing the level at index i
                new_report = report[:i] + report[i+1:]
                if is_safe_report(new_report):
                    found_safe_by_removal = True
                    break
            
            if found_safe_by_removal:
                safe_reports += 1
    
    return safe_reports


# Counting the safe reports
safe_count = count_safe_reports(x.split('\n'))
print(f"Number of safe reports: {safe_count}")