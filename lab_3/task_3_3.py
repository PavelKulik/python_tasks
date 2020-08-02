string = input('Input the string: ')
if len(string) > 10:
    new_string = string + '!!!'
    print(new_string)
elif 1 < len(string) < 10:
    print(string[1])
else:
    print('error')
