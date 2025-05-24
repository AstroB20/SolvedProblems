def evalString(s , cache):
    s = s.strip()
    if '+'in s:
        parts = s.split('+')
        op = '+'
    elif '-' in s:  
        parts = s.split('-')
        op = '-'
    elif '*' in s:
        parts = s.split('*')
        op = '*'    
    elif '/' in s:
        parts = s.split('/')
        op = '/'
    else:
        return "Invalid operation"
    num = map(int, parts)
    prefix =str(op)+",".join(sorted(parts))
    print("Prefix: ", prefix)
    if prefix in cache:
        print("Cache hit")
        print(cache[prefix])
    else:
        if op == '+':
            result = sum(num)
        elif op == '-':
            result = num[0] - sum(num[1])
        elif op == '*':
            result = 1
            for n in num:
                result *= n
        elif op == '/':
            result = num[0]
            for n in num[1:]:
                result /= n
        print("Result: ", result)
        cache[prefix] = result
    return cache
cache = {}  
while True:
    print("Cache: ", cache)
    s = input("Enter a string: ")
    if s == "exit":
        break
    else:
        cache = evalString(s, cache)

        

    