from lexer import LexicalAnalyzer
import sys

def main():

    args_list = sys.argv

    if len(args_list) != 2: 
         print("Usage: python plumber.py <input file>")
         sys.exit(1)

    try: 
        simple_lexer = LexicalAnalyzer(args_list[1])
        simple_lexer.scanToken()
        simple_lexer.displayTokenTable()
        simple_lexer.outputTextFile()

    except IOError as e: 
        print(e)

if __name__ == "__main__": 
    main()