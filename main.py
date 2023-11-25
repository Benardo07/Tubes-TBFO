import argparse
import sys
from parsePDA import parse
from parsePDA import validate_tokens
from parsePDA import parseHTML

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

if(validate):
    print()
    print(GREEN + "ACCEPTED" + RESET)
    print()

else:
    print()
    print(RED + "REJECTED" + RESET)
    print(RED + "Error in Line number " + str(lineNumber) + RESET)
    print(YELLOW +"      Line " + str(lineNumber) + " : ",end="")
    print(YELLOW + lineHTML[lineNumber-1] + RESET)

    if not(inputError in PDA["input_symbols"]):
        print(BLUE + "Invalid syntax at " + GREEN + inputError + RESET)
    else:
        if expected:
            expected_inputs = ", ".join(expected)
            print(BLUE + "Expected this following elements: " + GREEN +expected_inputs + RESET)
            print()


