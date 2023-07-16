def main():
    
    num = eval(input("What is the range that you want to test?"))
    lst = Primelst()
    primeDict =GoldbachConjecture(lst,num)
    display(primeDict)



def isPrime(n):

    i = 2
    while n > i :

        if n % i == 0 :
            return False
        i += 1
    return True




def Primelst():

    numlst = []

    for num in range(2,100):

        if isPrime(num) == True:
            numlst.append(num)
    return numlst

def GoldbachConjecture(lst,num):


    primeDict = {}

    for i in range(2,num,2):
        if i == 2:
            primeDict[i] = (1,1)
        else:
            for a in lst:
                for b in lst:
                    if i == a+b:
                        primeDict[i]=(a,b)
    return primeDict


def display(primeDict):

    for key, value  in primeDict.items():
        

       print("{:2}".format(key)," = ","{:2}".format(value[0])," + " ,"{:2}".format(value[1]))
                        

    
               

        

    
