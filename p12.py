def intToRoman(num:int):
    i=0
    res=""
    vals=[["M",1000],["CM",900],["D",500],["CD",400],["C",100],["XC",90],["L",50],["XL",40],["X",10],["IX",9],["V",5],["IV",4],["I",1]]
    while num>0:
        if num<vals[i][1]:
            i+=1
        else:
            num-=vals[i][1]
            res+=vals[i][0]
    return res
print(intToRoman(109))

        
        
        
        