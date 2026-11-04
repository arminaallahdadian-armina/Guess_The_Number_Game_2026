import random

print("=" * 45)
print("       WELCOME TO GUESS THE NUMBER! 🎀")
print("=" * 45)

while True:

    secret_number = random.randint(1, 100)
    max_attempts = 5
    attempts = 0
    won = False

    print("\nI have selected a number between 1 and 100.")
    print("You have 5 chances to guess it. 💗")
    print("-" * 45)

    while attempts < max_attempts:

        print(f"\nAttempt {attempts + 1} of {max_attempts}")
        print(f"Remaining chances: {max_attempts - attempts}")

        try:
            guess = int(input("Enter your guess: "))

        except ValueError:
            print("\nOops! That didn't work! 😔")
            print("Don't give up! Try again! 💗")
            continue

        if guess < 1 or guess > 100:
            print("\nOops! Please enter a number between 1 and 100! 😔")
            continue

        attempts += 1

        if guess == secret_number:

            print("\n" + "=" * 45)
            print("       YOU DID IT! 🎉🥳")
            print("=" * 45)

            won = True

            if attempts == 1:
                print("Your rank: Excellent! 🌟")
            elif attempts == 2:
                print("Your rank: Very Good! 💖")
            elif attempts == 3:
                print("Your rank: Good! 🌸")
            elif attempts == 4:
                print("Your rank: Acceptable! ✨")
            else:
                print("Your rank: Lucky Winner! 🍀")

            break

        difference = abs(secret_number - guess)

        print("\nOops! That didn't work! 😔")
        print("Don't give up! Try again! 💗")

        if guess > secret_number:
            print("Try a smaller number! ⬇️")
        else:
            print("Try a bigger number! ⬆️")

        if difference <= 5:
            print("OHH! SO CLOSE! 😭💕")
        elif difference <= 15:
            print("You're getting closer! 😌💗")
        else:
            print("Too far! Keep trying! 🥺")

    if not won:

        print("\n" + "=" * 45)
        print("       GAME OVER! 💔")
        print("=" * 45)

        print("You ran out of chances!")
        print(f"The secret number was: {secret_number}")

    print("\n" + "-" * 45)

    while True:

        play_again = input(
            "Do you want to play again? (yes/no): "
        ).lower().strip()

        if play_again == "yes":
            print("\nYay! Let's play again! 🎀")
            break

        elif play_again == "no":
            print("\nThank you for playing! 💗")
            print("See you next time! 👋")
            exit()

        else:
            print("\nInvalid choice! Please enter yes or no. 😔")