# with open('tes.html', 'r') as file:
#     # content = file.read()
#     # print(content)
#     # for line in file:
#     #     print(line.strip()) 
#     #     print("halo")
#     i = 0
#     for huruf in file.read():
#         if (huruf != "\n"):
            
#             if(huruf == " " and i == 0):
#                 print("\n")              
#                 i += 1
#             elif(huruf != " "): 
#                 print(huruf,end="")
#                 i = 0


import argparse
import sys
from parsePDA import parse
from parsePDA import validate_tokens

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

    # Check if the html_file is a .html file
    if not args.html_file.endswith('.html'):
        print("Error: The second file must be a .html file.")
        sys.exit(1)

    # Use the parsed arguments
    text_file = args.text_file
    html_file = args.html_file

    print(f"Text file: {text_file}")
    print(f"HTML file: {html_file}")

    with open(html_file, 'r') as file:
        token = []
        temp = ''
        tempIsi = 'nostr'
        isInPetik = False
        isDalamKomentar = False
        closetag = False
        strictString = False
        firstMin = True
        
        for char in file.read():
            if isInPetik and char != '"':
                if strictString :
                    if(char != ' '):
                        temp += char
                if(char != ' '):
                    tempIsi = 'str'  
            elif isDalamKomentar and char == ' ' :
                temp = ''
            elif char == '-':
                if isDalamKomentar and firstMin:
                    temp = ''
                    temp += char
                    firstMin = False
                else :
                    temp += char
                    firstMin = True
                if(temp == "<!--"):
                    isDalamKomentar = True
                    token.append(temp)
                    temp = ''             
            elif char == '<':
                if(temp != ''):
                    token.append('str')
                    temp=''
                temp += char
                closetag = False
            elif char == '>' :
                if(isDalamKomentar):
                    temp += char
                    if(temp == "-->"):
                        token.append(temp)
                        temp = ''
                        isDalamKomentar = False
                else : 
                    if(temp != ''):
                        token.append(temp)
                        temp=''
                    token.append(char)
                    closetag = True
            elif  char == "=" and not(closetag):
                if(temp != ''):
                    if(temp == 'method' or temp == 'type'):
                        strictString = True
                    token.append(temp)
                    temp = ''
                token.append(char)
            elif char == '"' and isInPetik:
                if(strictString):
                    strictString = False
                else:
                    temp += tempIsi
                temp += char
                token.append(temp)
                temp =''
                tempIsi = 'nostr'
                isInPetik = False
            elif char == '"' and not(closetag):
                temp += char
                isInPetik = True
            elif  char != " " and char != "\n":
                temp += char
            elif char == " ":
                if(closetag) and char != '\n' and char != ' ':
                    temp  += char
                elif not(closetag) and (temp != '') and not(isDalamKomentar):
                    if(temp == 'method' or temp == 'type'):
                        strictString = True
                    token.append(temp)
                    temp = ''

    if(temp != '' and isInPetik):
        token.append(temp)
        temp = ''
    print(token)

    transition = parse(text_file)
    print(transition)

    if(validate_tokens(token,transition,'S')):
        print("Accepted")
    else:
        print("rejected")

    # Rest of your script logic here

if __name__ == "__main__":
    main()