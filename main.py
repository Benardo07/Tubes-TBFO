import argparse
import sys
from parsePDA import parse
from parsePDA import validate_tokens
from parsePDA import parseHTML
from parsePDA import output_to_terminal

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RESET = "\033[0m"
BLUE = "\033[34m"   # Blue text
MAGENTA = "\033[35m" # Magenta text
CYAN = "\033[36m"    # Cyan text
WHITE = "\033[37m"   # White text

parser = argparse.ArgumentParser(description="Process some files.")

# Positional arguments
parser.add_argument('text_file', type=str, help='Path to the text file (e.g., pda.txt)')
parser.add_argument('html_file', type=str, help='Path to the HTML file (e.g., inputReject.html)')

# Parse arguments
args = parser.parse_args()

if not args.text_file.endswith('.txt'):
    print("Error: The first file must be a .txt file.")
    sys.exit(1)

if not args.html_file.endswith('.html'):
    print("Error: The second file must be a .html file.")
    sys.exit(1)

text_file = args.text_file
html_file = args.html_file


token , lineHTML = parseHTML(html_file)

PDA =  parse(text_file)



validate, inputError, lineNumber ,stack_symbol,expected = validate_tokens(token,PDA)

output_to_terminal(validate,inputError,lineNumber,stack_symbol,expected,lineHTML,PDA)


