def uppercase_lowercase_words(s):
    if not isinstance(s, str) :
        raise TypeError('Not a string')
    elif s is None:
        return None
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

print(uppercase_lowercase_words('Lorem ipsum dolor sit amet'))
