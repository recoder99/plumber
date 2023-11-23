package org.recoder;

//list of tokens
enum TokenType {
    //single character tokens
    LPAREN, RPAREN, COL, SEMICOL,
    LCBRACK, RCBRACK, PLUS, MINUS, STAR, SLASH, DOT, NEWLINE, QUOTE,

    //two or more character token
    ASMT, NEQUAL, EQUAL, GT, LT, GT_EQUAL, LT_EQUAL,

    //literals
    ID, STRING, NUMBER, HASH,

    //Keywords
    GET, SET, DO, IF, ELIF, ELSE, FOR, WHILE, TRUE, FALSE,
    EOF
}

//Token Class
public class Token {
    final String lexeme;
    final TokenType type;
    //final Object literal;
    final int line;

    Token(TokenType type, String lexeme, int line){
        this.lexeme = lexeme;
        this.type = type;
        //this.literal = literal;
        this.line = line;
    }
    public void ShowToken(){
        System.out.println("('" + lexeme +"') - Token Type: " + type);
    }
}
