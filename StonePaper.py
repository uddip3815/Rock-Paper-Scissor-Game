import random as rd
a = rd.randint(1, 3)
print("Computer's Turn: ")
if a==1:
    comp = "Rock"
elif a==2:
    comp = "Paper"
elif a==3:
    comp = "Scissor"
me = input("Your Turn: ")
if me=="Stone":
    if comp=="Rock":
        print("Tie!")
    elif comp=="Paper":
        print("You Lose!")
    elif comp=="Scissor":
        print("You Won!")
elif me=="Paper":
    if comp=="Rock":
        print("You Won!")
    elif comp=="Paper":
        print("Tie!")
    elif comp=="Scissor":
        print("You Lose!")
elif me=="Scissor":
    if comp=="Rock":
        print("You Lose!")
    elif comp=="Paper":
        print("You Won!")
    elif comp=="Scissor":
        print("Tie!")
print(f"You Choose {me}")
print(f"Computer Choose {comp}")
