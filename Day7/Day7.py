# INITIAL THOUGHT PROCESS
"""
1.) Split input into two groups
    a.) Group A: Results
    b.) Group B: Numbers
2.) Start by evaluating sum of all numbers
3.) Progress through all possible operator combinations, checking
    each time for validity
4.) If valid then add all valid results and return amount
"""

# Imports
from pathlib import Path
from itertools import product
import re

# Get contents of text file
ROOT_DIR = Path(__file__).parent
TEXT_FILE = ROOT_DIR / "input.txt"
input = TEXT_FILE.read_text()

# Regex
regex_key = '^(\d+):\s([\d\s]+)$'
lines = re.findall(regex_key, input, re.MULTILINE)

results = []
number_sets = []

# Parse Input into lists
for result, numbers in lines:
    results.append(int(result))
    number_sets.append(tuple(map(int, numbers.split()))) 

valid_results = 0

for index, result in enumerate(results):
    number_set = number_sets[index]
    operations_combinations = product(['+','x'], repeat=len(number_set)-1)
    found_valid = False

    for operations in operations_combinations:
        total = number_set[0]

        # Apply the operations to the numbers
        for i in range(len(operations)):
            if operations[i] == '+':
                total += number_set[i + 1]
            elif operations[i] == 'x':
                total *= number_set[i + 1]

        if total == result:
            valid_results += result
            found_valid = True
            break
   
    if not found_valid:
        print(f"No valid operations for {number_set} to reach {result}")

print(f"Valid Result Sum: {valid_results}")