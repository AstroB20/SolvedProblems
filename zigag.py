def convert(s,numRows:int):
    resStr=""
    for r in range(numRows):
        inc=2*(numRows-1)
        for i in range(r,len(s),inc):
            resStr+=s[i]
            if r>0 and r<numRows-1 and i+inc-2*r<len(s):
                resStr+=s[i+inc-2*r]
    print(resStr)

convert("abcdefg",3)