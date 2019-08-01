import math
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
        result = True
        for i in cond :
            if i == False :
                result = False
                break
    return (result)

def is_a_condition_true(cond) :
    if cond == [] :
        result = None
    else :
        result = False
        for i in cond :
            if i == True :
                result = True
                break
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
