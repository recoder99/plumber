from tokens import TokenType

class LexicalAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.delimiter = False
    
    keyword_list = ['get', 'set', 'do', 'if', 'elif', 'else']
    operator_list = [' ', '\n', ':', '+', '-', '*', '/', '<<', '=', '!=']

    

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
                while True:
                    c = file.read(1)    
                        #for string operations
                    if not c:
                        print("EOF")
                        break
                    if c == '\"':
                        if not is_string:
                            self.tokenize(token_temp)
                            token_temp = c
                            is_string  = not is_string
                        else:
                            self.tokenize(token_temp + '\"')
                            token_temp = ""
                            is_string = not is_string
                        continue

                    if is_string:
                        token_temp += c
                        continue

                    if is_delimiter == False and c in self.operator_list:
                        #tokenize token_temp
                        self.tokenize(token_temp)
                        token_temp = ""
                        is_delimiter = True

                    if is_delimiter:
                        temp = token_temp + c
                        if temp in self.operator_list:
                            token_temp += c
                        else:
                            is_delimiter = False
                            self.tokenize(token_temp)
                            token_temp = c 
                        continue

                    token_temp += c
                       
                                
                            # if key_itr < len(self.keyword_list):
                            #     if char_itr < len(self.keyword_list[key_itr]):
                            #         if c == self.keyword_list[key_itr][char_itr]:
                            #             char_itr += 1
                            #         else:
                            #             key_itr += 1

                        


        except IOError as e:
            print(e)

        

    def tokenize(self, lexeme):

        if lexeme in self.keyword_list: 
            token_type = self.keyword_mapping.get(lexeme, TokenType.ID)

        elif lexeme[0] == '""' and lexeme[-1] == '""': 
            token_type = TokenType.STRING

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
            token_Type = TokenType.MINUS 
        
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

        else: 
            token_type = TokenType.ID

        
            


        

