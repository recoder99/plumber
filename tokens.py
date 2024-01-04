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
    CALL = 35
    RUN = 36
    IF = 37
    ELIF = 38
    ELSE = 39
    FOR = 40
    WHILE = 41
    IN = 42
    APL = 43 
    TRUE = 44
    FALSE = 45
    EOF = 46

    ERROR = 47

class Token(): 

    def __init__(self, type, lexeme, line : int): 
        self.lexeme = lexeme
        self.line = line
        self.type = type
    
    def get_lexeme(self):
        return self.lexeme
    
    def get_type(self):
        return self.type

    def get_line(self) -> int:
        return self.line


        
    