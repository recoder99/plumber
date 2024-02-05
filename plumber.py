from lexer import LexicalAnalyzer
from parser_class import Parser
import sys
import os 

def main():

    #for debug reasons. set this to false if not using debugger
    debug = False#set sample file path inside the debug_path
    debug_path = os.getcwd() + "\\sample.plumb"
    script_path = ""
    #end of debug settings

    shell = False
    script = False

    args_list = sys.argv

    if len(args_list) <= 1 and not debug:
            shell = True
        
    if len(args_list) >= 2 and not debug:
         if args_list[1] == "--help":
            print("Usage: python plumber.py <input file>")
            sys.exit(1)
         else:
             script_path += args_list[1]
             script = True

    #check if file ends with plumb
    

    if shell:
        while True:
            str = input("\033[0m"+"Plumber shell << ")
            if str == "":
                continue
            else:
                str += "\n"
            lex = LexicalAnalyzer(str)
            lex.scanToken()
            if lex.isError():
                 continue
            parser = Parser(lex.get_token_list()).ParseToken()

    if script:
        if debug:
             script_path = debug_path
        if not script_path.endswith(".plumb"):
                print("Error: Invalid file type. Try using .plumb")
                sys.exit(1)

        try:
            f = open(script_path, "r")
            file_str = f.read()
            lexer = LexicalAnalyzer(file_str)
            lexer.scanToken()
            parser = Parser(lexer.get_token_list())
            if lexer.isError():
                 return
            parser.ParseToken()


        except:
            print("some error occured")

if __name__ == "__main__": 
    main()