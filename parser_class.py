from tokens import TokenType, Token

class TokenIterator:
    def __init__(self, token_list : list[Token]):
        self.token_list = token_list
        self.itr = -1

    def outOfRange(self) -> bool:
        if self.itr < len(self.token_list):
            return False
        else:
            return True
    def peek(self) -> Token:
        if self.outOfRange():
            return Token(TokenType.EOF, "End of file", 99999)
        return self.token_list[self.itr]
    
    def advance(self):
        self.itr += 1
        if self.outOfRange():
            return False
        return self.token_list[self.itr]
    
    def resetItr(self):
        self.itr = -1

class BinNode:
    def __init__(self, left : Token, op : Token, right : Token):
        self.left = left
        self.op = op
        self.right = right

class NumberNode:
    def __init__(self, number : Token):
        self.number = number

    def __repr__(self) -> str:
        return f'{self.number.get_type()}'
    
class Parser:

    def __init__(self, token_list : list[Token]):
        self.token_list = TokenIterator(token_list)


    def ParseToken(self):
        self.token_list.advance()
        self.root()
        print("Syntax Analyzer finished")
        pass

    def parse_integer(self, token): 
        try: 
            return int(token.get_lexeme())
        except ValueError: 
            print(f"Error: Invalid integer value at line {token.get_line()}")
    
    def parse_float(self, token): 
        try: 
            return float(token.get_lexeme())
        except ValueError: 
            print(f"Error: Invalid float value at line {token.get_line()}")

    def root(self):

        while not self.token_list.outOfRange() or self.token_list.peek().get_type() == TokenType.EOF:
            self.gen_stmt()
            
            while self.token_list.peek().get_type() in (TokenType.NEWLINE, TokenType.SEMICOL):
                self.token_list.advance()
                if self.token_list.peek().get_type() == TokenType.EOF: 

                    return 

                self.gen_stmt()
            print("Syntax Error: Expected Newline")
            return
        pass

    def gen_stmt(self):
        
        self.con_stmt()
        self.for_stmt()
        self.while_stmt()
        self.apl_stmt()
        self.pipe_stmt()
        
        pass

    
    def pipe_stmt(self):

        if self.token_list.peek().get_type() in [TokenType.IF, TokenType.FOR, TokenType.WHILE, TokenType.APL, TokenType.EOF, TokenType.ID, TokenType.ERROR, TokenType.NEWLINE, TokenType.SEMICOL]:
            # if self.token_list.peek().get_type() in [TokenType.EOF, TokenType.NEWLINE]:
            #     return
            # print("Syntax Error: Expected Keyword")
            # self.token_list.advance()
            return
        
        self.stmt()
        while self.token_list.peek().get_type() in [TokenType.ASMT]:
            self.token_list.advance()
            self.stmt()
            
        pass

    def con_stmt(self):

        if self.token_list.peek().get_type() == TokenType.IF: 
            self.token_list.advance()

            if self.token_list.peek().get_type() == TokenType.COL:
                self.token_list.advance() 
                self.expr()
                self.block_stmt()

                while self.token_list.peek().get_type() == TokenType.ELIF: 
                    self.token_list.advance()

                    if self.token_list.peek().get_type() == TokenType.COL: 
                        self.token_list.advance()
                        self.expr()
                        self.block_stmt()
                    
                    else: 
                        print(("Syntax Error: Expected ':' after 'elif' "))
                        
                        
                
                if self.token_list.peek().get_type() == TokenType.ELSE: 

                    self.token_list.advance()
                    self.block_stmt() 

                else: 

                    pass 
            
            else: 
                print("Syntax Error: Expected ':' after 'if'")
                
    

    def for_stmt(self):
        
        if self.token_list.peek().get_type() == TokenType.FOR: 
            
            self.token_list.advance()

            if self.token_list.peek().get_type() == TokenType.COL: 
                self.token_list.advance()
                
                if self.token_list.peek().get_type() == TokenType.VAR: 
                    self.token_list.advance()

                    if self.token_list.peek().get_type() == TokenType.IN:
                        self.token_list.advance() 
                        self.expr()
                        self.block_stmt()
                    
                    else: 
                        print("Syntax Error : Expected 'in' keyword")
                else: 
                    print("Syntax Error: Expected variable")

            else: 
                print("Syntax Error: Expected colon ':' ")
                self.token_list.advance()
        
        pass 

    

    def while_stmt(self):

        if self.token_list.peek().get_type() == TokenType.WHILE: 
            self.token_list.advance()

            if self.token_list.peek().get_type() == TokenType.COL:
                self.token_list.advance() 
                self.expr()
                self.block_stmt()
            else:
                print("Syntax Error: Expected \":\"")
        pass

    def apl_stmt(self):

        if self.token_list.peek().get_type() == TokenType.APL:
            self.token_list.advance()

            if self.token_list.peek().get_type() == TokenType.COL: 
                self.token_list.advance()
                self.args()
                self.block_stmt()

                if self.token_list.peek().get_type() == TokenType.ARROW:
                    self.token_list.advance()
                    
                    if self.token_list.peek().get_type() == TokenType.ID: 
                        self.token_list.advance()
                    else: 
                        print("Syntax Error: Expected ID")
                else: 
                    print("Syntax Error: Expected arrow '<-' ")
            
            else: 
                print("Syntax Error: Expected colon ':' ")
            
            pass 

    def args(self): 

        self.var()

        while self.token_list.peek().get_type() == TokenType.COMMA: 
            self.token_list.advance()
            self.var()
        
        pass 


    def block_stmt(self): 

        if self.token_list.peek().get_type() == TokenType.LCBRACK: 

            self.token_list.advance()

            while self.token_list.peek().get_type() not in [TokenType.RCBRACK, TokenType.EOF]: 

                self.gen_stmt()
                while self.token_list.peek().get_type() == TokenType.NEWLINE:
                        self.token_list.advance()
                if self.token_list.peek().get_type() == TokenType.SEMICOL: 
                    self.token_list.advance()
                    
            
            if self.token_list.peek().get_type() == TokenType.RCBRACK: 
                self.token_list.advance()
            
            else: 
                print("Syntax Error: Expected '}")


        else: 
            print("Syntax Error: Expected '{")
   
        pass

    def stmt(self):
        if self.token_list.peek().get_type() in [
            TokenType.VAR, 
            TokenType.NUMBER, 
            TokenType.NOT,
            TokenType.STAR,
            TokenType.SLASH,
            TokenType.MODULO, 
            TokenType.PLUS,
            TokenType.MINUS, 
            TokenType.LT,
            TokenType.LT_EQUAL, 
            TokenType.GT,
            TokenType.GT_EQUAL, 
            TokenType.EQUAL, 
            TokenType.NEQUAL, 
            TokenType.AND, 
            TokenType.OR, 
            TokenType.STRING,
            TokenType.LPAREN,
            TokenType.RPAREN]: 
            self.expr()

        else: 
            self.command()
             
        
        pass
     

    def expr(self):
        self.logical()
        while self.token_list.peek().get_type() == TokenType.OR:
            self.token_list.advance()
            self.logical()
        pass

    def command(self): 

        self.keyword()

        if self.token_list.peek().get_type() == TokenType.COL: 
            self.token_list.advance()
            
            if self.token_list.peek().get_type() == TokenType.ID: 
                self.token_list.advance()

                while self.token_list.peek().get_type() == TokenType.PARAMS:    
                    self.params()

            else: 
                print("Syntax Error: Expected identifier.")

        else:
            print("Syntax Error: Expected colon.") 
        
        pass 

    def params(self): 
        
        if self.token_list.peek().get_type() == TokenType.PARAMS: 
            self.token_list.advance()
            
            if self.token_list.peek().get_type() == TokenType.ID: 
                self.token_list.advance()
                self.expr()
            
            else: 
                print("Syntax Error: Expected Identifier.")

        else: 
            print("Syntax Error: Expected '--' ")
        pass 


    def keyword(self): 

        if self.token_list.peek().get_type() in [ 
            TokenType.GET, 
            TokenType.SET, 
            TokenType.DO, 
            TokenType.RUN, 
            TokenType.CALL, 
            TokenType.APL]:

            self.token_list.advance()
          
        else: 
            print("Syntax Error: Expected keyword")

        pass

    def logical(self):
        self.equality()
        while self.token_list.peek().get_type() in [TokenType.AND]:
            self.token_list.advance()
            self.equality()
        pass

    def equality(self):
        self.comp()
        while self.token_list.peek().get_type() in (TokenType.EQUAL, TokenType.NEQUAL):
            self.token_list.advance()
            self.comp()
        pass

    def comp(self):
        self.term()
        while self.token_list.peek().get_type() in (TokenType.LT, TokenType.LT_EQUAL, TokenType.GT, TokenType.GT_EQUAL):
            self.token_list.advance()
            self.term()
        pass

    def term(self):
        self.factor()
        while self.token_list.peek().get_type() in (TokenType.PLUS, TokenType.MINUS):
            self.token_list.advance()
            self.factor()
        pass
    
    def factor(self):
        self.not_()
        while self.token_list.peek().get_type() in (TokenType.STAR, TokenType.SLASH, TokenType.MODULO):
            self.token_list.advance()
            self.not_()
        pass

    def not_(self):
        if self.token_list.peek().get_type() == TokenType.NOT:
            self.token_list.advance()
        self.primary()
        pass

    def primary(self):
        if self.token_list.peek().get_type() in [TokenType.LPAREN]:
            self.token_list.advance()
            self.expr()
            if self.token_list.peek().get_type() != TokenType.RPAREN:
                print("Syntax Error: \")\" Expected")
            self.token_list.advance()
        else:
            if self.token_list.peek().get_type() in (TokenType.NUMBER, TokenType.VAR, TokenType.STRING, TokenType.TRUE, TokenType.FALSE, TokenType.FLOAT):
                self.token_list.advance()
            else:
                print("Syntax Error: Expression Statements Expected")
        pass
    
    def var(self): 

        if self.token_list.peek().get_type() == TokenType.VAR: 
            self.token_list.advance() 
        else: 
            print("Syntax Error: Expected Variable ")


    def OutputToken(self):
        print("Token Table: ")
        print("{}\t{}\t{} ".format("Line", "Lexeme", "Tokens"))
        print("-"*30)

        for i in self.token_list:
            line = i.get_line()
            print("{}\t{}\t{}".format(line, i.get_lexeme(), i.get_type()))
            print("-"*30)

    



    

    