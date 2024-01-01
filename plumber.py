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

    if args_list[1] == "--shell":
        while True:
            str = input("Plumber shell << ")
            if str == "":
                continue
            else:
                str += "\n"
            lex = LexicalAnalyzer(str)
            lex.scanToken()
            lex.displayTokenTable()

    try: 
        if not debug:
            f = open(args_list[1], "r")
            file_str = f.read()
            simple_lexer = LexicalAnalyzer(file_str)
        else:
            f = open(debug_path, "r")
            simple_lexer = LexicalAnalyzer(f.read())
        
        simple_lexer.scanToken()
        simple_lexer.displayTokenTable()
        simple_lexer.outputTextFile()

    except IOError as e: 
        print(e)

if __name__ == "__main__": 
    main()