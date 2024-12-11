# INITIAL THOUGHT PROCESS
"""
1.) 
2.) 
3.) 
4.) 
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
