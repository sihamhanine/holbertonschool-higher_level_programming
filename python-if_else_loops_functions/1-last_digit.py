#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastd = abs(number) % 10
if number < 0:
    lastd *= -1
#imprimer le last digit
print("Last digit of", number, "is", lastd, end=" ")
if lastd > 5:
    print("and is greater than 5")
elif lastd == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
    
    
