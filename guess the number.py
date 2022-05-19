from time import *
from random import randint
print("Game - 'Guess the number!'")
name_player = input('Hi dude, what is your name?---> ')
our_number = randint(1, 101)
total=1
while True:
    user_num = int(input(f'{name_player}, enter a number from 1 to 100: '))
    sleep(1)
    if user_num > our_number:
        total+=1
        print('Ops, too much,lets go again')
    elif user_num < our_number:
        total+=1
        print('Too little, think again')
    else:
        print('WOOOOW, THATS RIGHT, CONGRATULATION, it took you',total,'tries')
        sleep(2)
        print(f'{name_player}, maybe one more game?')
        sleep(0.5)
        if input().lower() == 'yes':
            sleep(1)
            print('')
            num = randint(1, 100)
            continue
        else:
            sleep(1.5)
            print('hmmm')
            sleep(1.5)
            print('Okay,its your choise 'f'{name_player}, good luck and see you later!')
            sleep(7)
            print('So why did you stay?)')
            sleep(5)
            print('mb one more?;)')
            sleep(5)
            print('okay,bb')
            sleep(3)
            break