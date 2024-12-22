import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
images = [rock,paper,scissor]
user_choice = int(input("Choose one of the following  options, 0 for Rock, 1 for Paper and 2 for Scissors. \n"))
print(images[user_choice])

computer_choise = random.randint(0,2)

print("Computer choose:")
print(images[computer_choise])

if user_choice >= 3 or user_choice < 0:
    print("The number is invalid. You lose!")
elif user_choice == 0 and computer_choise == 2:
    print("Yuou win")
elif computer_choise == 0 and user_choice==2:
    print("You lose")
elif computer_choise > user_choice:
    print("You lose")
elif user_choice > computer_choise:
    print("you win")
elif computer_choise == user_choice:
    print("The game is tie")
