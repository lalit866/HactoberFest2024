import random 
char = input("Pick rock , paper or scissor :")
list = ["rock","paper","scissor"]
comp = random.choice(list)
print("Computer selects",comp)
if char == comp :
    print("Both picked ",char,"so it's a draw.")
elif char == "rock":
    if comp == "scissor":
        print("You won as rock beats scissor.")
    elif comp == "paper" :
        print("You lost as paper beats rock.")
elif char == "paper":
    if comp == "scissor":
        print("You lost as scissor beats paper.")
    elif comp == "rock" :
        print("You won as paper beats rock.")
elif char == "scissor":
    if comp == "paper":
        print("You won as scissor beats paper.")
    elif comp == "rock" :
        print("You lost as rock beats scissor.")
else :
    print("ERROR!!")
