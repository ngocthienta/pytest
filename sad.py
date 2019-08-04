import math
import string
import pygame
pygame.init()
notes = ['a','b','c','d','e','f','g']
octaves = ['2','3','4','5']
conv = {'c#':'db','d#':'eb','f#':'gb','g#':'ab','a#':'bb'}
rm_val = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


def hello(name):
    """Prints a hello.

    Takes one argument name

    Args:
        name: A string
    Returns:
        A string composed of 'Hello ' concatenated with the argument name(rid
        of leading and trailing whitespace characters) and
        concatenated with the character '!'.
    Raises :
        TypeError: name is not a string.
    """
    if not isinstance(name, str):
        raise TypeError('A string is expected')
    if not name.strip():
        raise ValueError
    else:
        result = "Hello {}!".format(name.strip())
    return result


def calculate_hypotenuse(a, b):
    """Returns the length of the hypotenuse of a right triangle.

    Takes two arguments a and b (integers or floats) representing the
    length of the two sides of a right triangle.

    Args:
        a, b: An integer or a real number.
    Raises:
        TypeError: Either a or b doesn't belong to the types mentioned above.
    """
    x = lambda u : isinstance(u,int)
    y = lambda u : isinstance(u,float)
    if (not x(a) and not y(a)) or (not x(b) and not y(b)):
        raise TypeError('Length of the sides of a triangle must be a real number')
    if not a > 0 or not b > 0:
        raise ValueError('Length of the sides of a triangle must be greater than 0')
    result = math.sqrt(a * a + b * b)
    return result


def are_all_conditions_true(cond):
    """Checks whether all Conditions are True.

    Args:
        cond: A list contains booleans or an empty list.
    Returns:
        True, False or None.
    Raises:
        TypeError
        ValueError
    """
    if not cond:
        return None
    if not isinstance(cond,list):
        raise TypeError('A list is expected')
    for i in cond:
        if not isinstance(i,bool):
            raise ValueError('The list must contain either booleans or nothing at all')
    else:
        if False in cond:
            result = False
        else:
            result = True
    return result


def is_a_condition_true(cond):
    """Checks whether at least one Condition is True.

    Args:
        cond: A list contains booleans or an empty list.
    Returns:
        True, False or None.
    Raises:
        TypeError
        ValueError
    """
    if not isinstance(cond,list):
        raise TypeError('A list is expected')
    for i in cond:
        if not isinstance(i,bool):
            raise ValueError('The list must contain either booleans or nothing at all')
    if not cond:
        result = None
    else:
        if True in cond:
            result = True
        else:
            result = False
    return result


def filter_integers_greater_than(l, n):
    """Filters list of integers.

    Args:
        l : A list of integers.
        n : An integer.
    Returns:
        A new list containing integers greater than n.
    Raises:
        TypeError
        ValueError
    """
    if not isinstance(l,list):
        raise TypeError('A list is expected')
    if not isinstance(n,int):
        raise TypeError('An integer is expected')
    for i in l:
        if not isinstance(i,int):
            raise ValueError('The list must contain only integers')
    lst = []
    for i in l:
        if i > n:
            lst.append(i)
    return lst


def find_cheapest_hotels(hotel_daily_rates, maximum_daily_rate):
    """Finds cheapest hotels.

    Args:
        hotel_daily_rates: A list of hotels and their respective daily rate
                           represented by tuples.
        maximum_daily_rate: an integer or a float representing the maximum daily
                            rate the user is willing to pay for one day at an hotel.
    Returns:
        An list of affordable hotels sorted by the ascending daily rate.
    Raises:
        TypeError
        ValueError
    """
    if not isinstance(maximum_daily_rate,int) and not isinstance(maximum_daily_rate,float):
        raise TypeError('An integer or a float is expected')
    if not isinstance(hotel_daily_rates,list):
        raise TypeError('A list is expected')
    for i in hotel_daily_rates:
        if not isinstance(i,tuple):
            raise ValueError('The list must contain only tuples')
        if len(i) != 2:
            raise ValueError('Tuples must only contain 2 objects')
        if not isinstance(i[0],str) or (not isinstance(i[1],int) and not isinstance(i[1],float)):
            raise ValueError("Tuples' objects are invalid")
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
    """Calculates Distance between two 2D Points.

    Args:
        p1, p2: A tuple of 2 integers or floats.
    Raises:
        TypeError
        ValueError
    """
    if not isinstance(p1,tuple) or not isinstance(p2,tuple):
        raise TypeError('A tuple is expected')
    for i in range(len(p1)):
        if not isinstance(p1[i],int) and not isinstance(p1[i],float):
            raise ValueError('Coordinates must be real numbers')
        if not isinstance(p2[i],int) and not isinstance(p2[i],float):
            raise ValueError('Coordinates must be real numbers')
    euclid_dis = math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))
    return euclid_dis


def calculate_euclidean_distance_between_points(points):
    """Calculates Distance between several 2D Points

    Args:
        points: A list of points in x-y plane coordinate.
    Returns:
        The sum of the Euclidean distance between each consecutive
        points in the list.
    Raises:
        TypeError
        ValueError
    """
    if not isinstance(points,list):
        raise TypeError('Not a list')
    if len(points) < 2:
        raise ValueError("The list MUST contain at least 2 points")
    total_dis = 0
    for i in zip(points,points[1:]):
        total_dis += calculate_euclidean_distance_between_2_points(i[0],i[1])
    return total_dis


def capitalize_words(s):
    """Returns a copy of the string with all the words capitalized.

    This function sets the first character in each word of the string 's'
    to uppercase and the rest to lowercase.

    The function removes any duplicate whitespace characters between
    words.

    If 'None' is passed, the function returns 'None'.

    Args:
        s : A string that possibly contains words separated by whitespace
        characters.
    Raises:
        TypeError:  If the argument 's' is not a string.
    """
    if not isinstance(s, str):
        raise TypeError('Not a string')
    if s is None:
        return None
    else:
        # remove unnecessary white spaces
        s = s.split()
        news = " ".join(s).strip()
        # return
        return news.title()


def uppercase_lowercase_words(s):
    """Converts words to uppercase or lowercase

    Words at even position are converted to uppercase.
    Words at odd position are converted to lowercase.

    Args:
        s : A string
    Return:
        A copy of the string 's' with the words converted to uppercase
        or lowercase depending on their position in the string.
    Raises:
        ValueError: If the argument 's' is not a string.
    """
    if not s:
        return None
    if not isinstance(s, str) :
        raise TypeError('Not a string')
    else:
        # take out the words
        s = s.split()
        news = ""
        # process the words based on indexing and combine them into a new string
        # V1 :
        # for i in range(len(s)):
        #     if i % 2 == 0:
        #         news += s[i].upper() + " "
        #     else:
        #         news += s[i].lower() + " "
        for i in range(len(s)):
            if i % 2 == 0:
                s[i] = s[i].upper()
            else:
                s[i] = s[i].lower()
        return " ".join(s).strip()


def factorial(n):
    """Returns the factorial of an integer.

    Args:
        n : An integer.
    Raises:
        TypeError
        ValueError
    """
    if not isinstance(n, int):
        raise TypeError('Not an integer')
    if n < 0:
        raise ValueError('Not a positive integer')
    fact = 1
    for i in range(n):
        fact *= (i + 1)
    return fact


def char_to_int(c):
    """Returns an integer representing the numerical value of the character.

    Args:
        c : A string containing digit characters.
    Raises:
        TypeError: If the argument 'c' is not a string.
        ValueError: If the argument 'c' is a string but it does not only contain
                    1 character or this character is not a digit.
    """
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
    """Converts a string of digit characters to a number.

    Args:
        s: A string of digit characters.
    Returns:
        Return an integer representing the numerical value of the string.
    Raises:
        TypeError: If the argument 's' is not a string.
        ValueError: If the argument s is a string but it does not only contain
                    digit characters.
    """
    if not isinstance(s, str):
        raise TypeError('Not a string')
    digits_list = []
    for i in s:
        digits_list.append(char_to_int(i))
    num = 0
    for i in range(len(digits_list)):
        num += digits_list[i] * (10 ** (len(digits_list) - i - 1))
    return num


def is_palindrome(value):
    """Checks Palindrome string.

    Takes an argument value of any type and that returns True is the string
    representation of this value is a palindrome or False otherwise.

    The function only retains ASCII letter characters and digits.
    It ignores any other characters.

    The function is not case-sensitive, i.e, uppercase and lowercase
    characters are treated as equivalent.

    Args:
        value: Anything.
    Returns:
        True or False.
    """
    new = str(value).replace(' ', '').lower()
    for c in new:
        check1 = c in string.ascii_letters
        check2 = c in string.digits
        if not check1 and not check2:
            new = new.replace(c, '')
    if not new:
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
    """Returns the Numerical Value of a Roman Numeral.

    Args:
        roman_numerals: A string of a Roman Numeral.
    Raises:
        TypeError: If the argument 'roman_numeral' is not a string.
        ValueError: if the argument 'roman_numeral' is an empty string or
                    some characters of the string roman_numeral don't
                    represent Roman numeral symbols.
    """
    if not roman_numerals:
        raise TypeError('Not a string')
    if not isinstance(roman_numerals, str):
        raise TypeError('Not a string')
    if not roman_numerals.split():
        raise ValueError('Not an empty string')
    for i in roman_numerals:
        check = [x for x in rm_val]
        if i not in check:
            raise ValueError('Invalid characters')
    lst = []
    for i in roman_numerals:
        lst.append(rm_val[i])
    dlv = [i for i in lst if i in [5, 50, 500]]
    if len(dlv) > 3:
        raise ValueError('D,L,V must each appear once only')
    for i in [5, 50, 500]:
        ct = dlv.count(i)
        if ct > 1:
            raise ValueError('D,L,V must each appear once only')
    lst.append(0)
    new_lst = []
    i = 0
    while i < len(lst) - 1:
        if lst[i] >= lst[i + 1]:
            new_lst.append(lst[i])
            i += 1
        else:
            if lst[i] in [5, 50, 500]:
                raise ValueError('D,L,V cannot be written in the left of a larger denomination')
            elif lst[i + 1] > 10 * lst[i]:
                raise ValueError('A denomination cannot be written in the left of another denomination which is over 10 times larger')
            else:
                new_lst.append(lst[i + 1] - lst[i])
                i += 2
    if not sorted(new_lst, reverse=True) == new_lst:
        raise ValueError('The numerals are not written in descending order of value')
    total_val = val10 = val100 = val1000 = 0
    for i in new_lst:
        if i < 10:
            val10 += i
            if val10 >= 10:
                raise ValueError('X cannot be equalled or exceeded by smaller denominations')
        elif i < 100:
            val100 += i
            if val100 >= 100:
                raise ValueError('C cannot be equalled or exceeded by smaller denominations')
        elif i < 1000:
            val1000 += i
            if val1000 >= 1000:
                raise ValueError('M cannot be equalled or exceeded by smaller denominations')
        else:
            total_val += i
    total_val += val10 + val100 + val1000
    if total_val > 3999:
	       raise ValueError('The largest number that can be represented in this notation is 3,999')
    return total_val

def play_melody(melody, sound_basedir):
    """Plays a melody.

    The function replaces accidental sharp (♯) notes with the equivalent
    accidental flat (♭) notes.

    Args:
        melody: A collection (iterable) of notes, named after the
                international pitch notation.
        sound_basedir: A string representing the path of the directory
                       containing the note sound files.
    Returns:
        A list of the file pathname of the notes that have been played
        one after the other.
    Raises:
        TypeError : If the melody is not a list or is an empty list.
        ValueError
    """
    if not isinstance(melody,list) or not melody:
        raise TypeError('Not a list')
    for i in melody:
        if not isinstance(i,str):
            raise ValueError('Note should be a string')
    new_mel = []
    for i in melody:
        new_mel.append(i.lower())
    for i in range(len(new_mel)):
        if len(new_mel[i]) < 2 or len(new_mel[i]) > 3:
            raise ValueError
        if not new_mel[i][0] in notes or not new_mel[i][-1] in octaves:
            raise ValueError('Your note(s) do not exist')
        for j in ['e#','b#','cb','fb']:
            if j in new_mel[i]:
                raise ValueError('Your note(s) do not exist')
        if new_mel[i][0:2] in conv:
            print(new_mel[i][0:2])
            new_mel[i] = new_mel[i].replace(new_mel[i][0:2],conv[new_mel[i][0:2]])
    lst = []
    for i in new_mel:
        lst.append('{}/{}.ogg'.format(sound_basedir,i))
        sound = pygame.mixer.Sound('{}/{}.ogg'.format(sound_basedir,i))
        sound.play()
        pygame.time.delay(550)
        pygame.mixer.stop()
    return lst
