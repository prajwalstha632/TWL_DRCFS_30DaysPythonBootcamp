import random

options = [
           'rock', 
           'paper', 
           'scissor'
]

me = 0
you = 0
i = 0

while i < 5:
    i += 1
    # computer = random.choice(options)
    user = input("enter your guess (rock, paper, scissor): ")
    computer_choice = random.choice(options)
    if user == "rock":
        print("You chose rock")
    elif user == "paper":
        print("You chose paper")
    elif user == "scissor":
        print("You chose scissor")
    else:
        print("You chose invalid number")
        choose_again = input("Do choose the choices again carefully: ")
    
    if user == computer_choice:
        print(f"Computer chose {computer_choice}")
        print("Its a tie")
        # me += 1
        # you += 1
    elif (user=='rock' and computer_choice=='scissor') or (user=='paper' and computer_choice=='rock') or (user=='scissor' and computer_choice=='paper'):
        me += 1
        print(f"Computer chose {computer_choice}")
        print("HOORAY!! You Win")
    else:
        you += 1
        print(f"computer chose {computer_choice}")
        print("computer Wins")

if me == you:
    print('*' * 50)
    print("The game is drawn")
    print(f"You won {me} times")
    print(f"Computer won {you} times")
elif me > you:
    print('*' * 50)
    print(f"You won the game")
    print(f"You won {me} times")
    print(f"Computer won {you} times")
else:
    print('*' * 50)
    print(f"Computer won the game")
    print(f"Computer won {you} times")
    print(f"You won {me} times")