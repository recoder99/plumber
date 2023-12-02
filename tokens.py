from enum import Enum

#List of tokens 

class TokenType(Enum): 

    LPAREN = 1
    RPAREN = 2
    COL = 3
    SEMICOL = 4
    LCBRACK = 5
    RCBRACK = 6
    PLUS = 7
    MINUS = 8
    STAR = 9
    SLASH = 10
    DOT = 11
    NEWLINE = 12
    QUOTE = 13

    ASMT = 14
    NEQUAL = 15
    EQUAL = 16
    GT = 17
    LT = 18
    GT_EQUAL = 19
    LT_EQUAL = 20

    ID = 21
    VAR = 22
    STRING = 23
    NUMBER = 24
    HASH = 25

    GET = 26
    SET = 27
    DO = 28
    IF = 29
    ELIF = 30
    ELSE = 31
    FOR = 32
    WHILE = 33
    TRUE = 34
    FALSE = 35
    EOF = 36

    ERROR = 36

class Token(): 

    def __init__(self, type, lexeme, line): 
        
        self.lexeme = lexeme
        self.line = line 
        self.type = type

    def show_token(self): 
        print(f"('{self.lexeme}') - Token Type: {self.type}")

        
    