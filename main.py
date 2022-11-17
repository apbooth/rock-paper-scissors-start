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

#Write your code below this line 👇
import random

player_choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if player_choose == 0:
    player = rock
elif player_choose == 1:
    player = paper
elif player_choose == 2:
    player = scissors

computer_choice = random.randint(0, 2)

if computer_choice == 0:
    cpu = rock
elif computer_choice == 1:
    cpu = paper
elif computer_choice == 2:
    cpu = scissors

#determine winner

if player_choose >= 3:
    player = "Invalid choice"
    game = "CPU wins!"
elif computer_choice == 0 and player_choose == 2:
    game = "CPU wins!"
elif computer_choice == player_choose:
    game ="It's a draw"
elif computer_choice == 0 and player_choose == 1:
    game = "Player wins!"
    
elif computer_choice == 1 and player_choose == 0:
    game = "CPU wins"
elif computer_choice == 1 and player_choose == 2:
    game = "Player wins!"

elif computer_choice == 2 and player_choose == 0:
    game = "Player wins"
elif computer_choice == 2 and player_choose == 1:
    game = "CPU wins!"

print(player)
print(cpu)
print(game)