class Number_guessing:
    def __init__(self, to_guess = '1234'):
        self.to_guess = to_guess
        self.G = 0
        self.R_dict = {}
        self.R = 0
        self.tries = 0
        

    def compare(self, number):
        self.tries += 1
        self.reset_results()
        if self.check_index(number):
            return "Solo se aceptan 4 digitos"        
        for idx, digit in enumerate(number):
            if self.to_guess[idx] == digit:
                self.G += 1
            else:
                if self.to_guess[idx] in number:
                    self.R_dict[digit] = 1

        return self.get_result()
    
    def check_index(self,number):
        if len(number) == 4:
            return False
        else:
            return True
    def reset_results(self):
        self.G = 0
        self.R_dict = {}
        self.R = 0

    def get_R(self):
        for key in self.R_dict:
            self.R = self.R + self.R_dict[key]
        if self.R == 0:
            return ''
        else:
            return str(self.R) + 'R'

    def get_G(self):
        if self.G == 0:
            return ''
        else:
            
            return str(self.G) + 'G '

    def get_result(self):
        if self.G == 0 and self.R == 0:
            return "Sin coincidencias"
        result = self.get_G() + self.get_R()
        return result

    def check_win(self):
        if self.G == 4:
            return False
        return True

    def get_tries(self):
        return self.tries