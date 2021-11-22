from random import randint
NUM_LIVES = 5

print("i am thinking num between 1/100")
number = randint(1, 100)
print(number)
game_is_on = True
while game_is_on:
    # print("i am thinking num between 1/100")
    guess = int(input("make a guess?\n"))

    if guess > number:
        NUM_LIVES -= 1
        print("too high")
    elif guess < number:
        print("too low")
        NUM_LIVES -= 1
    else:
        print("You got it ")
        break

    if NUM_LIVES == 0:
        game_is_on = False
        print(f"the number was {number}")



