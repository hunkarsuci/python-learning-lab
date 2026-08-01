from random import randint 
# generate a number 1~10
answer = randint(1,10)

# input from user?


# check that input is a number 1~10
while True: 
    try:
        print(answer)
        guess = int(input('guess a number 1~10: '))
        if 0 < guess < 11:
            if guess == answer:
                print('you are a genius!')
                break
        else: 
            print('Hey Bozo, I said 1~10')
            
    except ValueError:
        print('Enter a number')
        continue # keep looping until we get the right answer

# check if number is the right guess. Otherwise ask again 



