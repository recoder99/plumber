from lexer import Lexer

def main(): 

    try: 

        filepath = "C:\\Users\\roelc\\IdeaProjects\\plumber\\src\\main\\java\\org\\recoder\\test.plumb"
        simple_lexer = Lexer(filepath)
        simple_lexer.scanFile()

    except IOError as e: 
        print(e)

if __name__ == "__main__": 

    main()