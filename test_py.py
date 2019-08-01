import unittest
import INTEK_test as main

class MyTest(unittest.TestCase):
    def test_waypoint1(self):
        name = '        world             '
        self.assertEqual(main.hello(name),"Hello world!")
    def test_waypoint2(self):
        a = 3
        b = 4
        self.assertEqual(main.calculate_hypotenuse(a,b),5.0)
    def test_waypoint3a(self):
        condition = [True, True, False, True, False, False, True]
        self.assertEqual(main.are_all_conditions_true(condition),False)
    def test_waypoint3b(self):
        condition = [True, True,True]
        self.assertEqual(main.are_all_conditions_true(condition),True)
    def test_waypoint3c(self):
        condition = []
        self.assertEqual(main.are_all_conditions_true(condition),None)
    def test_waypoint4a(self):
        condition = []
        self.assertEqual(main.is_a_condition_true(condition),None)
    def test_waypoint4b(self):
        condition = [False,False,False,False]
        self.assertEqual(main.is_a_condition_true(condition),False)
    def test_waypoint4c(self):
        condition = [False,True,False,False,False,True]
        self.assertEqual(main.is_a_condition_true(condition),True)
    def test_waypoint5a(self):
        l = [0, 3, 5, -2, 9, 8]
        a = 4
        self.assertEqual(main.filter_integers_greater_than(l,a),[5, 9, 8])
    def test_waypoint5b(self):
        l = [0, 3, 5, -2, 9, 8]
        a = 6
        self.assertEqual(main.filter_integers_greater_than(l,a),[9, 8])
    def test_waypoint6a(self):
        hotel_daily_rates = [
            ('Majestic Saigon Hotel', 93),
            ('Hotel Grand Saigon', 80),
            ('Sofitel Saigon Plaza', 123),
            ('Hotel Continental', 62),
            ('Caravelle Hotel', 180),
            ('Sheraton Saigon Hotel', 216),
            ('Park Hyatt Saigon', 209)]
        price = 50
        self.assertEqual(main.find_cheapest_hotels(hotel_daily_rates,price),[])
    def test_waypoint6b(self):
        hotel_daily_rates = [
            ('Majestic Saigon Hotel', 93),
            ('Hotel Grand Saigon', 80),
            ('Sofitel Saigon Plaza', 123),
            ('Hotel Continental', 62),
            ('Caravelle Hotel', 180),
            ('Sheraton Saigon Hotel', 216),
            ('Park Hyatt Saigon', 209)]
        price = 80
        self.assertEqual(main.find_cheapest_hotels(hotel_daily_rates,price),['Hotel Continental', 'Hotel Grand Saigon'])
    def test_waypoint6c(self):
        hotel_daily_rates = [
            ('Majestic Saigon Hotel', 93),
            ('Hotel Grand Saigon', 80),
            ('Sofitel Saigon Plaza', 123),
            ('Hotel Continental', 62),
            ('Caravelle Hotel', 180),
            ('Sheraton Saigon Hotel', 216),
            ('Park Hyatt Saigon', 209)]
        price = 150
        self.assertEqual(main.find_cheapest_hotels(hotel_daily_rates,price),['Hotel Continental', 'Hotel Grand Saigon', 'Majestic Saigon Hotel', 'Sofitel Saigon Plaza'])
    def test_waypoint6d(self):
        hotel_daily_rates = [
            ('Majestic Saigon Hotel', 93.55),
            ('Hotel Grand Saigon', 93.56),
            ('Sofitel Saigon Plaza', 100),
            ('Hotel Continental', 93.55),
            ('Caravelle Hotel', 110),
            ('Sheraton Saigon Hotel', 93),
            ('Park Hyatt Saigon', 120)]
        price = 100
        self.assertEqual(main.find_cheapest_hotels(hotel_daily_rates,price),['Sheraton Saigon Hotel','Majestic Saigon Hotel','Hotel Continental','Hotel Grand Saigon','Sofitel Saigon Plaza'])
    def test_waypoint7(self):
        p1 = (1,1)
        p2 = (2,2)
        self.assertEqual(main.calculate_euclidean_distance_between_2_points(p1,p2),1.4142135623730951)
    def test_waypoint8(self):
        arr = [(0, 0), (3, 4), (-1, -1)]
        self.assertEqual(main.calculate_euclidean_distance_between_points(arr),11.403124237432849)
    def test_waypoint8a(self):
        arr = [(0,0.5),(3.5,4.5),(-2.5,-3.5)]
        self.assertEqual(main.calculate_euclidean_distance_between_points(arr), 15.315072906367325)
    def test_waypoint9(self):
        string = '       khong           co           gi quy hon        doc    lap   tu  do'
        self.assertEqual(main.capitalize_words(string),'Khong Co Gi Quy Hon Doc Lap Tu Do')
    def test_waypoint10a(self):
        string = '1 one two 2 3 three four 4 five six'
        self.assertEqual(main.uppercase_lowercase_words(string),'1 one TWO 2 3 three FOUR 4 FIVE six')
    def test_waypoint10b(self):
        string = '   '
        self.assertEqual(main.uppercase_lowercase_words(string),'')
    def test_waypoint10c(self):
        string = None
        self.assertEqual(main.uppercase_lowercase_words(string),None)
    def test_waypoint11(self):
        n = 5
        self.assertEqual(main.factorial(n),120)
    def test_waypoint12(self):
        char = '9'
        self.assertEqual(main.char_to_int(char),9)
    def test_waypoint13(self):
        string = '17049171'
        self.assertEqual(main.string_to_int(string),17049171)
    def test_waypoint14a(self):
        value = 'madam'
        self.assertEqual(main.is_palindrome(value),True)
    def test_waypoint14b(self):
        value = 'racecar'
        self.assertEqual(main.is_palindrome(value),True)
    def test_waypoint14c(self):
        value = 10801
        self.assertEqual(main.is_palindrome(value),True)
    def test_waypoint14d(self):
        value = 1.947491
        self.assertEqual(main.is_palindrome(value),True)
    def test_waypoint14e(self):
        value = 'Hello, word!'
        self.assertEqual(main.is_palindrome(value),False)
    def test_waypoint14f(self):
        value = 'A man, a plan, a canal, Panama!'
        self.assertEqual(main.is_palindrome(value),True)
    def test_waypoint14g(self):
        value = "No 'x' in Nixon"
        self.assertEqual(main.is_palindrome(value),True)
    def test_waypoint14h(self):
        value = ""
        self.assertEqual(main.is_palindrome(value),False)
    def test_waypoint14i(self):
        value = "   "
        self.assertEqual(main.is_palindrome(value),False)
    def test_waypoint14j(self):
        value = " !!!!@@%$^$%&^**&)([],><!!!  "
        self.assertEqual(main.is_palindrome(value),False)
    def test_waypoint14k(self):
        value = None
        self.assertEqual(main.is_palindrome(value),False)
    def test_waypoint15(self):
        value = 'XXXIX'
        self.assertEqual(main.roman_numeral_to_int(value),39)
    def test_waypoint15a(self):
        value = 'CCXLVI'
        self.assertEqual(main.roman_numeral_to_int(value),246)
    def test_waypoint15b(self):
        value = 'DCCLXXXIX'
        self.assertEqual(main.roman_numeral_to_int(value),789)
    def test_waypoint15c(self):
        value = 'MMCDXXI'
        self.assertEqual(main.roman_numeral_to_int(value),2421)
    def test_waypoint15d(self):
        value = 'CLX'
        self.assertEqual(main.roman_numeral_to_int(value),160)
    def test_waypoint15e(self):
        value = 'CCVII'
        self.assertEqual(main.roman_numeral_to_int(value),207)
    def test_waypoint15f(self):
        value = 'MIX'
        self.assertEqual(main.roman_numeral_to_int(value),1009)
    def test_waypoint15g(self):
        value = 'MLXVI'
        self.assertEqual(main.roman_numeral_to_int(value),1066)
    def test_waypoint15h(self):
        value = 'MDCCLXXVI'
        self.assertEqual(main.roman_numeral_to_int(value),1776)
    def test_waypoint15j(self):
        value = 'MCMLIV'
        self.assertEqual(main.roman_numeral_to_int(value),1954)
    def test_waypoint15h(self):
        value = 'MMXIV'
        self.assertEqual(main.roman_numeral_to_int(value),2014)
    def test_waypoint15i(self):
        value = 'MMMCMXCIX'
        self.assertEqual(main.roman_numeral_to_int(value),3999)
#     def test_waypoint16(self):
#         MELODY_HAPPY_BIRTHDAY_TO_YOU = (
#             'C4', 'C4', 'D4', 'C4', 'F4', 'E4',
#             'C4', 'C4', 'D4', 'C4', 'G4', 'F4',
#             'C4', 'C4', 'C5', 'A4', 'F4', 'E4', 'D4',
#             'A#4', 'A#4', 'A4', 'F4', 'G4', 'F4',
#         )
#         addres = './sounds/piano'
#         self.assertEqual(main.play_melody(MELODY_HAPPY_BIRTHDAY_TO_YOU,addres),['./sounds/piano/c4.ogg', './sounds/piano/c4.ogg', './sounds/piano/d4.ogg', './sounds/piano/c4.ogg', './sounds/piano/f4.ogg', './sounds/piano/e4.ogg', './sounds/piano/c4.ogg', './sounds/piano/c4.ogg', './sounds/piano/d4.ogg', './sounds/piano/c4.ogg', './sounds/piano/g4.ogg', './sounds/piano/f4.ogg', './sounds/piano/c4.ogg', './sounds/piano/c4.ogg', './sounds/piano/c5.ogg', './sounds/piano/a4.ogg', './sounds/piano/f4.ogg', './sounds/piano/e4.ogg', './sounds/piano/d4.ogg', './sounds/piano/bb4.ogg', './sounds/piano/bb4.ogg', './sounds/piano/a4.ogg', './sounds/piano/f4.ogg', './sounds/piano/g4.ogg', './sounds/piano/f4.ogg']
# )
