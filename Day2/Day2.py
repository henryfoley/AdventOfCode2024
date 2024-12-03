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
TEXT_FILE = ROOT_DIR / "example.txt"
contents = TEXT_FILE.read_text()

# Regex
regex_key = '^(\d+(?: \d+)*)$'
rows = re.findall(regex_key, contents, re.MULTILINE)
reports = [tuple(map(int, row.split())) for row in rows]



iterator = 0

for report in reports:
    safe = True
    increasing = True
    iterator += 1
    for i in range(len(report)):
        if i < len(report)-1:
            if report[i] < report[i+1]:
                increasing = True
            else:
                increasing = False
        print(increasing)
    # for num in report:
    #     currentNum = num
    #     previousNum = num
    #     print(currentNum)

    print("REPORT FINISHED")
    if iterator == 1:
        break