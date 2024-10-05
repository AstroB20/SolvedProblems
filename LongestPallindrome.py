def longestPalindrome(s:str):
    rs=s[::-1]
    l=len(s)
    lpal=""
    for i in range(l):
        for j in range(i+1,l+1):    
            sub=s[i:j]
            print(sub)
            if sub in rs:
                if len(sub)>len(lpal):
                    lpal=sub

    print(lpal)

longestPalindrome("bb")