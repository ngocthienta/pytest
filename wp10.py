s = None
if s == None :
    print(None)
elif not isinstance(s, str) :
    raise TypeError('Not a string')
else :
    s = s.split()
    news = ""
    for i in range(len(s)) :
        if i % 2 == 0 :
            news += s[i].upper() + " "
        else :
            news += s[i].lower() + " "
        print(news);
