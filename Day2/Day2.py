# INITIAL THOUGHT PROCESS
"""
1.) Parse input into individual reports
2.) For each report:
    a.) Check all levels are in/decreasing
    b.) If true then ensure difference between numbers are between 1-3
3.) If report is safe then add to total
"""

# Imports
from pathlib import Path
import re

# Get contents of text file
ROOT_DIR = Path(__file__).parent
TEXT_FILE = ROOT_DIR / "input.txt"
contents = TEXT_FILE.read_text()

# Regex
regex_key = '^(\d+(?: \d+)*)$'
rows = re.findall(regex_key, contents, re.MULTILINE)
reports = [tuple(map(int, row.split())) for row in rows]

# Initialize Variables
iterator = 0
increasing = True
numSafe = len(reports)
safe = True
to_remove = []

# Check if all levels have the same flow
for report in reports:
    prevIncreasing = increasing
    for i in range(len(report)):
        if i < len(report)-1:
            if report[i] < report[i+1]:
                increasing = True
            else:
                increasing = False
        if increasing != prevIncreasing and i !=0 :
            safe = False
            break
        else:
            safe = True
        prevIncreasing = increasing
    if not safe:
        numSafe -= 1
        to_remove.append(report)

for report in to_remove:
    reports.remove(report)
to_remove.clear()

# Check number range
for report in reports:
    safe = True
    for i in range(len(report)):
        if i < len(report)-1:
            difference = abs(report[i]-report[i+1])
            if difference > 0 and difference < 4:
                safe = True
            else:
                safe = False
                break

    if not safe:
        to_remove.append(report)

for report in to_remove:
    reports.remove(report)

# Output Number of Safe Reports
print("Total Safe Reports: " + str(len(reports)))