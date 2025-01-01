def countAndSay(n:str):
    ct = 1
    res = ""
    n = list(n)
    current = n[0]
    for i in range(1, len(n)):
        if n[i] == current:
            ct += 1
        else:
            res += str(ct) + current
            ct = 1  
            current = n[i]
    res += str(ct) + current
    print(res)
            
countAndSay("1111")

