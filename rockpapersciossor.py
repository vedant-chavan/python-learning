import random 

def choices():

    user_choice  = input("Enter your choice (rock, paper, scissor): ")
    computer = ['rock', 'paper', 'scissor']
    computer_choice = random.choice(computer)
    choices = {
        "user_choice" : user_choice,
        "computer_choice" : computer_choice
    }
    return choices

def check_win(user_choice, computer_choice):
    
    if user_choice == computer_choice:
        return (f"You choice {user_choice} and computer choice {computer_choice}. So it's a tie!")
    elif user_choice == "rock":
        if computer_choice == "scissor":
            return (f"You choice {user_choice} and computer choice {computer_choice}. So you win!")
        else:
            return (f"You choice {user_choice} and computer choice {computer_choice}. So computer wins!")
    elif user_choice == "paper":
        if computer_choice == "rock":
            return (f"You choice {user_choice} and computer choice {computer_choice}. So you win!")
        else:
            return (f"You choice {user_choice} and computer choice {computer_choice}. So computer wins!")
    elif user_choice == "scissor":
        if computer_choice == "paper":
            return (f"You choice {user_choice} and computer choice {computer_choice}. So you win!")
        else:
            return (f"You choice {user_choice} and computer choice {computer_choice}. So computer wins!")
    else:
        return (f"You choice {user_choice} and computer choice {computer_choice}. So invalid choice!")


choices = choices()
result = check_win(choices["user_choice"], choices["computer_choice"])
print(result)