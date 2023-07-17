def main():
    greeting()

    x = loop()
    while x is True:
        
        num = getInput()
        lst = openFile(num)
        dic = StemAndLeaf(lst)
        plot(dic)
        x = loop()
    return "goodbye"



def greeting() :

    print("This is for plot the file 1 or 2 or 3 as a StemAndLeaf ")

def getInput():
    num =eval(input("Please enter 1 or 2 or 3 to decide which file you want to open"))
        

    return num

def openFile(num):

    file  = "StemAndLeaf"+ str(num)+".txt"

    outfile = open(file,"r")

    readfile = outfile.readlines()

    return readfile


def StemAndLeaf(lst):

    dic ={}

    numlst = []

    for i in lst:
        numi = int(i)
        numlst.append(numi)
        
    for nums in numlst:
        key , value = nums//10 , nums % 10
        if key not in dic:
            dic[key] = []
            dic[key].append(value)
        else :
            dic[key].append(value)
            
    return dic

def plot(dic):

    for x, y in dic.items():
        print("{:5}  |  {}".format(x, y))

    
def loop():
    ans = input("Do you want to execute the stem and leaf program , please answer yes or no ")

    if ans.lower() == "yes":
        return True
    else :
        return "Good bye"
        
        



    
    
    
