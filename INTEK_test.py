def hello(n) :
    if not isinstance(n, str) :
        raise ValueError('A string is expected')
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

def filter_integers_greater_than(l, n) :
    lst = []
    for i in l :
        if i > n :
            lst.append(i)
    return print(lst);

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
    return print(aff_hotels_names);

def calculate_euclidean_distance_between_2_points(p1, p2)
    import math
    euclid_dis = math.sqrt(((p1[0]-p2[0])**2) + ((p1[1]-p2[1])**2))
    return print(euclid_dis);

def capitalize_words(s):
    if not isinstance(s, str) :
        raise TypeError('Not a string')
    if s == None :
        print(None)
    else :
        #remove unnecessary white spaces
        s = s.split()
        news = " ".join(s)
        #print
        return print(news.title());

def uppercase_lowercase_words(s) :
    if not isinstance(s, str) :
        raise TypeError('Not a string')
    if s == None :
        print(None)
    else :
        #take out the words        raise TypeError('Not a string')

        s = s.split()
        news = ""
        #process the words based on indexing and combine them into a new string
        for i in range(len(s)) :
            if i % 2 == 0 :
                news += s[i].upper() + " "
            else :
                news += s[i].lower() + " "
        return print(news);

def factorial(n) :
    if not isinstance(n, int) :
        raise TypeError('Not an integer')
    if n < 0 :
        raise ValueError('Not a positive integer')
    fact = 1
    for i in range(n) :
            fact *= (i+1)
    return print(fact);
