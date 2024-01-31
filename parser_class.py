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

    keyword_list = [TokenType.GET, TokenType.SET, TokenType.DO, TokenType.RUN, TokenType.CALL]
    expr_list = [TokenType.NUMBER, TokenType.VAR, TokenType.STRING, TokenType.TRUE, TokenType.FALSE, TokenType.FLOAT, TokenType.RPAREN, TokenType.LPAREN]

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
        self.gen_stmt()

        while self.token_list.peek().get_type() in [TokenType.NEWLINE, TokenType.SEMICOL]:
            self.token_list.advance()
            self.gen_stmt()
        pass
        if self.token_list.peek().get_type() == TokenType.EOF:
            pass

    def gen_stmt(self):

        if self.token_list.peek().get_type() in self.keyword_list or self.token_list.peek().get_type() in self.expr_list:
            self.pipe_stmt()
        elif self.token_list.peek().get_type() in [TokenType.IF]:
            self.con_stmt()
        elif self.token_list.peek().get_type() in [TokenType.FOR]:
            self.for_stmt()
        elif self.token_list.peek().get_type() in [TokenType.WHILE]:
            self.while_stmt()
        elif self.token_list.peek().get_type() in [TokenType.APL]: 
            self.apl_stmt()
        pass

    def pipe_stmt(self):
        self.stmt()
        while self.token_list.peek().get_type() in [TokenType.ASMT]:
            self.token_list.advance()
            self.stmt()
        pass
        if self.token_list.peek().get_type() not in [TokenType.NEWLINE, TokenType.SEMICOL]:
            print("Syntax Error: Expected Newline")


    def con_stmt(self):
        if self.token_list.peek().get_type() in [TokenType.IF]:
            self.token_list.advance()
        if self.token_list.peek().get_type() in [TokenType.COL]:
            self.token_list.advance()
        else:
            print("Syntax Error: \":\" Expected")
            return
        self.expr()
        self.block_stmt()
        while self.token_list.peek().get_type() in [TokenType.ELIF]:
            if self.token_list.peek().get_type() in [TokenType.COL]:
                self.token_list.advance()
            else:
                print("Syntax Error: \":\" Expected")
                return
            self.expr()
            self.block_stmt()
        if self.token_list.peek().get_type() in [TokenType.ELSE]:
            self.token_list.advance()
            self.block_stmt()
        pass

    def block_stmt(self):
        if self.token_list.peek().get_type() in [TokenType.LCBRACK]:
            self.token_list.advance()
        else:
            print("Syntax Error: Expected '{'")
            return

        while self.token_list.peek().get_type() in [TokenType.NEWLINE]:
            self.token_list.advance()
        
        while self.token_list.peek().get_type() not in [TokenType.EOF]:
            self.gen_stmt()

            if self.token_list.peek().get_type() == TokenType.SEMICOL: 
                self.token_list.advance()
                while self.token_list.peek().get_type() in [TokenType.NEWLINE]:
                    self.token_list.advance()
            else:
                print("Syntax Error: Expected \";\"")
                return
            if self.token_list.peek().get_type() in [TokenType.RCBRACK]:
                break
        
        if self.token_list.peek().get_type() in [TokenType.RCBRACK]:
            self.token_list.advance()
        else:
            print("Syntax Error: Expected '}'")
            return

    def for_stmt(self):
        if self.token_list.peek().get_type() in [TokenType.FOR]:
            self.token_list.advance()
        if self.token_list.peek().get_type() in [TokenType.COL]:
                self.token_list.advance()
        else:
            print("Syntax Error: \":\" Expected")
            return
        if self.token_list.peek().get_type() in [TokenType.VAR]:
            self.token_list.advance()
        else:
            print("Syntax Error: variable expected")
            return
        if self.token_list.peek().get_type() in [TokenType.IN]:
            self.token_list.advance()
        else:
            print("Syntax Error: \"in\" Expected")
            return
        self.expr()
        self.block_stmt()
        pass

    def while_stmt(self):
        if self.token_list.peek().get_type() in [TokenType.WHILE]:
            self.token_list.advance()
        if self.token_list.peek().get_type() in [TokenType.COL]:
                self.token_list.advance()
        else:
            print("Syntax Error: \":\" Expected")
            return
        self.expr()
        self.block_stmt()
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


    def stmt(self):

        if self.token_list.peek().get_type() in self.keyword_list:
            self.command()
        elif self.token_list.peek().get_type() in self.expr_list:
            self.expr()
        else:
            print("I don't know how the fuck you get here but congrats, you have a bug")
        pass

    def command(self):
        self.keyword()
        if self.token_list.peek().get_type() == TokenType.COL:
            self.token_list.advance()
        else:
            print("Syntax Error: Expected Colon")
            return
        
        if self.token_list.peek().get_type() == TokenType.ID:
            self.token_list.advance()
        else:
            print("Syntax Error: Expected ID")
            return
        
        while self.token_list.peek().get_type() in [TokenType.PARAMS]:
            self.token_list.advance()
            self.params()

    def params(self):
        if self.token_list.peek().get_type() == TokenType.ID:
            self.token_list.advance()
        else:
            print("Syntax Error: Expected ID token")
            return
        
        if self.token_list.peek().get_type() in [TokenType.PARAMS]:
            return
        
        self.expr()

    
        pass
    def keyword(self):
        keyword_list = [TokenType.GET, TokenType.SET, TokenType.DO, TokenType.RUN, TokenType.CALL]
        if self.token_list.peek().get_type() in keyword_list:
            self.token_list.advance()
        pass
        
    def expr(self):
        self.logical()
        while self.token_list.peek().get_type() == TokenType.OR:
            self.token_list.advance()
            self.logical()
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

    



    

    