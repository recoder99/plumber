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

    def factor(self):
        if self.token_list.peekToken().get_type() in (TokenType.NUMBER, TokenType.FLOAT):
            return NumberNode(self.token_list.peekToken())

    def ParseToken(self):
        self.token_list.advance()
        self.root()
        print("Syntax Analyzer finished")
        pass

    def root(self):
        while not self.token_list.outOfRange():
            self.gen_stmt()
            self.token_list.advance()
            while self.token_list.peek().get_type() in (TokenType.NEWLINE, TokenType.SEMICOL):
                self.gen_stmt()
        pass

    def gen_stmt(self):
        self.con_stmt()
        self.for_stmt()
        self.while_stmt()
        self.pipe_stmt()
        pass

    
    def pipe_stmt(self):
        self.stmt()
        self.token_list.advance()
        while self.token_list.peek().get_type() in [TokenType.ASMT]:
            self.stmt()
            self.token_list.advance()
        pass

    def con_stmt(self):

        pass

    def for_stmt(self):
        pass

    def while_stmt(self):
        pass

    def stmt(self):
        self.expr()
        pass

    def expr(self):
        self.logical()
        while self.token_list.peek().get_type() in [TokenType.OR]:
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


    def OutputToken(self):
        print("Token Table: ")
        print("{}\t{}\t{} ".format("Line", "Lexeme", "Tokens"))
        print("-"*30)

        for i in self.token_list:
            line = i.get_line()
            print("{}\t{}\t{}".format(line, i.get_lexeme(), i.get_type()))
            print("-"*30)



    

    