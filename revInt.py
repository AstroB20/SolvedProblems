def reverse(self, x):
    stack=[]
    rev=0
    ct=0
    neg=False
    if x<0:
        neg=True
        x=x*-1
    temp=x
    while temp!=0:
        stack.append(temp%10)
        temp=int(temp/10)
        ct+=1
    for i in range(len(stack)):
        rev=rev+stack[i]*10**(ct-1)
        ct-=1
    if neg==True:
        rev=rev*-1
    if rev>-2**31 and rev<2**31-1:
        return rev
    else:
        return 0