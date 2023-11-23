package org.recoder;

import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class Lexer {

    List<Token> tokensList = new ArrayList<>();
    String filepath;

    Lexer(String filepath){
        this.filepath = filepath;
    }

    public void catFile(String filepath) throws IOException {
        FileReader reader = new FileReader(filepath);
        int b;
        while((b=reader.read()) != -1){
            System.out.print((char)b);
        }
    }

    //Scan for each character
    public void ScanToken(String text) throws  IOException{
        FileReader reader;
        try {
            reader = new FileReader(filepath);
        } catch (IOException e){
            e.printStackTrace();
            return;
        }
        char b;
        int line = 0;

        while ((b=(char)reader.read()) != -1){
            switch (b){
                case '+':
                    addToken(TokenType.PLUS, "+", line);
                    break;
                case '-':
                    addToken(TokenType.MINUS, "-",  line);
                    break;
                case '*':
                    addToken(TokenType.STAR, "*",  line);
                    break;
                case '/':
                    addToken(TokenType.SLASH, "/",  line);
                    break;
                case '(':
                    addToken(TokenType.LPAREN, "(",  line);
                    break;
                case ')':
                    addToken(TokenType.RPAREN, ")",  line);
                    break;
                case ';':
                    addToken(TokenType.SEMICOL, ";",  line);
                    break;
                case ':':
                    addToken(TokenType.COL, ":",  line);
                    break;
            }
        }
    }


    //add token
    private void addToken(TokenType type, String lexeme, int line){
        tokensList.add(new Token(type, lexeme, line));
    }
}
