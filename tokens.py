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
    STRING = 22
    NUMBER = 23
    HASH = 24

    GET = 25
    SET = 26
    DO = 27
    IF = 28
    ELIF = 29
    ELSE = 30
    FOR = 31
    WHILE = 32
    TRUE = 33
    FALSE = 34
    EOF = 35

class Token(): 

    def __init__(self, type, lexeme, line): 
        
        self.lexeme = lexeme
        self.line = line 
        self.type = type

    def show_token(self): 
        print(f"('{self.lexeme}') - Token Type: {self.type}")

        
    