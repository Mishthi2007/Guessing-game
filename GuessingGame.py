import random
print('Number Guessing game')
number=random.randint(1,9)
chances=0
while chances<5 :
    g=int(input('enter your guess'))
    if g==number :
        print('Mind reading going on...!')
        break
    elif g<number :
        print('Think higher')
    else : 
        print('Think lower')
    chances=chances+1
if not chances<5 : 
    print('You lost the number is',number)