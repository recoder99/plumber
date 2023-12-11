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
    MODULO = 11 
    DOT = 12
    NEWLINE = 13
    QUOTE = 14

    ASMT = 15
    PARAMS = 16
    NEQUAL = 17
    EQUAL = 18
    GT = 19
    LT = 20
    GT_EQUAL = 21
    LT_EQUAL = 22
    NOT = 23
    AND = 24
    OR = 25

    ID = 26
    VAR = 27
    STRING = 28
    NUMBER = 29
    FLOAT = 30
    HASH = 31

    GET = 32
    SET = 33
    DO = 34
    RUN = 35
    IF = 36
    ELIF = 37
    ELSE = 38
    FOR = 39
    WHILE = 40
    IN = 41 
    APL = 42 
    TRUE = 43
    FALSE = 44
    EOF = 45

    ERROR = 46

class Token(): 

    def __init__(self, type, lexeme, line): 
        
        self.lexeme = lexeme
        self.line = line 
        self.type = type


        
    