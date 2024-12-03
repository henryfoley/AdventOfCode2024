# INITIAL THOUGHT PROCESS
# 1.) Parse text into two lists each containing a row
# 2.) Sort the row
# 3.) Get the absolute value of the difference between the corresponding value of the index
# 4.) Add the differences

# Imports
from pathlib import Path
import re

# Get contents of text file
ROOT_DIR = Path(__file__).parent
TEXT_FILE = ROOT_DIR / "input.txt"
contents = TEXT_FILE.read_text()

# Regex
regex_key = '(\d+)\s+(\d+)'
matches = re.findall(regex_key, contents)

# Create Columns
column_1 = []
column_2 = []

for match in matches:
    column_1.append(int(match[0]))
    column_2.append(int(match[1]))

column_1.sort()
column_2.sort()

# Sum of diffences between corresponding values
differenceSum = 0

if len(column_1) != len(column_2):
    print ("Number sets are not the same length!")
else:
    for i in range(len(column_1)):
        differenceSum += abs(column_1[i] - column_2[i])

print("Sum of differences is: " + str(differenceSum))