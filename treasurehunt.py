choicea = input('You\'re at a cross road after leaving a wooded area.  Looking down you see a small key.  Do you pick it up or leave?  Type "pick up" or "leave it" \n').lower()
if choicea == "pick up":
    keygot = True
elif choicea == "leave it": 
    keygot = False
choice1 = input('You\'re still at the cross road. Where do you want to go? Type "left" or "right" \n').lower()
if choice1 == "left":
  choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
  if choice2 == "wait":
    choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
    if choice3 == "red":
      print("It's a room full of fire. Game Over.")
    elif choice3 == "yellow":
      print("You found the treasure! But it\'s locked....Do you have the key?\n")
      choice4 = input("Do you have the key to unlock the chest?  Type yes or no\n").lower()
      if choice4 == "no":
          print("...Ok so what now...?")
          choice5 = input("So are you going to give up or force the lock? \nType 'give up' or 'force lock'\n").lower()
          if choice5 == "force lock":
              print("Bang!  \nThe chest just blew up!!! \nGame Over!!!")
          elif choice4 == "give up":
              print("You go home empty handed after all that! \nGame Over!!!")
      else:
          if keygot == True:
                print("Ok unlocking the box, yep you've got the treasure!")    
          else: 
                print("Oh dear you dont have the key.....")    
                choice6 = input("So are you going to give up or force the lock? Type 'give up' or 'force lock'").lower()
                if choice6 == "force lock":
                    print("Bang!  \nThe chest just blew up!!! \nGame Over!!!")
                elif choice6 == "give up":
                    print("You go home empty handed after all that! \nGame Over!!!")
    elif choice3 == "blue":
      print("You enter a room of beasts. Game Over.")
    else:
      print("You chose a door that doesn't exist. Game Over.")
  else:
    print("You get attacked by an angry trout. Game Over.")
else:
  print("You fell into a hole. Game Over.")