#Password validation

import re

print("Create a new password" + """\n\t
*At least 1 small letter between [a-z] and 1 capital letter between [A-Z].
*At least 1 number between [0-9].
*At least 1 character from [%$#@].
*Minimum length 6 characters.
*Maximum length 16 characters.
""")

p= input("Input your password ")
x = True
while x:  
    if (len(p)<6 or len(p)>17):
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[A-Z]",p):
        break
    elif not re.search("[%$#@]",p):
        break
    elif re.search("\s",p):
        break
    else:
        print("Valid Password")
        x=False
        break
    
    
if x:
    print("Not a Valid Password")