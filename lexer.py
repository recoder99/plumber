from tokens import TokenType, Token

class LexicalAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.token_table = []
    
    
    keyword_list = ['get', 'set', 'do', 'if', 'elif', 'else', 'for', 'while', 'true', 'false']
    operator_list = [' ', '\n', ':', '+', '-', '*', '/', '<<', '=', '!=', ';', '{', '}']

    alpha = ['a','A','b', 'B', 'c', 'C', 
                 'd', 'D', 'e', 'E', 'f', 'F', 
                 'g', 'G', 'h', 'H', 'i', 'I', 
                 'j', 'J', 'k', 'K', 'l', 'L', 
                 'm', 'M', 'n', 'N', 'o', 'O', 
                 'p', 'P', 'q', 'Q', 'r', 'R', 
                 's', 'S', 't', 'T', 'u', 'U', 
                 'v', 'V', 'w', 'W', 'x', 'X', 
                 'y', 'Y', 'z', 'Z']
        
    num = ['0','1','2','3','4','5','6','7','8','9']

    alnum = alpha + num 

    

    def scanToken(self):
        self.keyword_list.sort()
        self.operator_list.sort()
        self.keyword_mapping = {
        'get': TokenType.GET, 
        'set': TokenType.SET, 
        'do': TokenType.DO, 
        'if': TokenType.IF, 
        'elif': TokenType.ELIF, 
        'else': TokenType.ELSE
    }
        token_temp = ""
        is_string = False
        is_delimiter = False
        
        

        try:
            with open(self.file_path, 'r') as file:
                    
                current_line = 1 #track the current line number 
                  #for string operations
                while True:
                    
                    c = file.read(1)
                        
                    if not c:
                        if token_temp: 
                            self.tokenize(token_temp,current_line)
                        break

                    if c == '\"':
                        if not is_string:
                            self.tokenize(token_temp, current_line)
                            token_temp = c
                            is_string  = not is_string
                        else:
                            self.tokenize(token_temp + '\"', current_line)
                            token_temp = ""
                            is_string = not is_string
                        continue

                    if is_string:
                        token_temp += c
                        continue

                    if is_delimiter == False and c in self.operator_list:
                        #tokenize token_temp
                        self.tokenize(token_temp, current_line)
                        token_temp = ""
                        is_delimiter = True

                    if is_delimiter:
                        temp = token_temp + c
                        if temp in self.operator_list:
                            token_temp += c
                        else:
                            is_delimiter = False
                            self.tokenize(token_temp, current_line)
                            token_temp = c 
                        continue

                    token_temp += c

                    if c == '\n': 
                        current_line += 1

        except IOError as e:
            print(e)


    def isDigit(self,lexeme): 

        for char in lexeme: 

            if char not in self.num: 

                return False 
            
        return True    
    
    def isIdentifier(self, lexeme): 

        
        if not lexeme[0] in self.alnum or lexeme[0] == '_': 

            return False
        
        for char in lexeme[1:]: 

            if char not in self.alnum or char == '_': 
                return False 
        
        return True 
    
    def isVar(self, lexeme):

        if lexeme[0] == '$': 

            for char in lexeme[1:]: 

                if char not in self.alnum or char == '_': 

                    return False 
                
            return True 



    def tokenize(self, lexeme, line_number):

        while lexeme and lexeme[0] == ' ': 
            lexeme = lexeme[1:]

        if not lexeme:
            return

        if lexeme in self.keyword_list: 
            token_type = self.keyword_mapping.get(lexeme, TokenType.ID)

        elif lexeme[0] == '"' and lexeme[-1] == '"': 
            token_type = TokenType.STRING

        elif self.isDigit(lexeme): 
            token_type = TokenType.NUMBER

        elif lexeme == '=': 
            token_type = TokenType.EQUAL

        elif lexeme == '!=': 
            token_type = TokenType.NEQUAL

        elif lexeme == '>': 
            token_type = TokenType.GT

        elif lexeme == '>=': 
            token_type = TokenType.GT_EQUAL

        elif lexeme == '<': 
            token_type = TokenType.LT

        elif lexeme == '<=': 
            token_type = TokenType.LT_EQUAL
        
        elif lexeme == '+': 
            token_type = TokenType.PLUS 

        elif lexeme == '-': 
            token_type = TokenType.MINUS 
        
        elif lexeme == '*': 
            token_type = TokenType.STAR

        elif lexeme == '/': 
            token_type = TokenType.SLASH

        elif lexeme == ':': 
            token_type = TokenType.COL

        elif lexeme == '\n': 
            token_type = TokenType.NEWLINE

        elif lexeme == '(': 
            token_type = TokenType.LPAREN

        elif lexeme == ')': 
            token_type = TokenType.RPAREN

        elif lexeme == '{': 
            token_type = TokenType.LCBRACK

        elif lexeme == '}': 
            token_type = TokenType.RCBRACK

        elif lexeme == ';': 
            token_type = TokenType.SEMICOL

        elif lexeme == '.': 
            token_type = TokenType.DOT

        elif lexeme == '"':
            token_type = TokenType.QUOTE

        elif lexeme == '#':
            token_type = TokenType.HASH

        elif lexeme == '<<': 
            token_type = TokenType.ASMT
        
        elif self.isIdentifier(lexeme): 
            token_type = TokenType.ID

        elif self.isVar(lexeme): 
            token_type = TokenType.VAR

        elif not lexeme: 
            token_type = TokenType.EOF

        else: 

            raise ValueError(f"A lexical error has been encountered. The following lexeme is not recognized{lexeme}") 

        
        token = Token(token_type, lexeme, line_number)
        self.token_table.append((lexeme, token_type.name))

    def displayTokenTable(self):

        print("Token Table: ")
        print("{:<15} {:<15}".format("Lexeme", "Token Type"))
        print("-"*30)

        for lexeme, token_type in self.token_table: 

            print("{:<15} {:<15}".format(lexeme,token_type))
            print("-"*30)

          


     

        
            


        

