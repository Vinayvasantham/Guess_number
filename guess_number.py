import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}'))
        if guess > random_number:
            print('Sorry ! Guess is too low')
        elif guess < random_number:
            print('Sorry ! Guess is too high')
        else:
            print('Yeah.. YOU WON!')

#print(guess(3))

def computer_guess(num):
    low = 1
    high = num
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(1,num)
        else:
            guess = low
            break
        feedback = input(f'Is {guess} too low (L),Is too high(H),or Is correct (C)?? ').lower()
        if feedback == 'h':
            low = guess-1
        elif feedback == 'l':
            high = guess+1
    print(f'Yeah computer guessed your number correctly that is {guess}')


computer_guess(10)