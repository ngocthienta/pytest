rm_num = list(input())
integer_list = []
rm = (('I',1),('V',5),('X',10),('L',50),('C',100),('D',500),('M',1000))
for i in rm_num :
    for c in rm :
        if i == c[0] :
            integer_list.append(c[1])
print(integer_list)
integ = 0
t = 0
while t <= len(integer_list) - 1 :
    if t == len(integer_list) - 1 :
        integ += integer_list[t]
        break
    if integer_list[t] >= integer_list[t+1] :
        integ += integer_list[t]
        t += 1
    else :
        integ += integer_list[t+1]-integer_list[t]
        t += 2
    print(integ)
print(integ)
