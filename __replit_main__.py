# Role Playing Game
# Authour: Dylan Rowsell
# Date: January 18, 2018

import game
import gamestats
import random

health = 40
mana = 40
attack = 8
weapon = "null"
enemy = "null"
enemyAttack = 1
enemyHealth = 1
enemyXP = 0
xp = 0
  
#game.loading()

print("You awake in a dark room.")

#game.loading()

print("There are three objects lying on the floor. A sword, bow, and book.")

#game.loading()

print("Do you wish to pick them up?")

weapon = game.weaponYesNo(weapon)



print("The other objects suddenly turn into dust!")

game.loading()

print("You leave the cave.")

game.loading()

enemyWeak = ["trogg", "gnoll", "kobold", "wolf", "dwarf"]
enemyMed = ["troll", "archer", "theif", "wizzard"]
weakEnemyList = [random.choice(enemyWeak), random.choice(enemyWeak), random.choice(enemyWeak)]
medEnemyList = [random.choice(enemyMed), random.choice(enemyMed), random.choice(enemyMed)]
# Initial stat boost
weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp = gamestats.increase(weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp)

for enemy in weakEnemyList:

  print("A wild " + enemy + " appears!")
  
  weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp = game.fight(weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp)

for enemy in medEnemyList:

  print("A wild " + enemy + " appears!")
  
  weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp = game.fight(weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp)
  
print("Wow, much impressed.")

