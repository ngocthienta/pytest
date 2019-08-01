s = "1235"
if isinstance(s,str) == False :
    raise TypeError('Not a string')
for i in s :
    if ord(i) < 48 or ord(i) > 57 :
        raise ValueError('Not a positive integer string expression')
digits_list = []
for c in s :
    for i in range(10) :
        if ord(str(i)) == ord(c) :
            digits_list.append(i)
num = 0
for i in range(len(digits_list)) :
    num += digits_list[i]*(10**(len(digits_list)-i-1))
print(num)
