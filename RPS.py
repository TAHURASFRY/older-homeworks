import random

items = ["ROCK","PAPER","SCISSOR","EXIT"]

computer_score = 0
user_score = 0

computer_choice = random.choice(items)

print("0-ROCK")
print("1-PAPER")
print("2-SCISSOR")
print("3-EXIT")

while True:
    user_choice_index = int(input())
    user_choice = items[user_choice_index]
    
    if user_choice == 3:
        break

    elif computer_choice == "ROCK" and user_choice == "SCISSOR":
        print("computer wins")
        computer_score +=1
        print(computer_choice)
        print(user_score, "USER")
        print(computer_score, "COMPUTER")
    elif computer_choice == "ROCK" and user_choice == "PAPER":
        print("user wins")
        user_score +=1
        print(computer_choice)
        print(user_score, "USER")
        print(computer_score, "COMPUTER")
    elif computer_choice == "ROCK" and user_choice == "ROCK":
        print("equal")
        print(computer_choice)
        print(user_score, "USER")
        print(computer_score, "COMPUTR")
    elif computer_choice == "PAPER" and user_choice == "ROCK":
        print("user wins")
        user_score +=1
        print(computer_choice)
        print(user_score, "USER")
        print(computer_score, "COMPUTER")
    elif computer_choice == "PAPER" and user_choice == "PAPER":
        print("equal") 
        print(computer_choice) 
        print(user_score, "USER")
        print(computer_score, "COMPUTER")
    elif computer_choice == "PAPER" and user_choice == "SCISSOR":
        print("computer wins")
        computer_score +=1
        print(computer_choice)
        print(user_score, "USER")
        print(computer_score, "COMPUTER")
    elif computer_choice == "SCISSOR" and user_choice == "ROCK":
        print("user wins")
        user_score +=1
        print(computer_choice)
        print(user_score, "USER")
        print(computer_score, "COMPUTER")
    elif computer_choice == "SCISSOR" and user_choice == "PAPER":
        print("computer wins")
        computer_score +=1
        print(computer_choice)
        print(user_score, "USER")
        print(computer_score, "COMPUTER")
    elif computer_choice == "SCISSOR" and user_choice == "SCISSOR":
        print("equal")
        print(computer_choice)
        print(user_score, "USER")
        print(computer_score, "COMPUTER")
