import random

while True:
    user_action = input("Enter a choice (rock, paper, scissors): ")
    # A prompt and input asking the user to pick

    possible_actions = ["rock", "paper", "scissors"]
    # Actions possible by both players 

    computer_action = random.choice(possible_actions)
    # Telling computer to randomly choose one of the above Actions

    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")
    # \n = New Line or End of Line, tells my command and computer commands in text

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
        # Results in tie when both inputs are the same

    elif user_action == "rock":
    # elif means: if previous conditions untrue, try this condition

        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
            # Previous was rock v rock, this one is rock v scissors

        else:
            print("Paper covers rock! You lose.")
            # Previous was rock v rock, rock v scissors, and now rock v paper, you lose

    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
    # Repeat for all other possible outcomes, game ends and prompt below asks for input, loop

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
