

def compare():#The game itself
    import random
    score = { #Stores the score for the tally
        "user score" : 0,
        "bot score" : 0
    }

    options = ["Rock", "Paper", "Scissors"]
    user_choice = input("Choose Rock, Paper, or Scissors: ")
    user_choice = user_choice.strip().title()#Capitalizes the first letter of each word and eliminates spaces
    computer_choice = random.choice(options)#Randomize choices
    print("You chose: ", user_choice)
    print("Computer chose: ", computer_choice)
    
    if user_choice == computer_choice:
        print("It's a tie!")
        score["user score"] +=1
        score["bot score"] +=1
        print(score)
        
    elif user_choice == "Rock" and computer_choice == "Scissors":
        print("You win!")
        score["user score"] +=1
        print(score)
        
    elif user_choice == "Paper" and computer_choice == "Rock":
        print("You win!")
        score["user score"] +=1
        print(score)
        
    elif user_choice == "Scissors" and computer_choice == "Paper":
        print("You win!")
        score["user score"] +=1
        print(score)
        
    else:
        print("Computer wins!")
        print(score)
        score["bot score"] +=1      
    
    
        while score["bot score"] < 2 and score["user score"] < 2:
           result = compare()
           print(result)
           
        if result == "You win!":
                score["user score"] +=1
                print(score)
        elif result == "Computer wins!":
            score["bot score"] +=1
            print(score)
        elif result == "It's a tie!":
            score["bot score"]+=1
            score["user score"]+=1
            print(score)
        if score["bot score"] == 2 and score["user score"] < 2:
            print("Checkmate! Bot Wins")
            print(score)    
        elif score["user score"] == 2 and score["bot score"] < 2:
            print("Checkmate! You Win")
            print(score)
       
if __name__ == "__main__":
        compare()
    


