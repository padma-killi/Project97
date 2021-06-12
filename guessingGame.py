import random
number=random.randint(1,9)
lives=0
while lives<5:
        guess=int(input('Enter an integer from 1 to 9 '))
        lives=lives+1
        if(guess==number):
                print('Congrats you WON!!!!!!!!!!!')
                break
        if(guess<number):
                print('your guess was low try a number higher than ',guess)
        if(guess>number):
                print('your guess was high try a number lower than ',guess)

if not lives<5:
        print('You LOST!!!! The number is ',number)
