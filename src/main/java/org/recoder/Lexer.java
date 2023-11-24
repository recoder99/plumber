package org.recoder;

import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class Lexer {

    List<Token> tokenList = new ArrayList<>();
    String filepath;

    Lexer(String filepath){
        this.filepath = filepath;
    }

    //Scans the file itself.
    public void ScanFile() throws IOException{
        //file reader
        FileReader reader;
        try {
            reader = new FileReader(filepath);
        } catch (IOException e){
            e.printStackTrace();
            return;
        }

        int b; //temporary character storage

        //iterates into every character inside the file
        while ((b=reader.read()) != -1){
            //displays every character (sample logic)
            String x = "sample: " + (char)b + "\n";
            System.out.print(x);
        }

    }

    //checks if the token is valid
    private boolean CheckToken(String text){
        return false;
    }

    //identifies the type of token and stores to the token list
    private void Tokenize(){
    }


    //add token to the list
    private void AddToken(TokenType type, String lexeme, int line){
        tokenList.add(new Token(type, lexeme, line));
    }

    //returns the tokenList (Will be used in Syntax Analyzer)
    public List<Token> getToken(){
        return tokenList;
    }
}

// test 


