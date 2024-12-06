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
            continue  # No need to check further if already safe
           
    return safe_reports

def removal_count_safe_reports(data):
    safe_reports = 0
    
    for line in data:
        # Convert each line into a list of integers (levels)
        report = list(map(int, line.split()))
        
        # Check if the report is safe without removal
        if is_safe_report(report):
            safe_reports += 1
            continue  # No need to check further if already safe
        
        # If not safe, check by removing one level at a time
        for i in range(len(report)):
            new_report = report[:i] + report[i+1:]
            if is_safe_report(new_report):
                safe_reports += 1
                break  # Stop as soon as we find a safe report by removal
           
    return safe_reports


# Read the input data
with open("AdventOfCode/Day 2/input-day2.txt") as f:
    x = f.read().strip()

# Counting the safe reports
safe_count_1 = count_safe_reports(x.split('\n'))
safe_count_2 = removal_count_safe_reports(x.split('\n'))
print(f"Number of safe reports in solution 1: {safe_count_1}")
print(f"Number of safe reports in solution 2: {safe_count_2}")