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
    NOT = 21 
    AND = 22
    OR = 23

    ID = 24
    VAR = 25
    STRING = 26
    NUMBER = 27
    FLOAT = 28
    HASH = 29

    GET = 30
    SET = 31
    DO = 32
    IF = 33
    ELIF = 34
    ELSE = 35
    FOR = 36
    WHILE = 37
    TRUE = 38
    FALSE = 39
    EOF = 40

    ERROR = 41

class Token(): 

    def __init__(self, type, lexeme, line): 
        
        self.lexeme = lexeme
        self.line = line 
        self.type = type


        
    