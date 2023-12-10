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
    NEQUAL = 16
    EQUAL = 17
    GT = 18
    LT = 19
    GT_EQUAL = 20
    LT_EQUAL = 21
    NOT = 22
    AND = 23
    OR = 24

    ID = 25
    VAR = 26
    STRING = 27
    NUMBER = 28
    FLOAT = 29
    HASH = 30

    GET = 31
    SET = 32
    DO = 33
    RUN = 34
    IF = 35
    ELIF = 36
    ELSE = 37
    FOR = 38
    WHILE = 39
    IN = 40 
    APL = 41 
    TRUE = 42
    FALSE = 43
    EOF = 44

    ERROR = 45

class Token(): 

    def __init__(self, type, lexeme, line): 
        
        self.lexeme = lexeme
        self.line = line 
        self.type = type


        
    