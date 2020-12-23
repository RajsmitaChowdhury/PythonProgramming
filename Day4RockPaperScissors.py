import random
rock = '''
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
computer = random.randint(0,2)
you = int(input("Please enter your choice. Type 0 for rock, 1 for paper and 2 for scissors."))
if you == 0:
    if computer==1:
        print(f"You chose \n{rock}")
        print(f"Computer chose \n{paper}")
        print("You lose!")
    elif computer == 2:
        print(f"You chose \n{rock}")
        print(f"Computer chose \n{scissors}")
        print("You win!")
    else:
        print(f"You chose \n{rock}")
        print(f"Computer chose \n{rock}")
        print("It's a tie!")
elif you == 1:
    if computer == 0:
        print(f"You chose \n{paper}")
        print(f"Computer chose \n{rock}")
        print("You win!")
    elif computer == 1:
        print(f"You chose \n{paper}")
        print(f"Computer chose \n{paper}")
        print("It's a tie!")
    else:
        print(f"You chose \n{paper}")
        print(f"Computer chose \n{scissors}")
        print("You lose!")
else:
    if computer == 0:
        print(f"You chose \n{scissors}")
        print(f"Computer chose \n{rock}")
        print("You lose!")
    elif computer == 1:
        print(f"You chose \n{scissors}")
        print(f"Computer chose \n{paper}")
        print("You win!")
    else:
        print(f"You chose \n{scissors}")
        print(f"Computer chose \n{scissors}")
        print("It's a tie!")

