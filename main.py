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
        tempIsi = 'noStr'
        isInPetik = False
        for char in file.read():
            if isInPetik and char != '"':
                if(char != ' '):
                    tempIsi = 'str'
                
            elif char == '<':
                if(temp != ''):
                    token.append(temp)
                    temp=''
                temp += char
            elif char == '>' :
                if(temp != ''):
                    token.append(temp)
                    temp=''
                token.append(char)
            elif  char == "=":
                if(temp != ''):
                    token.append(temp)
                    temp = ''
                token.append(char)
            elif char == '"' and isInPetik:
                temp += tempIsi
                temp += char
                token.append(temp)
                temp =''
                tempIsi = 'noStr'
                isInPetik = False
            elif char == '"':
                temp += char
                isInPetik = True
            elif  char != " " and char != "\n":
                temp += char
            elif char == " ":
                if(temp != ''):
                    token.append(temp)
                    temp = ''

    if(temp != '' and isInPetik):
        token.append(temp)
        temp = ''
    print(token)
    # Rest of your script logic here

if __name__ == "__main__":
    main()