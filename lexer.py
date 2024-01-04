from tokens import TokenType, Token


class StringIterator:

    def __init__(self, string : str):
        self.string = string
        self.str_len = len(string)

    itr = -1
    current_line = 1
    newline = False

    def reset_itr(self):
        self.itr = -1
        self.current_line = 1

    def read_itr(self):
        self.itr += 1
        if not self.check_out_of_range():
            if self.string[self.itr] == '\n':
                self.current_line += 1
            return self.string[self.itr]
        else:
            return None
    
    def check_out_of_range(self):
        if self.itr >= self.str_len:
            return True
        else:
            return False
        
    def get_current_line(self) -> int:
        return self.current_line
    


class LexicalAnalyzer:

    def __init__(self, string : str):
        self.string = string
        self.token_table = []
        self.token_list = []
        self.invalid_characters = [' ', ',', '.', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '[', ']', '{', '}', '+', '-', '=', '/', '\\', '|', ':', ';', '"', "'", '<', '>', '?', '`', '~']

    
    
    keyword_list = ['get', 'set', 'do', 'call', 'run', 'if', 'elif', 'else', 'for', 'while', 'in', 'apl', 'true', 'false']
    operator_list = [' ', '\n', '=', ':', '+', '-', '*', '/','#', '%', '>', '>=', '<', '<=', '<<', '--', '==', '!=', '!',  '&&', '||', ';', '{', '}']
    char_ignore = [' ', '#'] #useless for now

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
        'call': TokenType.CALL,
        'run' : TokenType.RUN,
        'if': TokenType.IF, 
        'elif': TokenType.ELIF, 
        'else': TokenType.ELSE,
        'for' : TokenType.FOR, 
        'while' : TokenType.WHILE,
        'in' : TokenType.IN,
        'apl' : TokenType.APL, 
        'true' : TokenType.TRUE,
        'false' : TokenType.FALSE 
    }
        token_temp = ""
        #is_string = False
        is_delimiter = False
                    
        current_line = 1 #track the current line number 
        #for string operations
        str_file = StringIterator(self.string)

        c = str_file.read_itr()

        while True:
            if c == None:
                if token_temp: 
                    self.tokenize(token_temp, str_file.get_current_line())
                break
            #if the character is a comment
            if c == "#":
                multiline = False
                if str_file.read_itr() == "#":
                    multiline = True
                    while str_file.read_itr() != "#":
                        multiline = True
                        #ignore everything
                    if str_file.read_itr() != "#":
                        print("Expected # for multiline comment")
                
                if multiline == False:
                    while str_file.read_itr() != "\n" and not str_file.check_out_of_range():
                        multiline = False
                        #ignore everything
                c = str_file.read_itr()
                continue

            #if a character is a string
            if c == "\"":
                string_temp = "\""
                c = str_file.read_itr()
                while c != "\"" and c != None:
                    if c == "\n":
                        break
                    string_temp += c
                    c = str_file.read_itr()

                if c == "\"":
                    string_temp += c
                self.tokenize(string_temp, str_file.get_current_line())
                c = str_file.read_itr()
                #proceeds to next character after tokenization
                continue

            #if the character is a delimiter or a special operator
            if c in self.operator_list:
                i = 0
                c_temp = ""

                while c in self.operator_list:
                    comp = c_temp + c
                    if comp in self.operator_list:
                            c_temp += c
                            c = str_file.read_itr()
                    else:
                        break
                self.tokenize(c_temp, str_file.get_current_line())       
                continue                
                

            #if a character is a keyword or a constant
            #it should iterate until it reaches a delimiter
            temp = ""
            while c not in self.operator_list and c != None:
                temp += c
                c = str_file.read_itr()
            
            self.tokenize(temp, str_file.get_current_line())

    def isDigit(self,lexeme): 

        for char in lexeme: 

            if char not in self.num: 

                return False 
            
        return True    
    
    def isFloat(self,lexeme): 

        decimal_point = 0 

        for char in lexeme: 

            if char == '.': 
                decimal_point += 1 

            elif char not in self.num: 
                return False 
            
        return decimal_point == 1 


    
    def isIdentifier(self, lexeme): 

        
        if not lexeme[0] in self.alnum or lexeme[0] == '_': 

            return False
        
        for char in lexeme[1:]: 
            
            if not (char in self.alnum or char == '_'): 

                return False 

        return True    


    def isVar(self, lexeme):

        
        if lexeme[0] == '$': 

            for char in lexeme[1:]: 

                if char not in self.alnum or char == '_': 

                    return False 
                
            return True 



    def tokenize(self, lexeme, line_number : int):

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

        elif self.isFloat(lexeme): 
            token_type = TokenType.FLOAT

        elif lexeme == '==': 
            token_type = TokenType.EQUAL

        elif lexeme == '!=': 
            token_type = TokenType.NEQUAL

        elif lexeme == '!': 
            token_type = TokenType.NOT

        elif lexeme == '&&': 
            token_type = TokenType.AND

        elif lexeme == '||': 
            token_type = TokenType.OR 

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

        elif lexeme == '%': 
            token_type = TokenType.MODULO

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

        elif lexeme == '--':
            token_type = TokenType.PARAMS
        
        elif self.isIdentifier(lexeme): 
            token_type = TokenType.ID

        elif self.isVar(lexeme): 
            token_type = TokenType.VAR

        elif not lexeme: 
            token_type = TokenType.EOF

        else: 
            token_type = TokenType.ERROR
            print(f"A lexical error has been encountered. The following lexeme is not recognized{lexeme}") 

        
        token = Token(token_type, lexeme, line_number)
        self.token_table.append((lexeme, token_type.name))
        self.token_list.append(token)

    def get_token_list(self):
        return self.token_list
    
    def displayTokenTable(self):

        print("Token Table: ")
        print("{:<15} {:<15}".format("Lexeme", "Tokens"))
        print("-"*30)

        for lexeme, token_type in self.token_table: 

            print("{:<15} {:<15}".format(lexeme,token_type))
            print("-"*30)

    def outputTextFile(self): 

       filename = "Symbol_Table.txt"

       with open (filename, 'w') as f: 

           f.write("Symbol Table: \n")
           f.write("{:<15} {:15}\n".format("Lexeme", "Tokens"))
           f.write("-"*30 + "\n")

           for lexeme, token_type in self.token_table: 

               f.write("{:<15} {:<15}\n".format(lexeme,token_type))
               f.write("-"*30 + "\n")

          


     

        
            


        

