class YourLexicalAnalyzer:
    keyword_list = ['get', 'set', 'do', 'if', 'elif', 'else']
    operators_list = [' ', '+', '-', '*', '/', '<<', '=', '!=']
    operators_list.sort()

    def __init__(self, file_path):
        self.file_path = file_path
        self.delimiter = False

    def scanFile(self):
        try:
            with open(self.file_path, 'r') as file:
                for line_number, line in enumerate(file, start=1):
                    char_itr = 0
                    keyword_itr = 0
                    concat_text = ""

                    while char_itr < len(line):
                        char = line[char_itr]
                        isValid = self.checkToken(char, char_itr, keyword_itr)

                        while not isValid:
                            keyword_itr += 1
                            if keyword_itr >= len(self.keyword_list) + len(self.operators_list):
                                # Restart the entire file scan
                                char_itr = -1
                                keyword_itr = 0
                                break
                            isValid = self.checkToken(char, char_itr, keyword_itr)

                        if self.delimiter and isValid:
                            self.tokenize(concat_text)
                            self.delimiter = False
                            char_itr = -1
                            keyword_itr = 0

                        char_itr += 1

        except IOError as e:
            print(e)

    def checkToken(self, char, char_itr, key_itr):
        scan_list = self.keyword_list + self.operators_list

        if key_itr >= len(scan_list):
            return False

        current_lexeme = scan_list[key_itr]

        if char_itr >= len(current_lexeme):
            # Move to the next lexeme
            return False

        if current_lexeme[char_itr] == char:
            return True
        else:
            # Restart the entire file scan
            return False

    def tokenize(self, lexeme):
        
        print(f'Tokenizing: {lexeme}')

                    

                    
                            
                    
                        

                    
                    

    #def isValid(char, char_itr, key_itr, scan_list, concat_text):

     #   if char_itr + 1  > len(scan_list[key_itr]): 

      #      return False
        

       # if scan_list[key_itr] == concat_text: 

        #    return True 
        
       # else: 
        #    return False
        
        



        
    



                    
                    

