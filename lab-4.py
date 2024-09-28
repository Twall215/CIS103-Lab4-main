import random

def compare():
    #tallys the score and holds in storage until the game is complete
    score = {
        "user score": 0,
        "bot score": 0
    }
    round = 1 #starts off the round counter
    total_rounds = 3 #Best 2 out of 3

    options = ["Rock", "Paper", "Scissors"]
#game logic
    while round <= total_rounds and (score["bot score"] < 2 and score["user score"] < 2):
        #Func counts the rounds and also the scores per round
        user_choice = input("Choose Rock, Paper, or Scissors: ").strip().title()
        computer_choice = random.choice(options)
        print("You chose:", user_choice)
        print("Computer chose:", computer_choice)

        if user_choice == computer_choice:
            print (f"Round {round}")
            print("It's a tie!")
            score["user score"] += 1 #Score counter
            score["bot score"] += 1
            print(score)
        
        elif (user_choice == "Rock" and computer_choice == "Scissors") or (user_choice == "Paper" and computer_choice == "Rock") or (user_choice == "Scissors" and computer_choice == "Paper"):
            print (f"Round {round}")
            print("You win!")
            score["user score"] += 1
            print(score)
            
        else:
            print (f"Round {round}")
            print("Computer wins!")
            score["bot score"] += 1
            print(score)

        round += 1 #Round counter

#this is the winning logic. If they tie 3 times the Func will auto restart until a winner is decided
    if score['bot score'] == 2 and score['user score'] < 2:
        print("Checkmate! Bot Wins")
    elif score['user score'] == 2 and score['bot score'] < 2:
        print("Checkmate! You Win")
    else:
        compare()

if __name__ == "__main__":
    compare()


