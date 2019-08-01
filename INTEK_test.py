import math
import string
def hello(n) :
    if isinstance(n, str) == False:
        raise ValueError('A string is expected')
    n = n.strip()
    result = "Hello {}!".format(n)
    return (result)

def calculate_hypotenuse(a, b) :
    result = math.sqrt(a*a + b*b)
    return (result)

def are_all_conditions_true(cond) :
    if cond == [] :
        result = None
    else :
        if False in cond :
            result = False
        else :
            result = True
    return (result)

def is_a_condition_true(cond) :
    if cond == [] :
        result = None
    else :
        if True in cond :
            result = True
        else :
            result = False
    return (result)

def filter_integers_greater_than(l, n) :
    lst = []
    for i in l :
        if i > n :
            lst.append(i)
    return (lst)

def find_cheapest_hotels(hotel_daily_rates,maximum_daily_rate) :
    aff_hotels = []
    #find the suitable hotels
    for i in hotel_daily_rates :
        if maximum_daily_rate >= i[1] :
            aff_hotels.append(i)
    #sort them by the ascending
    aff_hotels = sorted(aff_hotels, key=lambda i: i[1])
    #remove the prices
    aff_hotels_names = []
    for i in aff_hotels :
        aff_hotels_names.append(i[0])
    return (aff_hotels_names)

def calculate_euclidean_distance_between_2_points(p1, p2) :
    euclid_dis = math.sqrt(((p1[0]-p2[0])**2) + ((p1[1]-p2[1])**2))
    return (euclid_dis)

def calculate_euclidean_distance_between_points(points):
    if type(points) == type(None) or len(points) < 2 :
        raise ValueError("The list MUST contain at least 2 points")
    import math
    x_coors, y_coors = [], []
    for i in points :
        x_coors.append(i[0])
        y_coors.append(i[1])
    total_dis = 0
    for i in range(len(x_coors)-1) :
        total_dis += math.sqrt((x_coors[i]-x_coors[i+1])**2 + (y_coors[i]-y_coors[i+1])**2)
    return (total_dis)

def capitalize_words(s):
    if s == None :
        return(None)
    if isinstance(s, str) == False:
        raise TypeError('Not a string')
    else :
        #remove unnecessary white spaces
        s = s.split()
        news = " ".join(s)
        #return
        return (news.title())

def uppercase_lowercase_words(s) :
    if s == None :
        return None
    if isinstance(s, str) == False:
        raise TypeError('Not a string')
    else :
        #take out the words
        s = s.split()
        news = ""
        #process the words based on indexing and combine them into a new string
        for i in range(len(s)) :
            if i % 2 == 0 :
                news += s[i].upper() + " "
            else :
                news += s[i].lower() + " "
        return (news.strip())

def factorial(n) :
    if isinstance(n, int) == False :
        raise TypeError('Not an integer')
    if n < 0 :
        raise ValueError('Not a positive integer')
    fact = 1
    for i in range(n) :
            fact *= (i+1)
    return (fact)

def char_to_int(c) :
    if isinstance(c,str) == False :
        raise TypeError('Not a string')
    if len(c) != 1 or ord(c) < 48 or ord(c) > 57 :
        raise ValueError('Not a single digit')
    #V1
    # for i in range(10) :
    #     if ord(str(i)) == ord(c) :
    #         return (i)
    #V2
    num = ord(c) - 48
    return num

def string_to_int(s) :
    if isinstance(s,str) == False :
        raise TypeError('Not a string')
    for i in s :
        if ord(i) < 48 or ord(i) > 57 :
            raise ValueError('Not a positive integer string expression')
    digits_list = []
    for c in s :
        digits_list.append(ord(c)-48)
    num = 0
    for i in range(len(digits_list)) :
        num += digits_list[i]*(10**(len(digits_list)-i-1))
    return (num)

def is_palindrome(value) :
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
    return (T_or_F)

def roman_numeral_to_int(roman_numeral) :
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
    return (val)
