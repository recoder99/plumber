from tokens import TokenType, Token

class NumberNode: 
    def __init__(self, token): 
        self.token = token 

class Node:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    
class Parser:

    def __init__(self, token_list : list[Token]):
        self.token_list = token_list 
        self.token_idx = 1
        self.advance()

    def advance(self): 

        self.token_idx += 1 

        if self.token_idx < len(self.token_list): 
            self.current_token = self.token_list[self.token_idx]
        return self.current_token 
    
    def parse(self): 

        res = self.expr()

        return res
            
    def factor(self):   
        
        token = self.current_token

        if token.type == TokenType.NUMBER or token.type == TokenType.FLOAT: 
            self.advance()

            return NumberNode(token) 
        

    def term(self): 
        
        return self.binary_op(self.factor, (TokenType.STAR, TokenType.SLASH))


    def expr(self): 

        return self.binary_op(self.term, (TokenType.PLUS, TokenType.MINUS))
        


    def binary_op(self, func, op_token): 

        left = func()

        while self.current_token.type in op_token:

            op_token = self.current_token
            self.advance()
            right = func()
            left = Node(left, op_token, right)

    def ParseToken(self):
        print("Token Table: ")
        print("{}\t{}\t{} ".format("Line", "Lexeme", "Tokens"))
        print("-"*30)

        for i in self.token_list:
            line = i.get_line()
            print("{}\t{}\t{}".format(line, i.get_lexeme(), i.get_type()))
            print("-"*30)
    
    
    def outputTextFile(self): 

       filename = "Symbol_Table.txt"

       with open (filename, 'w') as f: 

        f.write("Token Table: \n")
        f.write("{:<15} {:<15} {:<15}\n".format("Line", "Lexeme", "Tokens"))
        f.write("-"*30 + "\n")

        for i in self.token_list:
            line = i.get_line()
            f.write("{:<15} {:<15} {:<15}\n".format(line, i.get_lexeme(), i.get_type()))
            f.write("-"*30 + "\n")



    

    