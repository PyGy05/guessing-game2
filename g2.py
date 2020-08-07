from random import randint
# you will need to run this on your machine and not this website for the sys.argv to work!
import sys

answer = randint(int(sys.argv[1]), int(sys.argv[2]))

while True:
    try:
        guess = int(input(f'guess a number {sys.argv[1]}~{sys.argv[2]}:  '))
        if int(sys.argv[1]) < guess < int(sys.argv[2]):
            if guess == answer:
                print('you are a genius!')
                break
        else:
            g1 = int(sys.argv[1])
            g2 = int(sys.argv[2])
            print('hey bozo, you said', g1, '~', g2, "guess again!")
    except ValueError:
        print('please enter a number')
        continue
