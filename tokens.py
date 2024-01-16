from enum import Enum

#List of tokens 

class TokenType(Enum): 

    LPAREN = 1
    RPAREN = 2
    COL = 3
    SEMICOL = 4
    LCBRACK = 5
    RCBRACK = 6
    LBRACK = 7 
    RBRACK = 8     
    COMMA = 9
    PLUS = 10
    MINUS = 11
    STAR = 12
    SLASH = 13
    MODULO = 14 
    DOT = 15
    NEWLINE = 16
    QUOTE = 17

    ASMT = 18
    PARAMS = 19
    NEQUAL = 20
    EQUAL = 21
    GT = 22
    LT = 23
    GT_EQUAL = 24
    LT_EQUAL = 25
    NOT = 26
    AND = 27
    OR = 28

    ID = 29
    VAR = 30
    STRING = 31
    NUMBER = 32
    FLOAT = 33
    HASH = 34

    GET = 35
    SET = 36
    DO = 37
    CALL = 38
    RUN = 39
    IF = 40
    ELIF = 41
    ELSE = 42
    FOR = 43
    WHILE = 44
    IN = 45
    APL = 46 
    TRUE = 47
    FALSE = 48
    INPUT = 49
    EOF = 50

    ERROR = 51
    ARROW = 52

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


        
    