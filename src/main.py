from lexer import Lexer

def main(): 

    try: 

        filepath = "D:\\user_data\\Documents\\code_projects\\plumber\\src\\sample.plumb"
        simple_lexer = Lexer(filepath)
        simple_lexer.scanFile()

    except IOError as e: 
        print(e)

if __name__ == "__main__": 

    main()