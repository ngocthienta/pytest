import string
c = input()
if isinstance(c,str) == False :
    raise TypeError('Not a string')
if len(c) != 1 or ord(c) < 48 or ord(c) > 57 :
    raise ValueError('Not a single digit')
for i in string.digits :
    if ord(i) == ord(c) :
        print(i)
        break
