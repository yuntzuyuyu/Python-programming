def main():
    while True:
        
        n = getInput()

        if n != 0 :
        
            ifprime = isPrime(n)
            
            ifHappyNumber = isHappyNumber(n)
            
            display(ifprime,ifHappyNumber,n)
        else:
            return " Goodbye"


def getInput():

    num  = eval(input("Please enter a number that you want to test or press  0 to exit"))

    return num  
        

def isPrime(n):

    i = 2

    for num in range(2,n):

        if n % i == 0 :

            return False

        i += 1
        
    return True
               
def SumofSquare(num):

    sum = 0

    for x in str(num):

        sum += int(x)**2
        
    return sum



def isHappyNumber(n):

    sumNum_lst = []

    while True :

        n = SumofSquare(n)

        if n not in sumNum_lst:

            sumNum_lst.append(n)

        elif n == 1 :

            return True

        else :

            return False
            
            
def display(ifprime,ifHappyNumber,n):

    x = ifprime

    y =  ifHappyNumber


    if x and y is True :

        print("The number {:2} is a happy prime".format(str(n)))
        
    elif x is True and y is False :
        
        print("The number {:2} is a sad prime".format(str(n)))
        
    elif x is False and y is True :
        
        print("The number {:2} is a happy non - prime".format(str(n)))
        
    else:
        
        print("The number {:2} is a sad non -prime".format(str(n)))
    
    


