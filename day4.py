import random
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
game_tools =[rock, paper, scissors]
# Player
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if player_choice >= 3 or player_choice < 0: 
  print("You typed an invalid number, you lose! try again!")
else:
  print(game_tools[player_choice])
  # Computer
  computer_choice = random.randint(0, 2)
  print("Computer Choice:")
  print(game_tools[computer_choice])

#game starts
  if player_choice == computer_choice:
    print("It's a tie!")
  elif player_choice == 0 and computer_choice == 2:
    print("Rock smashes scissors! You win!")
  elif player_choice == 0 and computer_choice == 1:
    print("Paper covers rock! You lose.")
  elif player_choice == 1 and computer_choice == 0:
    print("Paper covers rock! You win!")
  elif player_choice == 1 and computer_choice == 2:
    print("Scissors cuts paper! You lose.")
  elif player_choice == 2 and computer_choice == 1:
    print("Scissors cuts paper! You win!")
  elif player_choice == 2 and computer_choice == 0:
    print("Rock smashes scissors! You lose.")
