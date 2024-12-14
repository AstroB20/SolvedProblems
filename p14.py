def longestCommonPrefix(strs):
    res=""
    w=strs[0]
    for i in range(len(w)):
        for wd in strs:
            if len(wd)==i or wd[i]!=w[i]:
                return res
        res+=w[i]
x=longestCommonPrefix(["flower","flower","flower","flower"])
print(x)