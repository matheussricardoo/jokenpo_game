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

# Possible user choices
lista = [rock, paper, scissors]

# Random computer choice
computador = random.choice(lista)

# User choice request
print("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.")
escolha = int(input())
print()

# Displays user and computer choice
print("Your choice:")
print(lista[escolha])
print("Computer's choice:")
print(computador)

# Game logic
if escolha == 0 and lista.index(computador) == 0:
    print("It's a draw!")
elif escolha == 1 and lista.index(computador) == 1:
    print("It's a draw!")
elif escolha == 2 and lista.index(computador) == 2:
    print("It's a draw!")
elif (escolha == 0 and lista.index(computador) == 2) or \
     (escolha == 1 and lista.index(computador) == 0) or \
     (escolha == 2 and lista.index(computador) == 1):
    print("You win!")
else:
    print("You lose!")
