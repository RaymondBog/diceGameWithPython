import random

while True:
    choice = input("Roll a dice? (y/n): ").lower()
    if choice == "y":
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        print(f"({roll1},{roll2})")
    elif choice == "n":
        print("Thanks for playing")
        break
    else:
        print("Invalid format. Please enter 'y' or 'n'.")
