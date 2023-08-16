def humanpyramid(row,col):


    #each point pass half of weight to the next point
    weight = 128/2

    if row == 0 and col == 0 :#first one just give wieight and also is my base case to stop the recursive

        return 0
    
#for the left side person they only gather one previous person weight
#example: (1,0)+64
    
    elif row == 0  :

        return  weight + (humanpyramid(0 , col-1)/2)

#for the right side person they only gather one previous person weight
#example: (1,1)+64
    
    elif row == col :

        return  weight + (humanpyramid(row-1 , col-1)/2)

    else :

        return weight*2+(humanpyramid(row-1 , col-1)/2)+(humanpyramid(row , col-1)/2)

        
        
def call():

    row = eval(input("enter which row you are looking for"))

    col = eval(input("enter which column you are looking for"))

    return humanpyramid(row,col)
    
