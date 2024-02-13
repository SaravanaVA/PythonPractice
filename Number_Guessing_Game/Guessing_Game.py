# simple game project without using function

import random


# game rules
print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")


guesslist = [0]

while True:

    randomnumber = random.randint(1,100)

    userguess = int(input('\n Enter a number from 1 to 100 : '))

    if userguess < 0 or userguess > 100:
       print('OUT of range please try again')
       continue

    if userguess == randomnumber:
        print(f'You won!!! \t Random num is \t{randomnumber} \tand your guss list is \t{guesslist}')
        break

    guesslist.append(userguess)
    # print(f'\n\n\n random number -- {randomnumber}\n\n\n')
    # print(f'\n\n\n guesslist -- {guesslist}\n\n\n')

    if guesslist[-2]:
        if abs(randomnumber-guesslist[-2]) > abs(randomnumber-guesslist[-1]) :
            print('Warmer')
        else:
            print('Colder')
    else:
        diff = abs(userguess-randomnumber)
        if diff<=10:
            print('Warm')
        else:
            print('Cold')
    
    pass