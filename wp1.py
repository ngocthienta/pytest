def hello(n) :
    n = n.strip()
    result = "Hello {}!".format(n)
    return print(result);

def calculate_hypotenuse(a, b) :
    import math
    result = math.sqrt(a*a + b*b)
    return print(result);

def are_all_conditions_true(cond) :
    if cond == [] :
        result = None
    else :
        result = True
        for i in cond :
            if i == False :
                result = False
                break
    return print(result);

def is_a_condition_true(cond) :
    if cond == [] :
        result = None
    else :
        result = False
        for i in cond :
            if i == True :
                result = True
                break
    return print(result);

def filter_integers_greater_than(l, n) 
    lst = []
    for i in l :
        if i > n :
            lst.append(i)
    return print(lst);
l = [1,2,3,4,5,6,7,8,9,10]
n = 4
filter_integers_greater_than(l, n)
