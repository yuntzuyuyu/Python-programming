
import random

def main():

    q = True

    while q == True:

        num,randomlst = numandlst()

        dic = sumdictionary(num,randomlst)

        display(dic)

        q = loopquestion()

    return "goodbye"
        
        

        

# Ask the user for i and n. Create a list of i random numbers between 0 and 100.

def numandlst():

    num = eval(input("What is the number you're trying to find?"))
    
    numlst = eval(input("How many numbers in the list that you are trying to create?"))
    
    randomlst = random.sample(range(0,100),numlst)

    return num,randomlst

#create the dictionary for two numbers sums up to n


def sumdictionary(num,randomlst):
    

    sumdictionary = {}

    for i in range(len(randomlst)):

        n1 = randomlst[i]

        if num > randomlst[i]:

            n2 = num - randomlst[i]
            
            n3 = BinarySearch(n2, randomlst)

            if n3 == False :

                 return False

                #return " Can not find the number that sums up as {}".format(num)
            else :
                
                sumdictionary[num] = [n1,n3]
                
    return sumdictionary


# Binary Search. to see if the second number is in the list

def BinarySearch(n2, randomlst):
    
    randomlst.sort()

    low = 0
    
    high = len(randomlst) - 1

    while low <=high :

        mid = int((low + high)/2)

        item = randomlst[mid]

        if n2 == item:

            return randomlst[mid]

        elif n2 < item:

            high = mid -1
        else:

            low = mid +1
            
    return False

def display(dic):



    if dic != False:

        for key,item in dic.items():

            print("We found {}+{}={}".format(item[0],item[1],key))         

    else:
            
        print("We can't find any number summing up to in the list")

    

def loopquestion():

    q = input("Do you want ot continue please answer yes or no ?")

    if q.lower() == "no":
        return False
    else:

        return True
