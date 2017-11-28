print('Please input a number, string or list')
data = input()
if type(data) is int and data >=100:
    print('That is a big number!')
elif type(data) is int and data <100:
    print('That is a small number')
elif type(data) is str and len(data) >=50: 
    print('Long Sentence')
elif type(data) is str and len(data) <50:
    print('Short Sentence')
elif type(data) is list and len(data) >=10: 
    print('Big List!')
else:
    print('Short List')
