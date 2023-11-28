class LexicalFuck:
    def __init__(self, file_path):
        self.file_path = file_path
        self.delimiter = False
    
    keyword_list = ['get', 'set', 'do', 'if', 'elif', 'else']
    operator_list = [' ', '\n', ':', '+', '-', '*', '/', '<<', '=', '!=']

    def scanToken(self):
        self.keyword_list.sort()
        self.operator_list.sort()
        token_temp = ""
        is_string = False
        is_delimiter = False
        try:
            with open(self.file_path, 'r') as file:
                while True:
                    c = file.read(1)    
                        #for string operations
                    if not c:
                        print("EOF")
                        break
                    if c == '\"':
                        if not is_string:
                            self.tokenize(token_temp)
                            token_temp = c
                            is_string  = not is_string
                        else:
                            self.tokenize(token_temp + '\"')
                            token_temp = ""
                            is_string = not is_string
                        continue

                    if is_string:
                        token_temp += c
                        continue

                    if is_delimiter == False and c in self.operator_list:
                        #tokenize token_temp
                        self.tokenize(token_temp)
                        token_temp = ""
                        is_delimiter = True

                    if is_delimiter:
                        temp = token_temp + c
                        if temp in self.operator_list:
                            token_temp += c
                        else:
                            is_delimiter = False
                            self.tokenize(token_temp)
                            token_temp = c 
                        continue

                    token_temp += c
                       
                                
                            # if key_itr < len(self.keyword_list):
                            #     if char_itr < len(self.keyword_list[key_itr]):
                            #         if c == self.keyword_list[key_itr][char_itr]:
                            #             char_itr += 1
                            #         else:
                            #             key_itr += 1

                        


        except IOError as e:
            print(e)

    def checkToken(self, char, char_itr, key_itr):
        keyword_list = ['get', 'set', 'do', 'if', 'elif', 'else']
        operators_list = [' ',':', '+', '-', '*', '/', '<<', '=', '!=']
        operators_list.sort()

        scan_list = keyword_list + operators_list

        if key_itr >= len(scan_list):
            return False

        current_lexeme = scan_list[key_itr]

        if char_itr >= len(current_lexeme):
            # Move to the next lexeme
            return False

        if current_lexeme[char_itr] == char:
            return True
        elif key_itr >= len(keyword_list):
            self.delimiter = True
            return True
        else:
            return False

    def tokenize(self, lexeme):
        if lexeme == '\n':
            lexeme = "newline"
        elif lexeme == ' ':
            lexeme = "whitespace"
        print(f'Tokenizing: {lexeme}')