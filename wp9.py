def capitalize_words(s):
    #remove unnecessary white spaces
    s = s.split()
    news = " ".join(s)
    #print
    return print(news.title());
s = input()
capitalize_words(s)
