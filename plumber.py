from lexer import LexicalAnalyzer
import sys

def main():

    args_list = sys.argv

    try: 
        simple_lexer = LexicalAnalyzer(args_list[1])
        simple_lexer.scanToken()

    except IOError as e: 
        print(e)

if __name__ == "__main__": 
    main()