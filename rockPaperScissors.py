
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
# Obtain gamer decision
gamer_decison = input("Type rock, paper, pr scissors choice: \n")
gamer_decison = gamer_decison.lower()
# Computer decision
gametypes = [rock, paper, scissors]
computer_decis = random.randint(0,2)
if gamer_decison == "rock":
    print("Gamer Decision: \n")
    print(rock)
    print("\n")  
elif gamer_decison == "paper":
    print("Gamer Decision: \n")
    print(paper)
    print("\n")  
elif gamer_decison == "scissors":
    print("Gamer Decision: \n")
    print(scissors)   
    print("\n")     
    

if computer_decis == 0:
    print("Computer Decision: \n")
    print(gametypes[0])
elif computer_decis == 1:
    print("Computer Decision: \n")
    print(gametypes[1])
elif computer_decis == 2:
    print("Computer Decision: \n")
    print(gametypes[2])     
if computer_decis == 0 and gamer_decison == "rock":
    print("Both rocks, draw!")  
elif computer_decis == 0 and gamer_decison == "paper":
    print("Paper wins against rock.")
elif computer_decis == 0 and gamer_decison == "scissors":
    print("Rock wins against scissors.")   
elif computer_decis == 1 and gamer_decison == "rock":
    print("Paper wins against rock.")  
elif computer_decis == 1 and gamer_decison == "paper":
    print("Both paper, draw!")
elif computer_decis == 1 and gamer_decison == "scissors":
    print("Scissors win against paper.") 
elif computer_decis == 2 and gamer_decison == "rock":
    print("Rock wins against scissors.")  
elif computer_decis == 2 and gamer_decison == "paper":
    print("Scissors win against paper.")
elif computer_decis == 2 and gamer_decison == "scissors":
    print("Both scissors, draw!") 