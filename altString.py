def alternate(word1,word2):
    word=""
    ct=-(len(word1)) if len(word1)<=len(word2) else len(word2)
    for i in range(abs(ct)):
        word+=word1[i]
        word+=word2[i]
    if ct>0:
        word+=word1[abs(ct):]
    elif ct<0:
        word+=word2[abs(ct):]
    print(word)
alternate("ABCDEFG","VWX")


