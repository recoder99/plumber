package org.recoder;

import java.io.IOException;

// Press Shift twice to open the Search Everywhere dialog and type `show whitespaces`,
// then press Enter. You can now see whitespace characters in your code.
public class Main {
    public static void main(String[] args) throws  IOException{
        Lexer simpleLexer = new Lexer("sex.jabol");
        simpleLexer.catFile("C:\\Users\\roelc\\IdeaProjects\\plumber\\src\\main\\java\\org\\recoder\\sex.jabol");
    }
}