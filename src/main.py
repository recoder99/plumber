from lexer import LexicalFuck

def main(): 

    try: 

        filepath = "D:\\user_data\\Documents\\code_projects\\plumber\\src\\sample.plumb"
        simple_lexer = LexicalFuck(filepath)
        simple_lexer.scanToken()

    except IOError as e: 
        print(e)

if __name__ == "__main__": 

    main()