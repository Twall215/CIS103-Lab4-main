import random #Needed so computer can make its own choice 

 

options = ["Rock", "Paper", "Scissors"] #List that the computer picks from

 

user_choice = input("Choose Rock, Paper, or Scissors: ")

computer_choice = random.choice(options)

 

print("You chose: ", user_choice)

print("Computer chose: ", computer_choice)

 
#Game logic
if user_choice == computer_choice:

    print("It's a tie!")

elif user_choice == "Rock" and computer_choice == "Scissors":

    print("You win!")

elif user_choice == "Paper" and computer_choice == "Rock":

    print("You win!")

elif user_choice == "Scissors" and computer_choice == "Paper":

    print("You win!")

else:

    print("Computer wins!")

