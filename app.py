# Write a program to simulate a game of rolling dice between two players and to print who is the winner

import random

print("Welcome to Dice Game")

# Player 1
player1 = input("Enter Player 1 name: ")
p1=0

# Player 2
player2 = input("Enter Player 2 name: ")
p2=0

print("Player 1 is: ", player1)
print("Player 2 is: ", player2)

# Roll the dice
print("Rolling the dice...")
print("The values are....")

for i in range(5):
    r1 = random.randint(1, 6)
    r2 = random.randint(1, 6)

    print(f"Step {i+1}")
    if(r1>r2):
        p1+=1
        print(f"{player1} won the round with total points {p1} and a dice value of {r1}")
    elif (r2>r1):
        p2+=1
        print(f"{player2} won the round with total points {p2} and a dice value of {r2}")
    else:
        print("Draw")
    
if(p1>p2):
    print(f"{player1} won the game with {p1} points")
elif(p2>p1):
    print(f"{player2} won the game with {p2} points")