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
from random import randint

arr = [rock, paper, scissors]
selection = int(input("Enter 0 for rock, 1 for paper and 2 for scissiors: "))
print("\n\nPLayer's Move",arr[selection])
computer = randint(0,2)
print("\n\nComputer's Move",arr[computer])
print("\nResult: ", end="")
if (selection == 0 and computer == 1) or (selection == 1 and computer== 2) or (selection == 2 and computer==0):
    print("Computer WINS")
elif selection == computer:
    print("Draw")
else:
    print("Player WINS")



