import random
secret_number = random.randint(1, 10)
guess = int(input("Guess the number between 1 and 10: "))
match guess:
    case _ if guess == secret_number:
       print ("Yaauy! You nailed it!")
    case _ if guess < secret_number:
       print (f"Too low! The number was {secret_number}")
    case _ if guess > secret_number:
        print (f"Too high! The number was {secret_number}")
    case _:
        print ("Invalid input! Please enter a number between 1 and 10.")
# --- IGNORE ---


