def generateParantheses(n):
    stack=[]
    res=[]

    def backtrack(open,closed):
        if open==closed==n:
            res.append("".join(stack))
        if open<n:
            stack.append("(")
            backtrack(open+1,closed)
            stack.pop()
        if open>closed:
            stack.append(")")
            backtrack(open,closed+1)
            stack.pop()
    backtrack(0,0)
    return res
print(generateParantheses(3))