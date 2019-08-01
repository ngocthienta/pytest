lst = [78,73,88,86,76,67,68,77]
if isinstance(roman_numeral,str) == False :
    raise TypeError('Not a string')
order = 0
count = 0
for c in roman_numeral :
    check = ord(c) in lst
    if check == False :
        raise ValueError('Not a Roman numeral')
    if ord(c) != order :
        order = ord(c)
        count = 0
    else :
        count += 1
    if count == 3 :
        raise ValueError('Not a Roman numeral')
lst_rm = list(roman_numeral)
int_list = []
rm = (('I',1),('V',5),('X',10),('L',50),('C',100),('D',500),('M',1000))
for i in lst_rm :
    for c in rm :
        if i == c[0] :
            int_list.append(c[1])
val = 0
t = 0
while t <= len(int_list) - 1 :
    if t == len(int_list) - 1 :
        val += int_list[t]
        break
    if int_list[t] >= int_list[t+1] :
        val += int_list[t]
        t += 1
    else :
        val += int_list[t+1]-int_list[t]
        t += 2
print(val)
