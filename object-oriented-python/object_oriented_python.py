class Liar(list):
    
    def __len__(self):
        return super().__len__()-1

liar_list = Liar([1,2,3,3])

print(len(liar_list))


class Letter:
    def __init__(self, pattern=None):
        self.pattern = pattern
      
    def __iter__(self):
        yield from self.pattern
      
    def __str__(self):
        output = []
        for blip in self:
            if blip == '.':
                output.append('dot')
            else:
                output.append('dash')
        return '-'.join(output)

    @classmethod
    def from_string(cls,string):
        pattern = string.split('-')
        output=[]
        for character in pattern:
        	if (character == 'dot'):
        		output.append('.')
        	else:
        		output.append('_')
        return cls(output)
    

class S(Letter):
    def __init__(self):
         pattern = ['.', '.', '.']
         super().__init__(pattern)


print(Letter.from_string('dot-dash-dot-dot').pattern)