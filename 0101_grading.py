def grade():
    grade = 0
    a = input("If the assignment is not submitted as a single uncompressed,yes or no" ,)
    while True :
        if a.lower() == "no":
            return grade
        elif a.lower() !="yes":
            print("Please enter yes or no")
            a = input("If the assignment is not submitted as a single uncompressed,yes or no" ,)
        else :
            b=input("If the assignment does not include the author’s name and date,yes or no" ,)
            while True:
                if b.lower() == "no":
                    return grade
                elif b.lower()!= "yes":
                    print("Please enter yes or no")
                    b=input("If the assignment does not include the author’s name and date,yes or no" ,)
                else:
                    c=input("If the assignment does not include the honor statement,yes or no" ,)
                    while True:
                        if c.lower() == "no":
                            return grade
                        elif c.lower()!= "yes":
                            print("Please enter yes or no")
                            c=input("If the assignment does not include the honor statement,yes or no" ,) 
                        else:
                            d=input("If the assignment does not include a link to an unlisted 3-minute YouTube video ,yes or no ")
                            while True:
                                if d.lower() == "no":
                                    return grade
                                elif d.lower()!= "yes":
                                    print("Please enter yes or no")
                                    d=input("If the assignment does not include a link to an unlisted 3-minute YouTube video ,yes or no ") 
                                else:
                                    e= eval(input("Up to ten points are awarded based on the correctness of the code; that is, how well it meets the given specifications"))
                                    grade+=e
                                    f= eval(input("Up to ten points are awarded based on the elegance of the code (data structure selection,algorithm efficiency, function implementation,"))
                                    grade+=f
                                    g= eval(input(" Up to ten points are awarded based on the code hygiene"))
                                    grade+=g
                                    h= eval(input("Up to ten points are awarded based on the quality of the discussion in the YouTube video"))
                                    grade+=h

                                    i = input("if you are late?, yes or no:")
                                    while True:
                                        if i.lower() =="no":
                                            return grade
                                        elif i.lower()!= "yes":
                                            print("Please enter yes or no")
                                            i = input("if you are late?, yes or no:")
                                        else:
                                            j = eval(input("how many hour you are late ?"))
                                            return grade - grade*j/100
                                    
                
                            
                    
            


                    
        
     
