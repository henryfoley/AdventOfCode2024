# INITIAL THOUGHT PROCESS
"""
1.) 
"""

# Imports
from pathlib import Path
import re

# Get contents of text file
ROOT_DIR = Path(__file__).parent
TEXT_FILE = ROOT_DIR / "input.txt"
input = TEXT_FILE.read_text()

# Regex
regex_key = '.+'
lines = re.findall(regex_key, input, re.MULTILINE)
