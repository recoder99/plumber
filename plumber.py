from lexer import LexicalAnalyzer
import sys

def main():

    #for debug reasons. set this to false if not using debugger
    debug = False
    #set sample file path inside the debug_path
    debug_path = "D:\\user_data\\Documents\\code_projects\\plumber\\sample.plumb"
    #end of debug settings

    args_list = sys.argv
    if len(args_list) != 2 and not debug: 
         print("Usage: python plumber.py <input file>")
         sys.exit(1)

    try: 
        if not debug:
            simple_lexer = LexicalAnalyzer(args_list[1])
        else:
            simple_lexer = LexicalAnalyzer(debug_path)
        simple_lexer.scanToken()
        simple_lexer.displayTokenTable()
        simple_lexer.outputTextFile()

    except IOError as e: 
        print(e)

if __name__ == "__main__": 
    main()