import math
import string
rm_val = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


def hello(n):
    if not isinstance(n, str):
        raise TypeError('A string is expected')
    if n.strip:
        raise ValueError
    else:
        result = "Hello {}!".format(n)
    return result


def calculate_hypotenuse(a, b):
    result = math.sqrt(a * a + b * b)
    return result


def are_all_conditions_true(cond):
    if not cond:
        result = None
    else:
        if False in cond:
            result = False
        else:
            result = True
    return result


def is_a_condition_true(cond):
    if not cond:
        result = None
    else:
        if True in cond:
            result = True
        else:
            result = False
    return result


def filter_integers_greater_than(l, n):
    lst = []
    for i in l:
        if i > n:
            lst.append(i)
    return lst


def find_cheapest_hotels(hotel_daily_rates, maximum_daily_rate):
    aff_hotels = []
    # find the suitable hotels
    for i in hotel_daily_rates:
        if maximum_daily_rate >= i[1]:
            aff_hotels.append(i)
    # sort them in ascending order
    aff_hotels = sorted(aff_hotels, key=lambda u: u[1])
    # remove the prices
    aff_hotels_names = []
    for i in aff_hotels:
        aff_hotels_names.append(i[0])
    return aff_hotels_names


def calculate_euclidean_distance_between_2_points(p1, p2):
    euclid_dis = math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))
    return euclid_dis


def calculate_euclidean_distance_between_points(points):
    if isinstance(points, type(None)) or len(points) < 2:
        raise ValueError("The list MUST contain at least 2 points")
    x_coors, y_coors = [], []
    for i in points:
        x_coors.append(i[0])
        y_coors.append(i[1])
    total_dis = 0
    for i in range(len(x_coors) - 1):
        total_dis += math.sqrt((x_coors[i] - x_coors[i + 1]) ** 2 + (y_coors[i] - y_coors[i + 1]) ** 2)
    return total_dis


def capitalize_words(s):
    if s is None:
        return None
    if not isinstance(s, str):
        raise TypeError('Not a string')
    else:
        # remove unnecessary white spaces
        s = s.split()
        news = " ".join(s)
        # return
        return news.title()


def uppercase_lowercase_words(s):
    if s is None:
        return None
    if not isinstance(s, str) :
        raise TypeError('Not a string')
    else:
        # take out the words
        s = s.split()
        news = ""
        # process the words based on indexing and combine them into a new string
        for i in range(len(s)):
            if i % 2 == 0:
                news += s[i].upper() + " "
            else:
                news += s[i].lower() + " "
        return news.strip()


def factorial(n):
    if not isinstance(n, int):
        raise TypeError('Not an integer')
    if n < 0:
        raise ValueError('Not a positive integer')
    fact = 1
    for i in range(n):
        fact *= (i + 1)
    return fact


def char_to_int(c):
    if not isinstance(c, str):
        raise TypeError('Not a string')
    if len(c) != 1 or ord(c) < 48 or ord(c) > 57:
        raise ValueError('Not a single digit')
    # V1
    # for i in range(10):
    #     if ord(str(i)) == ord(c):
    #         return (i)
    # V2
    num = ord(c) - 48
    return num


def string_to_int(s):
    if not isinstance(s, str):
        raise TypeError('Not a string')
    for i in s:
        if ord(i) < 48 or ord(i) > 57:
            raise ValueError('Not a positive integer string expression')
    digits_list = []
    for c in s:
        digits_list.append(ord(c) - 48)
    num = 0
    for i in range(len(digits_list)):
        num += digits_list[i] * (10 ** (len(digits_list) - i - 1))
    return num


def is_palindrome(value):
    new = str(value).replace(' ', '').lower()
    for c in new:
        check1 = c in string.ascii_letters
        check2 = c in string.digits
        if not check1 and not check2:
            new = new.replace(c, '')
    if new == '':
        result = False
    else:
        t = 1
        result = True
        times_to_run = len(new) // 2
        for i in range(times_to_run):
            if new[i] != new[i - t]:
                result = False
                break
            t += 2
    return result


def roman_numeral_to_int(roman_numerals):
    if roman_numerals is 'N':
        total_val = 0
    else:
        if not isinstance(roman_numerals, str) or not roman_numerals.split():
            raise TypeError
        for i in roman_numerals:
            check = [x for x in rm_val]
            if i not in check:
                raise ValueError
        lst = []
        for i in roman_numerals:
            lst.append(rm_val[i])
        dlv = [i for i in lst if i in [5, 50, 500]]
        if len(dlv) > 3:
            raise ValueError
        for i in [5, 50, 500]:
            ct = dlv.count(i)
            if ct > 1:
                raise ValueError
        lst.append(0)
        new_lst = []
        i = 0
        while i < len(lst) - 1:
            if lst[i] >= lst[i + 1]:
                new_lst.append(lst[i])
                i += 1
            else:
                if lst[i] in [5, 50, 500]:
                    raise ValueError
                elif lst[i + 1] > 10 * lst[i]:
                    raise ValueError
                else:
                    new_lst.append(lst[i + 1] - lst[i])
                    i += 2
        if not sorted(new_lst, reverse=True) == new_lst:
            raise ValueError
        total_val = val10 = val100 = val1000 = 0
        for i in new_lst:
            if i < 10:
                val10 += i
                if val10 >= 10:
                    raise ValueError
            elif i < 100:
                val100 += i
                if val100 >= 100:
                    raise ValueError
            elif i < 1000:
                val1000 += i
                if val1000 >= 1000:
                    raise ValueError
            else:
                total_val += i
        total_val += val10 + val100 + val1000
    return total_val
