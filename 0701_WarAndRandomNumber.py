import random

class WarAndPeacePseudoRandomNumberGenerator:

    def __init__(self,seed):
        self.seed = seed

    def randomnum(self) :

        lst = []
        count = 0

        file = open("book-war-and-peace.txt","r")
        a = random.randint(3,self.seed)
        
        while count < 32 :
            
            file.seek(a)
            x = file.read(1)
            b = a + 100
            file.seek(b)
            y = file.read(1)

            if x > y :
                lst.append(1)
                count += 1
                a = b + 100
            elif x < y:
                lst.append(0)
                count += 1
                a = b + 100
            else:
                a = b + 100
                
        num = 0
    
        for i in range(32):
            
            num += lst[i] * pow((1/2),(i+1))
        file.close()
        return num
                              
                              
    def result(self,times) :
        resultlst = []
        resultnum = 0
        self.times = times

        for j in range(self.times):

            r = self.randomnum()
            resultlst.append(r)
            resultnum += r
        maxnum = max(resultlst)
        minnum = min(resultlst)
        meannum = resultnum/self.times

        print("mean number is: " ,meannum )
        print("maximun number is: " ,maxnum )
        print("minimun number is: " ,minnum  )


 

             
             
         
         

        




         

             
             
                

       

            
