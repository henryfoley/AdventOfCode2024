# INITIAL THOUGHT PROCESS
"""
1.) Split the input into two groups
    a.) Ruleset
    b.) Page updates
2.) Take ruleset and create ordered list of pages
3.) Input update order and compare if current number has a lower index then the next number
    a.) Ex. If 61 is the third page in the ruleset, then the next number 53 should have a 
    higher index in the ordered list than 61
4.) If list is evaluated correctly then add middle number to total
"""

# Imports
from pathlib import Path
import re

# Get contents of text file
ROOT_DIR = Path(__file__).parent
TEXT_FILE = ROOT_DIR / "example.txt"
contents = TEXT_FILE.read_text()

# Regex
regex_key = 'mul\(*(\d+)\,(\d+)\)'
matches = re.findall(regex_key, contents, re.MULTILINE)

total = 0
print(contents)

