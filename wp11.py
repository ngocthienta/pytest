n = 1
if not isinstance(n, int) :
    raise TypeError('Not an integer')
if n < 0 :
    raise ValueError('Not a positive integer')
fact = 1
for i in range(n) :
        fact *= (i+1)
print(fact)
