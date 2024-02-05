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
            return Token(TokenType.EOF, "End of file", len(self.token_list))
        return self.token_list[self.itr]
    
    def advance(self):
        self.itr += 1
        if self.outOfRange():
            return False
        return self.token_list[self.itr]
    
    def resetItr(self):
        self.itr = -1

    def retrieveList(self):
        return self.token_list

class SyntaxError:

    def __init__(self) -> None:
        self.isTriggered = False

    def message(self, message, token : Token):
        if self.isTriggered:
            return
        print("\033[0;31m"+f"[Line: {token.get_line()}] Syntax Error: {message}")
        print(f"Error token: {token.get_lexeme()}")
        self.isTriggered = True
    
class Parser:

    keyword_list = [TokenType.GET, TokenType.SET, TokenType.DO, TokenType.RUN, TokenType.CALL]
    expr_list = [TokenType.NUMBER, TokenType.LT, TokenType.GT, 
                 TokenType.LT_EQUAL, TokenType.GT_EQUAL, TokenType.VAR, 
                 TokenType.STRING, TokenType.TRUE, TokenType.FALSE, TokenType.FLOAT, 
                 TokenType.RPAREN, TokenType.LPAREN, TokenType.PLUS, TokenType.MINUS, 
                 TokenType.NOT, TokenType.STAR, TokenType.EQUAL]

    def __init__(self, token_list : list[Token]):
        self.token_list = TokenIterator(token_list)

    error = None

    def ParseToken(self):
        self.error = SyntaxError()
        self.token_list.advance()
        self.root()
        print("\033[0;32m" + "Syntax Analyzer finished")
        self.error = None
        pass

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
        elif self.token_list.peek().get_type() in [TokenType.ID]:
             self.error.message(f"\"{self.token_list.peek().get_lexeme()}\" is not a valid statement", self.token_list.peek())
        pass

    def pipe_stmt(self):
        self.stmt()
        while self.token_list.peek().get_type() in [TokenType.ASMT]:
            self.token_list.advance()
            self.stmt()
        pass
        if self.token_list.peek().get_type() not in [TokenType.NEWLINE, TokenType.SEMICOL]:
            self.error.message(f"{self.token_list.peek().get_lexeme()} is not a valid delimiter", self.token_list.peek())


    def con_stmt(self):
        if self.token_list.peek().get_type() in [TokenType.IF]:
            self.token_list.advance()
        if self.token_list.peek().get_type() in [TokenType.COL]:
            self.token_list.advance()
        else:
            self.error.message("\":\" Expected", self.token_list.peek())
            return
        self.expr()
        self.block_stmt()
        while self.token_list.peek().get_type() in [TokenType.ELIF]:
            if self.token_list.peek().get_type() in [TokenType.COL]:
                self.token_list.advance()
            else:
                self.error.message("\":\" Expected", self.token_list.peek())
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
            self.error.message("Expected '{'", self.token_list.peek())
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
                self.error.message("Expected \";\"", self.token_list.peek())
                return
            if self.token_list.peek().get_type() in [TokenType.RCBRACK]:
                break
        
        if self.token_list.peek().get_type() in [TokenType.RCBRACK]:
            self.token_list.advance()
        else:
            self.error.message("Expected '}'", self.token_list.peek())
            return

    def for_stmt(self):
        if self.token_list.peek().get_type() in [TokenType.FOR]:
            self.token_list.advance()
        if self.token_list.peek().get_type() in [TokenType.COL]:
                self.token_list.advance()
        else:
            self.error.message("\":\" Expected", self.token_list.peek())
            return
        if self.token_list.peek().get_type() in [TokenType.VAR]:
            self.token_list.advance()
        else:
            self.error.message("Expected variable token type", self.token_list.peek())
            return
        if self.token_list.peek().get_type() in [TokenType.IN]:
            self.token_list.advance()
        else:
            self.error.message("Expected \"in\"", self.token_list.peek())
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
            self.error.message("\":\" Expected", self.token_list.peek())
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
                        self.error.message("Expected ID at line ", self.token_list.peek())
                else: 
                    self.error.message("Expected arrow '<-' token type", self.token_list.peek())
            
            else: 
                self.error.message("Expected colon ':' ", self.token_list.peek())
            
            pass 
        
    def args(self): 

        self.var()
        while self.token_list.peek().get_type() == TokenType.COMMA: 
            self.token_list.advance()
            self.args()
        
        pass


    def stmt(self):

        if self.token_list.peek().get_type() in self.keyword_list:
            self.command()
        elif self.token_list.peek().get_type() in self.expr_list:
            self.expr()
        else:
            self.error.message(f"\"{self.token_list.peek().get_lexeme()}\" is not a valid statement", self.token_list.peek())
        pass

    def command(self):
        self.keyword()
        if self.token_list.peek().get_type() == TokenType.COL:
            self.token_list.advance()
        else:
            self.error.message("Expected \":\"")
            return
        
        if self.token_list.peek().get_type() == TokenType.ID:
            self.token_list.advance()
        else:
            self.error.message("Expected ID token type", self.token_list.peek())
            return
        
        while self.token_list.peek().get_type() in [TokenType.PARAMS]:
            self.token_list.advance()
            self.params()

    def params(self):
        if self.token_list.peek().get_type() == TokenType.ID:
            self.token_list.advance()
        else:
            self.error.message("Expected ID token type", self.token_list.peek())
            return
        if self.token_list.peek().get_type() in self.expr_list:
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

        if self.token_list.peek().get_type() in [TokenType.PLUS, TokenType.MINUS]:
            self.token_list.advance()
            if self.token_list.peek().get_type() in [TokenType.NUMBER]:
                self.integer()
                return
            elif self.token_list.peek().get_type() in [TokenType.FLOAT]:
                self.float()
                return
            self.error.message("Expected integer or float value", self.token_list.peek())
            return
            pass
        if self.token_list.peek().get_type() in [TokenType.LPAREN]:
            self.token_list.advance()
            self.expr()
            if self.token_list.peek().get_type() != TokenType.RPAREN:
                self.error.message(" Expected \")\"", self.token_list.peek())
            self.token_list.advance()
            return

        if self.token_list.peek().get_type() in (TokenType.NUMBER, TokenType.VAR, TokenType.STRING, TokenType.TRUE, TokenType.FALSE, TokenType.FLOAT):
            self.token_list.advance()
        else:
            self.error.message(f"Expression statement expected, \"{self.token_list.peek().get_lexeme()}\" is not a valid expression", self.token_list.peek())
        pass

    def integer(self):
        if self.token_list.peek().get_type() in [TokenType.NUMBER]:
            self.token_list.advance()
        return
    
    def float(self):
        if self.token_list.peek().get_type() in [TokenType.FLOAT]:
            self.token_list.advance()
        return
    
    def var(self): 

        if self.token_list.peek().get_type() in [TokenType.VAR, TokenType.INPUT]: 
            self.token_list.advance() 
        else: 
            print("Syntax Error: Expected Variable ")

  



    def OutputToken(self):
        print("Token Table: ")
        print("{}\t{}\t{} ".format("Line", "Lexeme", "Tokens"))
        print("-"*30)

        for i in self.token_list.retrieveList():
            line = i.get_line()
            print("{}\t{}\t{}".format(line, i.get_lexeme(), i.get_type()))
            print("-"*30)

    



    

    