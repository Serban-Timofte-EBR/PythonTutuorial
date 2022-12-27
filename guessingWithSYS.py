from random import randint
import sys
answer = randint(int(sys.argv[1]),int(sys.argv[2]))
while True:
    try:
        print(answer)
        guess = input("Guess a number 1 to 10: ")
        if 0 < int(guess) < 11:
            if int(guess) == answer:
                print(f"Was {answer}! Really genius!")
                break
        else:
            print("I told you a number 1 to 10!")
    except ValueError:
        print("Plese enter a number")
        continue
