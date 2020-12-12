import random

# THIS FUNCTION WILL RUN FOR SINGLE MODE

def game_single(p1_turn, player_2):
    if p1_turn == player_2.upper():   # TIE CONDITION
        print(f"{player_name},Your Game is Tie")
    elif p1_turn == 'R':
        if player_2 == 'p' or player_2 == 'P':
            print(f"{player_name} Wins")
        elif player_2 == "s" or player_2 == 'S':
            print(f"{player_name} Loses")
    elif p1_turn == "S":
        if player_2 == "p" or player_2 == "P":
            print(f"{player_name} Loses")
        elif player_2 == "r" or player_2 == "R":
            print(f"{player_name} Wins")
    elif p1_turn == "P":
        if player_2 == "s" or player_2 == "S":
            print(f"{player_name} Wins")
        elif player_2 == "r" or player_2 == "R":
            print(f"{player_name} Loses")


#--------------------------------------------------------

#THIS FUNCTION WILL RUN FOR ROUND MODE

def game_round(p1_turn, player_2):
    if p1_turn == player_2.upper():
        print(f"Computer choice: {p1_turn}\n")
        print(f"Your choice is: {player_2}\n")
        print("No score scored by each party.\n\n")
        return None
    elif p1_turn == 'R':
        if player_2 == 'p' or player_2 == 'P':
            print(f"Computer choice: {p1_turn}\n")
            print(f"Your choice is: {player_2}\n")
            print(f"{player_name} SCORED\n\n")
            return 1
        elif player_2 == "s" or player_2 == 'S':
            print(f"Computer choice: {p1_turn}\n")
            print(f"Your choice is: {player_2}\n")
            print(f"Computer SCORED\n\n")
            return 0
    elif p1_turn == "S":
        if player_2 == "p" or player_2 == "P":
            print(f"Computer choice: {p1_turn}\n")
            print(f"Your choice is: {player_2}\n")
            print(f"Computer SCORED\n\n")
            return 0
        elif player_2 == "r" or player_2 == "R":
            print(f"Computer choice: {p1_turn}\n")
            print(f"Your choice is: {player_2}\n")
            print(f"{player_name} SCORED\n\n")
            return 1
    elif p1_turn == "P":
        if player_2 == "s" or player_2 == "S":
            print(f"Computer choice: {p1_turn}\n")
            print(f"Your choice is: {player_2}\n")
            print(f"{player_name} SCORED\n\n")
            return 1
        elif player_2 == "r" or player_2 == "R":
            print(f"Computer choice: {p1_turn}\n")
            print(f"Your choice is: {player_2}\n")
            print(f"Computer SCORED\n\n")
            return 0


#---------------------------------------------------------

#IF YOU CHOOSE OPTION 1 SINGLE MODE THIS SUBROUTINE WILL EXECUTE

def single_mode():
    print("Choose your move.\n1.Rock(R)\n2.Paper(P)\n3.Scissor(S)")
    player_1 = random.randint(1, 3)  # COMPUTER CHOOSES BETWEEN 3 OPTIONS
    if player_1 == 1:
        p1_turn = 'R'
    elif player_1 == 2:
        p1_turn = 'P'
    elif player_1 == 3:
        p1_turn = 'S'
    player_2 = input(f"Choose your turn {player_name}:  ")
    game_single(p1_turn,player_2)
    print(f"Computer choice: {p1_turn}\n")
    print(f"Your choice is: {player_2}\n")
    res=int(input("Would you like to play again ( 1 for Yes and 0 for No)?\n"))
    if res == 1:
        restart()
    elif res == 0:
        print("Thanks For Playing")


#--------------------------------------------------------

#IF YOU CHOOSE OPTION 2 ROUND MODE THIS SUBROUTINE WILL EXECUTE

def round_mode():
    round=5
    com_score=0
    your_score=0
    for j in range(round):
        print("Choose your move.\n1.Rock(R)\n2.Paper(P)\n3.Scissor(S)\n\n")
        player_1 = random.randint(1, 3)
        if player_1 == 1:
            p1_turn = 'R'
        elif player_1 == 2:
            p1_turn = 'P'
        elif player_1 == 3:
            p1_turn = 'S'
        player_2 = input(f"Choose your turn {player_name}:  ")



 #THIS PART IS TAKING TOTAL SCORE FOR ROUND MODE AND GIVE US WINNER OF ROUND MODE

        x= game_round(p1_turn,player_2)
        if x == 1:
            your_score+=1
        elif x == 0:
            com_score+=1
    if your_score > com_score:
        print(f"\n{player_name} Wins\n")
        print(f"{player_name} scored:{your_score}\n")
        print(f"Computer scored:{com_score}\n")
    elif com_score > your_score:
        print(f"\n{player_name} Loses\n")
        print(f"\n{player_name} scored:{your_score}\n")
        print(f"Computer scored:{com_score}\n")
    elif com_score == your_score:
        print("Game Tied\n")
    res=int(input("Would you like to play again ( 1 for Yes and 0 for No?)\n"))
    if res == 1:
        restart()
    elif res == 0:
        print("\nThanks For Playing\n")

#------------------------------------------------------

#  TO RESTART THE GAME

def restart():
    print("Choose Mode \n 1. Single mode Vs Computer\n 2. Round Mode Vs Computer\n")
    mode_select=int(input("Choose mode\n"))
    mode(mode_select)

#------------------------------------------------------

# TO SELECTING A GAME MODE

def mode(i):
    switcher = {
        1: single_mode,
        2: round_mode
    }
    func=switcher.get(i,lambda:"invalid choice")
    return func()

#------------------------------------------------------

if __name__ == '__main__':
    print("O||\/ROCK PAPER SCISSOR GAME\/||O")
    player_name = input("Enter your Name:")
    print("Choose Mode \n 1. Single mode Vs Computer\n 2. Round Mode Vs Computer\n")
    mode_select=int(input("Choose mode\n"))
    mode(mode_select)





