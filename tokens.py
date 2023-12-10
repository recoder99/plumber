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
    FLOAT = 25
    HASH = 26

    GET = 27
    SET = 28
    DO = 29
    IF = 30
    ELIF = 31
    ELSE = 32
    FOR = 33
    WHILE = 34
    TRUE = 35
    FALSE = 36
    EOF = 37

    ERROR = 37

class Token(): 

    def __init__(self, type, lexeme, line): 
        
        self.lexeme = lexeme
        self.line = line 
        self.type = type


        
    