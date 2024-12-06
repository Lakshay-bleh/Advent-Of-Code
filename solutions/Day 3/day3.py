f = open("AdventOfCode\solutions\Day 3\input-day3.txt")
data = f.read()

import re

def solve_puzzle(corrupted_memory):
    # Regular expressions for mul() instructions, do(), and don't()
    mul_pattern = r'mul\((\d+),(\d+)\)'  # Capture only the numbers inside mul()
    do_pattern = r'do\(\)'  # Matches do() instruction
    dont_pattern = r"don't\(\)"  # Matches don't() instruction
    
    # Start with mul enabled
    enabled = True
    total = 0
    
    # Iterate through the input string and process each relevant part
    commands = re.finditer(f'({mul_pattern}|{do_pattern}|{dont_pattern})', corrupted_memory)

    for match in commands: 

        # Check if it's a do() instruction
        if match.group(1)=="don't()":  # If it's a don't() instruction
            enabled = False
        # Check if it's a don't() instruction

        if match.group(1) == "do()":  # If it's a do() instruction
            enabled = True    

        # print(match.group(1), match.group(2), match.group(3))
        # Check if it's a mul instruction
        if match.group(1):  # If it's a mul(X,Y) match
            if enabled:
                try:
                    # Extract the values and calculate the product
                    x, y = int(match.group(2)), int(match.group(3))
                    total += x * y
                except:
                    pass

    return total

result = solve_puzzle(data)
print(result)