from tokens import TokenType, Token


class Node:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    
class Parser:

    def __init__(self, token_list : list[Token]):
        self.token_list = token_list

    def ParseToken(self):
        print("Token Table: ")
        print("{}\t{}\t{} ".format("Line", "Lexeme", "Tokens"))
        print("-"*30)

        for i in self.token_list:
            line = i.get_line()
            print("{}\t{}\t{}".format(line, i.get_lexeme(), i.get_type()))
            print("-"*30)


    

    