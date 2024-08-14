import random


def get_user_action():
    while True:
        try:
            user_action = int(input("Enter your value (1: ROCK, 2: PAPER, 3: SCISSOR) = "))
            if user_action in [1, 2, 3]:
                return user_action
            else:
                print("Invalid input! Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def determine_winner(user_action, computer_action):
    if user_action == computer_action:
        return "tie"
    elif (user_action == 1 and computer_action == 3) or \
            (user_action == 2 and computer_action == 1) or \
            (user_action == 3 and computer_action == 2):
        return "win"
    else:
        return "lose"


def main():
    actions = {1: "ROCK", 2: "PAPER", 3: "SCISSOR"}
    possible_outcome = [1, 2, 3]

    user_score = 0
    computer_score = 0
    rounds = int(input("Enter Number of Rounds = "))  # Number of rounds

    for _ in range(rounds):
        print(f"\nRound {_ + 1} of {rounds}")

        user_action = get_user_action()
        computer_action = random.choice(possible_outcome)

        map_user_action = actions[user_action]
        map_computer_action = actions[computer_action]

        print(f"You chose: {map_user_action}")
        print(f"Computer chose: {map_computer_action}")

        result = determine_winner(user_action, computer_action)

        if result == "tie":
            print("It's a Tie!")
        elif result == "win":
            print("You Win this round!")
            user_score += 1
        else:
            print("You Lost this round!")
            computer_score += 1

        print(f"Score: You {user_score} - {computer_score} Computer")

    # Final Score and Result Announcement
    print("\nFinal Score:")
    print(f"Your Score: {user_score}")
    print(f"Computer's Score: {computer_score}")

    if user_score > computer_score:
        print("Congratulations! You won the game!")
    elif user_score < computer_score:
        print("Sorry, you lost the game. Better luck next time!")
    else:
        print("The game is a tie!")


if __name__ == "__main__":
    main()
