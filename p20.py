def isValid(s):
    v=False
    st=[]
    if len(s)%2==1:
        return False
    for i in range(len(s)):
        if s[i]=="{" or s[i]=="[" or s[i]=="(":
            st.append(s[i])
        else:
            if len(st)>0:
                if s[i]=="}" and st[-1]=="{":
                    v=True
                    st.pop()
                elif s[i]=="]" and st[-1]=="[":
                    v=True
                    st.pop()
                elif s[i]==")" and st[-1]=="(":
                    st.pop()
                    v=True
                else:
                    v=False
                    return False
            else:
                return False
    if len(st)==0 and v==True:
        return True
    else:
        return False

print(isValid("[([])]"))
            