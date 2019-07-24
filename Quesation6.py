'''
           ________PASSWORD CHECKER________
 
Create a function that validates a password to conform to the following rules: 
  
#    Length between 6 and 24 characters. 
#    At least one uppercase letter (A-Z). 
#    At least one lowercase letter (a-z). 
#    At least one digit (0-9). 

'''


a = list(input("enter new password: "))
if len(a) < 6 or len(a) > 24 :
    print("min 6 max 24 digits allow")

elif not(any(map(str.isupper, a))):
    print("ERRor At least one uper case alphabet: ")


#elif any(map(str.isupper, a)):
#   print("error At least one lower case alphabet: ")

elif not any(i.isdigit() for i in a):
    print("3RR0R at least add one digit ")  

s_c = ["!","@","#","$","%","^","&","*"]
if not any(character in s_c for character in a) :
    print("invalid: your password must contain !@#$%^&* any of these charactor: ")

else:
    print("PASSWORD has been created: ")