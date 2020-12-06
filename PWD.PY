import random
import string
LETTERS=string.ascii_letters
NUMS='0123456789'
SPE='@-+*%&$!_'
SYMBOLS=LETTERS+NUMS+SPE

while True:
    len=int(input("Enter Passowrd length:"))
    if len <0: 
        print("Enter length more than 0")
          
    
    elif len>=0:
     
        password= "".join(random.sample( SYMBOLS,len))
        print(f"Your Generated Passoword is {password}")
        break
      
