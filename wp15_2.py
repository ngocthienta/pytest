string = input()
rm_val = {'N':0,'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
def roman_numeral_to_int(string) :
    if isinstance(string,str) == False or not string.split() :
        raise TypeError
    for i in string :
        check = [x for x in rm_val]
        if i not in check :
            raise ValueError
    lst = []
    for i in string :
        lst.append(rm_val[i])
    print(lst)
    DLV = [i for i in lst if i in [5,50,500]]

    print(DLV)
    if len(DLV) > 3 :
        raise ValueError
    for i in [5,50,500] :
        ct = DLV.count(i)
        if ct > 1 :
            raise ValueError

    print(lst)

    remaining_num = [i for i in lst if i in [1,10,100]]
    if len(remaining_num) > 27 :
        raise ValueError
    for i in [1,10,100] :
        ct = remaining_num.count(i)
        if ct > 9 :
            raise ValueError
    lst1 = []
    lst.append(0)
    for i in range(len(lst)-1):
        if lst[i] > lst[i-1] and i > 0:
            continue
        else :
            if lst[i] >= lst[i + 1] :
                lst1.append(lst[i])
            else :
                lst1.append(lst[i+1]-lst[i])
    print(lst1)
    sum = val10 = val100 = val1000=0
    for i in lst1 :
        if i < 10 :
            val10 += i
            if val10 >= 10 :
                raise ValueError
        elif i < 100 :
            val100 += i
            if val100 >= 100 :
                raise ValueError
        elif i < 1000 :
            val1000 += i
            if val1000 >= 1000 :
                raise ValueError
        else :
            sum += i
    sum += val10 + val100 + val1000
    return (sum)

print(roman_numeral_to_int(string))























    # for i in lst
    #     if tmp >= i :
    #         tmp = i
    #         sum += i
    #     else :
    #         if tmp = 1 :
    #             if i = 5 or i = 10 :
    #                 tmp = i - tmp
    #                 sum += tmp
    #             else :
    #                 raise ValueError
    #         if tmp = 10 :
    #         if tmp = 100 :
    #

roman_numeral_to_int
