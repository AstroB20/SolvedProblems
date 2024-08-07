def Menu():
    cases=int(input("Enter number of cases :"))
    listCases=[]
    for i in range(cases):
        l=list(input(""))
        listCases.append(l)
        return listCases
def ValidCases(listCases):
    for li in listCases:
        if li[2]>li[0] and li[2]<=li[1]:
            print("Valid")
        else:
            print("Invalid")
    
listCases=Menu()
ValidCases(listCases)