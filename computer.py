from number_guessing import Number_guessing

class Computer:
    def __init__(self,to_guess):
        self.game = Number_guessing(to_guess)
        self.number = ['0','0','0','0']
        self.digit = 0
        self.results = '0'
        self.prevResults = '0'

    def play(self):
        if self.results[0] > self.prevResults[0]:
            self.digit += 1
        elif self.results[0] < self.prevResults[0]:
            self.number[self.digit] = str(int(self.number[self.digit]) - 1)
            self.digit += 1
        try:
            self.number[self.digit] = str(int(self.number[self.digit]) + 1)
        except:
            pass
        self.prevResults = self.results
        self.results = self.get_results()       

    def get_results(self):
        word = "".join(self.number)
        self.game.compare(word)
        return self.game.get_G() + self.game.get_R()

    def getNumber(self):
        word = "".join(self.number)
        return word