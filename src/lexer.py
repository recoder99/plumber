import io 
from tokens import TokenType, Token


class Lexer: 

    def __init__(self, file_path): 
        
        self.token_list = []
        self.file_path = file_path

    def scanFile(self): 

        try: 
            with open(self.file_path, 'r') as file: 

                for line_number, line in enumerate(file, start=1): 
                    for char in line:

                        x = f"Sample: {char}\n"
                        print(x, end="")

        except IOError as e: 
            print(e)

    def checkToken(self, text):   
    
        keyword = [TokenType.GET, TokenType.SET, TokenType.DO, 
                   TokenType.IF, TokenType.ELIF, TokenType.ELSE, 
                   TokenType.FOR, TokenType.WHILE, TokenType.TRUE, 
                   TokenType.FALSE, TokenType.EOF ]
        
        #operators = [TokenType.]
    
    def tokenize(self): 

        pass 

    def addToken(self, type, lexeme, line): 

        pass
    
    def getToken(self): 

        return self.token_list
    

