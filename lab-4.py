import random #Needed so computer can make its own choice 

def compare():
    #Choice starts it off
    choice = str(input("Choose 1. 1Player or 2. 2Player: "))
    
    if choice == "1":
    #tallys the score and holds in storage until the game is complete
        score = {
            "user score": 0,
            "bot score": 0
        }
        round = 1 #starts off the round counter
        total_rounds = 3 #Best 2 out of 3

        options = ["Rock", "Paper", "Scissors"]
    #game logic for player vs. com
        while round <= total_rounds and (score["bot score"] < 2 and score["user score"] < 2):
            #Func counts the rounds and also the scores per round
            user_choice = input("Choose: Rock, Paper, or Scissors: ").strip().title()
            computer_choice = random.choice(options)
            print("You chose:", user_choice)
            print("Computer chose:", computer_choice)

        # Invalid choice if user choice is not an option
            if user_choice not in options:
                print("Invalid choice! Please choose Rock, Paper, or Scissors.")
                continue
        
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

#this is the winning logic. If they tie 3 times the Func will end
        if score['bot score'] == 2 and score['user score'] < 2:
            print("Checkmate! Bot Wins")
        elif score['user score'] == 2 and score['bot score'] < 2:
            print("Checkmate! You Win")
        else:
            compare()

#2player game logic
    if choice == "2":
    #Adding a two player score tally
        scorefor2player = {
            "player 1 score": 0,
            "player 2 score": 0
        }
        round = 1 #starts off the round counter
        total_rounds = 3 #Best 2 out of 3

        options = ["Rock", "Paper", "Scissors"]
    #game logic for player vs. player
        while round <= total_rounds and (scorefor2player["player 1 score"] < 2 and scorefor2player["player 2 score"] < 2):
            #Func counts the rounds and also the scores per round
            user_choice = input("Player 1 Choose: Rock, Paper, or Scissors: ").strip().title()
            user2_choice = input("Player 2 Choose: Rock, Paper, or Scissors: ").strip().title()
            print("Player 1 chose:", user_choice)
            print("Player 2 chose:", user2_choice)

        # Invalid choice if users choice is not an option
            if user_choice not in options:
                print("Invalid choice! Please choose Rock, Paper, or Scissors.")
                continue
            if user2_choice not in options:
                print("Invalid choice! Please choose Rock, Paper, or Scissors.")
                continue

            if user_choice == user2_choice:
                print (f"Round {round}")
                print("It's a tie!")
                scorefor2player["player 1 score"] += 1 #Score counter
                scorefor2player["player 2 score"] += 1
                print(scorefor2player)
        
            elif (user_choice == "Rock" and user2_choice == "Scissors") or (user_choice == "Paper" and user2_choice == "Rock") or (user_choice == "Scissors" and user2_choice == "Paper"):
                print (f"Round {round}")
                print("Player 1 wins!")
                scorefor2player["player 1 score"] += 1
                print(scorefor2player)
            
            else:
                print (f"Round {round}")
                print("Player 2 wins!")
                scorefor2player["player 2 score"] += 1
                print(scorefor2player)

            round += 1 #Round counter

    #this is the winning logic. If they tie 3 times the Func will end
        if scorefor2player["player 2 score"] == 2 and scorefor2player["player 1 score"] < 2:
            print("Checkmate! Player 2 Wins")
        elif scorefor2player["player 1 score"] == 2 and scorefor2player["player 2 score"] < 2:
            print("Checkmate! Player 1 Win")
        else:
            compare()

if __name__ == "__main__":
    compare()

