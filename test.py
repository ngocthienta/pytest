def hello(n) :
    if not isinstance(n, str) or len(n.split()) == 0 :
        raise ValueError('A non-empty string is expected')
    n = n.strip()
    result = "Hello {}!".format(n)
    return print(result)
n = 849846132
hello(n)
