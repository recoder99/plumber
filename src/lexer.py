import io 
from tokens import TokenType, Token


class Lexer:

    delimiter = False


    def __init__(self, file_path): 
        
        self.token_list = []
        self.file_path = file_path


    def scanFile(self): 

        try: 
            with open(self.file_path, 'r') as file: 
                char_itr = 0
                keyword_itr = 0

                concat_text = ""
                for line_number, line in enumerate(file, start=1):
                    

                    for char in line:

                        isValid = self.checkToken(char, char_itr, keyword_itr)

                        if isValid == False:
                            keyword_itr += 1
                        else:
                            if self.delimiter == True:
                                self.tokenize(concat_text)
                                self.delimiter = False
                                char_itr = -1
                                keyword_itr = 0
                    
                        char_itr += 1
                            
                        #x = f"Sample: {char}\n"
                        #print(x, end="")

        except IOError as e: 
            print(e)


    def checkToken(self, char, file_itr, key_itr):

        keyword_list = ['get', 'set', 'do', 'if', 'elif', 'else']
        keyword_list.sort()
        operators_list = [' ','+', '-', '*', '/','<<', '=', '!=']
        operators_list.sort()


        scan_list = keyword_list + operators_list


        #check if current iteration is greater then the scan iteration
        if(file_itr > len(scan_list[key_itr])):
            
            return False
        
        print(scan_list[key_itr][key_itr])
        if(scan_list[key_itr][file_itr] == char):
            return True
        elif key_itr > 6:
            self.delimiter = True
            return True
        else:
            return False



    
        keyword = [TokenType.GET, TokenType.SET, TokenType.DO, 
                   TokenType.IF, TokenType.ELIF, TokenType.ELSE, 
                   TokenType.FOR, TokenType.WHILE, TokenType.TRUE, 
                   TokenType.FALSE, TokenType.EOF ]
        

        
        operators = {'+': TokenType.PLUS, 
                     '-': TokenType.MINUS, 
                     '*': TokenType.STAR,
                     '/': TokenType.SLASH,
                     '=': TokenType.EQUAL,
                     '!=':TokenType.NEQUAL,
                     '>=':TokenType.GT_EQUAL}
        


    
    
    def tokenize(self, lexeme): 
        print(lexeme)
        pass 

    def addToken(self, type, lexeme, line): 

        pass
    
    def getToken(self): 

        return self.token_list
    

