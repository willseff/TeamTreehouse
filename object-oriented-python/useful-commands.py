print(isinstance('a',str))
print(isinstance(4,(bool,int)))

print(issubclass(bool,int))

print(type('sd'))
print('asd'.__class__)
print('ser'.__class__.__name__)

def combiner(list):
    sum_combination=[0,'']
    for item in list:
        if isinstance(item,int):
            sum_combination[0]+=item
        elif isinstance(item,str):
            sum_combination[1]+=item
            
    return (str(sum_combination[1])+str(sum_combination[0]))


list = [2,5,34,5.345,'sefws','fescasdf']

print(combiner(list))