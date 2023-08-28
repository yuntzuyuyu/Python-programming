#Create a TenSidedDie and a TwentySidedDie class.
#These two class must extend SixSidedDie. T
#they must provide the same functionality

import random
class SixSidedDie:

    def __init__(self):
        self.side = 6

        self.value = random.randint(1,self.side)

    def roll(self):

        self.value = random.randint(1,self.side)

    def getFaceValue(self):
        
        return self.value
        

    def __repr__() :

        return "SixSidedDie({})".format(self.value)
    
class TenSidedDie(SixSidedDie):

    def __init__(self):
        self.side = 10

        self.value = random.randint(1,self.side)

class TwentySidedDie(SixSidedDie):

    def __init__(self):
        
        self.side = 20

        self.value = random.randint(1,self.side)
   
#Create a Cup class. A cup will hold several dice that may be rolled at once.
#The cup may hold any number of six-, ten-, or twenty- sided dice.

class Cup :

    def __init__(self,n_Six = 1 ,n_Ten = 1 ,n_Twenty= 1):

        self.n_Six = n_Six
        self.n_Ten = n_Ten
        self.n_Twenty = n_Twenty
        self.Sixlst = []
        self.Tenlst = []
        self.Twentylst = []


    def roll(self):

        for i in range(self.n_Six):
            s = SixSidedDie()
            s.roll()
            self.Sixlst.append(s.getFaceValue())
        for j in range(self.n_Ten):
            t = TenSidedDie()
            t.roll()
            self.Tenlst.append(t.getFaceValue())
        for k in range(self.n_Twenty):
            tt = TwentySidedDie()
            tt.roll()
            self.Twentylst.append(tt.getFaceValue())

        

    def sum(self):
        
        self.sum = 0 
        
        for x in self.Sixlst:
            self.sum += x
            
        for y in self.Tenlst:
            self.sum += y
            
        for z in self.Twentylst:
            
            self.sum += z
            
        return self.sum
    def __repr__(self):
        return "the sums of all dice is {}".format(self.sum)

        
