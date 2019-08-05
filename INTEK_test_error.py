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
    if not cond :
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
        digits_list.append(ordaccpt = ('N','I','V','X','L','C','D','M')
    val_accpt =(0,1,5,10,50,100,500,1000)
    sub_notat_usable_int = [1,10,100]

    #check if the string contains invalid characters or D, L, V each appears more than once
    if isinstance(roman_numeral,str) == False :
        raise TypeError('Not a string')
    if c in accpt == False :
        raise ValueError('Not a Roman numeral')
    x = lambda u : roman_numeral.count(u)
    if  x('D') > 1 or x('V') > 1 or x('L') > 1 :
        raise ValueError('Not a Roman numeral')

    #convert each symbol into its integer value. then add them to a list
    lst_rm = list(roman_numeral)
    int_list = []
    for i in lst_rm :
        for c in range(len(accpt)) :
            if i == accpt[c] :
                int_list.append(val_accpt[c])

    #apply Subtractive notation
    new_int_list = []
    t = 0
    while t < (len(int_list) - 1) :
        if int_list[t] >=  int_list[t+1] :
            new_int_list.append(int_list[t])
        elif sub_notat_usable_int.count(int_list[t]) == 0 :
            raise ValueError
        elif int_list[t+1] > 10*int_list[t] :
            raise(ValueError)
        else :
            so = int_list[t+1]-int_list[t]
            new_int_list.append(so)
            del int_list[t+1]
        t += 1
    if t < len(int_list) :
        new_int_list.append(int_list[-1])

    #check if the Roman numeral violates the second rule, then calculate its integer value
    value10 = value100 = value1000 = 0
    total = 0
    for i in range(len(new_introman_numeral = input()
    accpt = ('N','I','V','X','L','C','D','M')
    val_accpt =(0,1,5,10,50,100,500,1000)
    sub_notat_usable_int = [1,10,100]

    #check if the string contains invalid characters or D, L, V each appears more than once
    if isinstance(roman_numeral,str) == False :
        raise TypeError('Not a string')
    if c in accpt == False :
        raise ValueError('Not a Roman numeral')
    x = lambda u : roman_numeral.count(u)
    if  x('D') > 1 or x('V') > 1 or x('L') > 1 :
        raise ValueError('Not a Roman numeral')

    #convert each symbol into its integer value. then add them to a list
    lst_rm = list(roman_numeral)
    int_list = []
    for i in lst_rm :
        for c in range(len(accpt)) :
            if i == accpt[c] :
                int_list.append(val_accpt[c])

    #apply Subtractive notation
    new_int_list = []
    t = 0
    while t < (len(int_list) - 1) :
        if int_list[t] >=  int_list[t+1] :
            new_int_list.append(int_list[t])
        elif sub_notat_usable_int.count(int_list[t]) == 0 :
            raise ValueError
        elif int_list[t+1] > 10*int_list[t] :
            raise(ValueError)
        else :
            so = int_list[t+1]-int_list[t]
            new_int_list.append(so)
            del int_list[t+1]
        t += 1
    if t < len(int_list) :
        new_int_list.append(int_list[-1])_list)):
        if new_int_list[i] < 10 :
            value10 += new_int_list[i]
            if value10 >= 10 :
                raise ValueError
        elif new_int_list[i] < 100 :
            value100 += new_inroman_numeral = input()
    accpt = ('N','I','V','X','L','C','D','M')
    val_accpt =(0,1,5,10,50,100,500,1000)
    sub_notat_usable_int = [1,10,100]

    #check if the string contains invalid characters or D, L, V each appears more than once
    if isinstance(roman_numeral,str) == False :
        raise TypeError('Not a string')
    if c in accpt == False :
        raise ValueError('Not a Roman numeral')
    x = lambda u : roman_numeral.count(u)
    if  x('D') > 1 or x('V') > 1 or x('L') > 1 :
        raise ValueError('Not a Roman numeral')

    #convert each symbol into its integer value. then add them to a list
    lst_rm = list(roman_numeral)
    int_list = []
    for i in lst_rm :
        for c in range(len(accpt)) :
            if i == accpt[c] :
                int_list.append(val_accpt[c])

    #apply Subtractive notation
    new_int_list = []
    t = 0
    while t < (len(int_list) - 1) :
        if int_list[t] >=  int_list[t+1] :
            new_int_list.append(int_list[t])
        elif (sub_notat_usable_int.count(int_list[t]) == 0) or (int_list[t+1] > 10*int_list[t]) :
            raise(ValueError)
        else :
            so = int_list[t+1]-int_list[t]
            new_int_list.append(so)
            del int_list[t+1]
        t += 1
    if t < len(int_list) :
        new_int_list.append(int_list[-1])t_list[i]
            if value100 >= 100 :
                raise ValueError
        elif new_int_list[i] < 1000 :
            value1000 += new_int_list[i]
            if value1000 >= 1000 :
                raise ValueError
        else :
            total += new_int_list[i]
    total += value10 + value100 + value1000
    return (total)
(c)-48)
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
    accpt = ('N','I','V','X','L','C','D','M')
    val_accpt =(0,1,5,10,50,100,500,1000)
    sub_notat_usable_int = [1,10,100]
    if isinstance(roman_numeral,str) == False :
        raise TypeError('Not a string')

    #check if the string contains invalid characters or D, L, V each appears more than once
        if c in accpt == False :
            raise ValueError('Not a Roman numeral')
    x = lambda u : roman_numeral.count(u)
    if  x('D') > 1 or x('V') > 1 or x('L') > 1 :
        raise ValueError('Not a Roman numeral')

    #convert each symbol into its integer value. then add them to a list
    lst_rm = list(roman_numeral)
    int_list = []
    for i in lst_rm :
        for c in range(len(accpt)) :
            if i == accpt[c] :
                int_list.append(val_accpt[c])

    #create a new list containing numbers in descending order
    new_int_list = []
    t = 0
    while t < (len(int_list) - 1) :
        if int_list[t] >=  int_list[t+1] :
            new_int_list.append(int_list[t])
        elif sub_notat_usable_int.count(int_list[t]) == 0 :
            raise ValueError
        elif int_list[t+1] > 10*int_list[t] :
            raise(ValueError)
        else :
            so = int_list[t+1]-int_list[t]
            new_int_list.append(so)
            del int_list[t+1]
        t += 1
    if t < len(int_list) :
        new_int_list.append(int_list[-1])

    #check if the Roman numeral violates the second rule, then calculate its integer value
    value10 = value100 = value1000 = 0
    total = 0
    for i in range(len(new_int_list)):
        if new_int_list[i] < 10 :
            value10 += new_int_list[i]
            if value10 >= 10 :
                raise ValueError
        elif new_int_list[i] < 100 :
            value100 += new_int_list[i]
            if value100 >= 100 :
                raise ValueError
        elif new_int_list[i] < 1000 :
            value1000 += new_int_list[i]
            if value1000 >= 1000 :
                raise ValueError
        else :
            total += new_int_list[i]
    total += value10 + value100 + value1000
    return (total)
