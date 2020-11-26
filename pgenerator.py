#!/usr/bin/env python
import random
alpha = ["A","C","D","F","H"]
number = [1,10,5,6,7,8]
small = ["a","f","r","h"]
char = ["!","@","^","*"]
ran1 = random.choice(alpha)+str(random.choice(number))+random.choice(small)+random.choice(char)
ran2 = random.choice(alpha)+str(random.choice(number))+random.choice(small)+random.choice(char)
print(ran1+ran2)
