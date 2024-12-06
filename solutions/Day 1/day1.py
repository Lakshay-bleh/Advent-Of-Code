# SOLUTION 1

f=open("AdventOfCode\input-day1.txt");
x=f.read()
first,second = [],[]

#Answer for 1st part
sum = 0
l = list(map(lambda x: x.split('   '), x.split('\n')))
for i in l:
    try:
        first.append(i[0])
        second.append(i[1])
    except:
        pass

first.sort()
second.sort()

for i in range(len(first)):
    sum += abs(int(first[i])-int(second[i]))
print(sum)


#Answer of 2nd part
product = 0
for i in first:
    sum += int(i)*int(second.count(i))
print(product)


#  ------------------------------------------OPTIMISED SOLUTION 1 ------------------------------------


from collections import Counter

# Read the input
with open("AdventOfCode/input-day1.txt") as f:
    x = f.read()

# Initialize the lists
first, second = [], []

# Prepare the list of pairs, split by the '   ' delimiter
l = [line.split('   ') for line in x.split('\n') if line]

# Split the data into first and second parts
for i in l:
    if len(i) == 2:
        first.append(i[0])
        second.append(i[1])

# Answer for 1st part
sum_diff = 0
first.sort()
second.sort()

# Compute the sum of absolute differences
for f, s in zip(first, second):
    sum_diff += abs(int(f) - int(s))
print(sum_diff)

# Answer for 2nd part
product = 0
second_counts = Counter(second)

# Compute the sum for the second part
for f in first:
    product += int(f) * second_counts[f]
print(product)


# --------------------------------------------OPTIMISED SOLUTION 2 -------------------------------------------

import numpy as np
from collections import Counter

# Read the input file
with open("AdventOfCode/Day 1/input-day1.txt") as f:
    lines = f.read().splitlines()

# Initialize lists for the first and second columns
first, second = [], []

# Split data into two lists based on '   ' separator
for line in lines:
    parts = line.split('   ')
    if len(parts) == 2:  # Ensure both parts exist
        first.append(int(parts[0]))  # Convert to int for numerical operations
        second.append(int(parts[1]))  # Convert to int for numerical operations

# 1st part: Calculate sum of absolute differences between sorted values
sum_diff = np.abs(np.array(first) - np.array(second)).sum()
print(sum_diff)

# 2nd part: Calculate product of elements in 'first' with counts of corresponding values in 'second'
second_counts = Counter(second)  # Count occurrences of each 'second' value
product = sum(f * second_counts[f] for f in first)  # Sum product of values in 'first' with counts in 'second'
print(product)

# ------------------------------------------OPTIMISED SOLUTION 3 ----------------------------------------------------

import pandas as pd
import numpy as np

# Read the input data into a pandas DataFrame
df = pd.read_csv("AdventOfCode/input-day1.txt", sep='   ', header=None, names=["first", "second"])

# Remove any empty rows if they exist
df.dropna(inplace=True)

# 1st part: Calculate sum of absolute differences between sorted values
sum_diff = np.abs(df['first'].astype(int) - df['second'].astype(int)).sum()
print(sum_diff)

# 2nd part: Calculate product of elements in 'first' with counts of corresponding values in 'second'
second_counts = df['second'].value_counts()  # Count occurrences of each 'second' value
product = (df['first'].astype(int) * df['second'].map(second_counts)).sum()
print(product)