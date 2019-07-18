year = int(input("enter an year:"))
if  year % 400 == 0 and year % 100 == 0:
    print("its a leap year")
elif year % 400 != 0:
    print("its not a leap year")
else:
    print("Error")        

