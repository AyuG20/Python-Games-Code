import random
low_bound=int(input("Enter lower bound:"))
up_bound=int(input("Enter upper bound:"))
attpt_list = []
def show_score():
    if len(attpt_list) < 0:
        print("No High Score. Start playing to score")
    else:
        print(f"New high score is:{min(attpt_list)}")

def start_game():
    attempt=0
    rand_num=random.randint(low_bound,up_bound)
    game_start = input(f"Would you like to play {name}?.Enter (Yes or No): ")
    while game_start.lower() == "yes" :
        guess = int(input(f"pick number between {low_bound} and {up_bound}:"))
        if guess == rand_num :
            print("Yipee! You got it")
            attempt += 1
            attpt_list.append(attempt)
            print(f"It tooks you {attempt} attempts.")
            break
        elif guess < low_bound or guess > up_bound:
            print("Guess number within range")
        elif guess > rand_num:
            print("Correct Number is lower")
            attempt+=1
        elif guess < rand_num:
            print("Correct Number is higher")
            attempt+=1
        else:
            break
name = input("Enter Your Name:")
start_game()
play_again=input("Would you like to play again:")
attempt=0
show_score()
if play_again.lower()== "no":
    print("Fine! Have a great day")
    exit(0)
else:
    start_game()
if __name__ == '__main__':
    start_game()
