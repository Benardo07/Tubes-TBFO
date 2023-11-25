import argparse
import sys
from parsePDA import parse
from parsePDA import validate_tokens
from parsePDA import parseHTML

def main():
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


    token = parseHTML(html_file)

    PDA =  parse(text_file)

    if(validate_tokens(token,PDA)):
        print("Accepted")
    else:
        print("rejected")


if __name__ == "__main__":
    main()