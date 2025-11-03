# Monster Battle Arena Game by Mohmmad Nour

import random

print("================================")
print("MONSTER BATTLE ARENA")
print("================================")
print("Let the battle begin!")
print("\n\n")

while True:
    rounds = int(input("Enter number of rounds to fight (3-10): "))
    if 3 <= rounds <= 10:
        break
    else:
        print("Please enter a valid number between 3 and 10.")

player_health = 100
monster_health = 100

for round_number in range(1, rounds + 1):
    if player_health == 0 or monster_health == 0:
        break

    print("--------------- Round", round_number, "---------------")
    print("Your HP:", player_health, "| Monster HP:", monster_health)
    print("Make your move:\n")
    print("1. Attack")
    print("2. Defend")
    print("3. Heal")

    player_choice = int(input("Enter your choice (1-3): "))
    while player_choice < 1 or player_choice > 3:
        print("Invalid, please pick a number between 1 and 3!")
        player_choice = int(input("Enter your choice (1-3): "))

    monster_choice = random.randint(1, 3)
    print()

    player_damage = 0
    monster_damage = 0
    player_heal = 0
    monster_heal = 0

    if player_choice == 1:
        print("You chose ATTACK. Go for it!")
    elif player_choice == 2:
        print("You chose DEFEND. Shield up!")
    else:
        print("You chose HEAL. Patch yourself up.")

    if monster_choice == 1:
        print("Monster chose ATTACK.")
    elif monster_choice == 2:
        print("Monster chose DEFEND.")
    else:
        print("Monster chose HEAL.")

    if player_choice == 1:
        player_damage = random.randint(8, 15)
    if player_choice == 3:
        player_heal = random.randint(5, 12)

    if monster_choice == 1:
        monster_damage = random.randint(8, 15)
    if monster_choice == 3:
        monster_heal = random.randint(5, 12)

    if player_choice == 2 and monster_damage > 0:
        monster_damage = monster_damage // 2
        print("You defended. Incoming damage reduced.")
    if monster_choice == 2 and player_damage > 0:
        player_damage = player_damage // 2
        print("Monster defended. Your damage reduced.")

    if player_damage > 0:
        monster_health = monster_health - player_damage
        if monster_health < 0:
            monster_health = 0
        if player_damage >= 14:
            print("You dealt", player_damage, "damage. BIG HIT!")
        else:
            print("You dealt", player_damage, "damage.")
    if monster_damage > 0:
        player_health = player_health - monster_damage
        if player_health < 0:
            player_health = 0
        if monster_damage >= 14:
            print("Monster dealt", monster_damage, "damage. Ouch!")
        else:
            print("Monster dealt", monster_damage, "damage.")

    if player_heal > 0:
        player_health = player_health + player_heal
        if player_health > 100:
            player_health = 100
        if player_heal >= 10:
            print("You healed", player_heal, "HP. Clean heal! Current HP:", player_health)
        else:
            print("You healed", player_heal, "HP. Current HP:", player_health)
    if monster_heal > 0:
        monster_health = monster_health + monster_heal
        if monster_health > 100:
            monster_health = 100
        if monster_heal >= 10:
            print("Monster healed", monster_heal, "HP. Monster HP:", monster_health)
        else:
            print("Monster healed", monster_heal, "HP. Monster HP:", monster_health)

    if player_health > monster_health:
        print("Status: You're ahead. Keep pressure!")
    elif player_health < monster_health:
        print("Status: Behind. Play smart!")
    else:
        print("Status: Even. Anyone's game!")

    print("End of round -> Your HP:", player_health, " | Monster HP:", monster_health)

    if player_health == 0 or monster_health == 0:
        break

print("\n================================")
print("BATTLE OVER!")
print("Your HP:", player_health)
print("Monster HP:", monster_health)
if player_health > monster_health:
    print("You WIN!")
elif player_health < monster_health:
    print("Monster WINS!")
else:
    print("It's a DRAW!")
