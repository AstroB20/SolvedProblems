def divide(dividend, divisor):
    dneg=False
    Dneg=False
    quotient=0
    
    if dividend<0:
        Dneg=True
        dividend*=-1
    if divisor<0:
        dneg=True
        divisor*=-1
    while dividend>=divisor:
        dividend-=divisor
        quotient+=1

    if dneg:
        if Dneg:
            return quotient
        else:
            return quotient*(-1)
    if Dneg:
        if dneg:
            return quotient
        else:
            return quotient*(-1)
    return quotient

print(divide(10,2))