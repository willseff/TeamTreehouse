class Letter:
    def __init__(self, pattern=None):
        self.pattern = pattern
    
    def __str__(self):
        string = ''
        for symbol in self.pattern:
            if (symbol == '-'):
                string += 'dash-'
            else:
                string += 'dot-'
        string = string[:-1]
        return string
    

class S(Letter):
    def __init__(self):
        pattern = ['.', '.', '.']
        super().__init__(pattern)


print(S())

print(len(str(S())))