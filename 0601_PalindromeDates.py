#A palindrome date is a date that is the same when read forwards and backwards, e.g., ‘02/02/2020’. Write
#a program that identifies and saves to a file all the palindrome dates in the 21st century using the
#DD/MM/YYYY format. Do not use recursion. Do not use any built-in calendar-ish packages. To keep
#things simple, treat leap years as regular years.

def date():

    for year in range(2000,2100):
        
        for month in range(1,13):
            months = '%02d'%month
            for day in range(1,32):
                days = '%02d'%day
                date = str(days)+str(months)+str(year)
                
                if palindrome(date) is True and day not in [29,30,31] :
                    
                        print("{}/{}/{}".format(days,months,year))

                

                
def palindrome(string):

    if string ==string[::-1]:
        return True
    else:
        return False
        
