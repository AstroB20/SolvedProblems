def sqrt(x):
    i=0
    while i*i<=x:
        i+=1
    if x-(i-0.5)*(i-0.5)>=0:
        return i
    else:
        return i-1
sqrt(26)