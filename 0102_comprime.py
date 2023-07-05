
    
#check the if two numbers are co-prime


def coprime(a,b):
    
    

    lst_a = []
    lst_b = []
                 
    for i in range(2,a+1):
        if a % i == 0 :
            lst_a.append(i)
    for j in range(2,b+1):
        if b % j == 0 :
            lst_b.append(j)
            
    for x in lst_a:
        if x in lst_b:
            return False
    for y in lst_b:
        if y in lst_a:
            return False
        else:
            return True



def coprime_test_loop():
    a = eval(input("enter one number",))
    b = eval(input("enter another number",))
    x = coprime(a,b)
    
    while True:

        if x is True :
            print("They are co-prime numbers")
            ans=input("Do you want to contitnue? yes or no")
            if ans.lower() == "yes":
                a = eval(input("enter one number",))
                b = eval(input("enter another number",))
                x = coprime(a,b)
            elif ans.lower() == "no":
                return None
                
                
            else:
                print("please enter yes or no")
                
                
                
        else:
            print("They are not co-prime numbers")
            ans=input("Do you want to contitnue? yes or no")
            if ans.lower() == "yes":
                a = eval(input("enter one number",))
                b = eval(input("enter another number",))
                x = coprime(a,b)
            elif ans.lower() == "no":
                return None
                
                
            else:
                print("please enter yes or no")                
            
            
    
            
            
  






