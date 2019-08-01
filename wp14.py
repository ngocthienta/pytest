import(string)
new = str(value).replace(' ','').lower()
for c in new :
    check1 = c in string.ascii_letters
    check2 = c in string.digits
    if check1 == False and check2 == False:
        new = new.replace(c,'')
if new == '' :
    T_or_F = False
else :
    t = 1
    T_or_F = True
    times_to_run = len(new)//2
    for i in range(times_to_run) :
        if new[i] != new[i-t] :
            T_or_F = False
            break
        t += 2
print (T_or_F)
