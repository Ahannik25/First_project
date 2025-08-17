import random

print("Welcome to the Terminal Adventure Game!")
print("You wake up in a dark forest. Two paths stretch before you...\n")

game_over = False
hp = 10

while not game_over:
    print("Your HP:", hp)
    print("Where do you want to go?")
    print("1. Explore the cave")
    print("2. Walk down the river")
    print("3. Rest under a tree")
    choice = input("> ")
    
    if choice == "1":
        print("\nYou enter a cave...")
        if random.randint(1, 2) == 1:
            print("A wild goblin attacks!")
            damage = random.randint(1, 5)
            hp -= damage
            print(f"The goblin hits you for {damage} damage!")
        else:
            print("You find a chest with +3 HP!")
            hp += 3

    elif choice == "2":
        print("\nYou follow the river...")
        if random.randint(1, 2) == 1:
            print("You slip on a rock and lose 2 HP.")
            hp -= 2
        else:
            print("You catch a fish and eat it. +2 HP.")
            hp += 2

    elif choice == "3":
        print("\nYou rest under the tree...")
        if random.randint(1, 2) == 1:
            print("A snake bites you! -3 HP.")
            hp -= 3
        else:
            print("You feel refreshed. +1 HP.")
            hp += 1

    else:
        print("Invalid choice, try again.")
        
        
    # check win/lose conditions
    if hp <= 0:
        print("\nYou collapse... Game Over!")
        game_over = True
    elif hp >= 20:
        print("\nYou feel stronger than ever and escape the forest! You win!")
        game_over = True
    else:
        print("\n--- Next Turn ---\n")
        
