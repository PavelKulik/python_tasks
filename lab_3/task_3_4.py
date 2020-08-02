string = input('Input the string: ')
index = len(string) // 2
print(f'center symbol: {string[index]}')
if string[0] == string[index]:
    print(string[1:-1])
else:
    print('symbols unequal')
