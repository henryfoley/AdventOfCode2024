# INITIAL THOUGHT PROCESS
"""
1.) Split the input into two groups
    a.) Ruleset
    b.) Updates
2.) For each update check if it is valid
    a.) For each rule in the ruleset, get their index in the current page
    b.) If the index for the first rule is greater than the second, then it is not valid
3.) Get the middle index value of each valid ruleset and add to a total
"""

def checkValidPage(currentPage, rules):
    for rule in rules:
         if rule[0] in currentPage and rule[1] in currentPage:
             index1 = currentPage.index(rule[0])
             index2 = currentPage.index(rule[1])

             if index1 > index2:
                 return False
    return True

def getMiddle(page):
    return page[(len(page)//2)]

# Imports
from pathlib import Path
import re

# Get contents of text file
ROOT_DIR = Path(__file__).parent
TEXT_FILE = ROOT_DIR / "input.txt"
input = TEXT_FILE.read_text()

# Regex
regex_key = '^([\d|]+)$|^([\d,]+)$'
matches = re.findall(regex_key, input, re.MULTILINE)

#Split into lists
ruleset = []
updates = []

for line in input.splitlines():
    match = re.match(regex_key, line)
    if match:
        if match.group(1):
            ruleset.append(match.group(1))
        elif match.group(2):
            updates.append(match.group(2))

# Implementation inspired by x3mcj on Reddit
# Create Ruleset
rules = []
for rule in ruleset:
    if '|' in rule:
        page, before = rule.split('|')
        rules.append([int(page),int(before),])

pages = []
# Create Pages
for update in updates:
    if ',' in update:
        page = [int(t) for t in update.split(',')]
        pages.append(page)

total = 0
# Evaluate Update
for page in pages:
    if checkValidPage(page, rules):
        total += getMiddle(page)

print(total)