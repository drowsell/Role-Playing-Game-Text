# A Walk in the Woods - RPG
# Authour: Dylan Rowsell
# Date: January 18, 2018

# The user goes on a journy fighting monsters. The user can choose a unique weapon which gives them a special ability, fights randomized enemies, gains experience, and is able to heal. See if you can win! It's possible with all 3 weapons. I don't know if it's possible without a weapon though...

# importing other pages with defs on them
import game
import gamestats

# importing modules
import random
import time

# Defining game stats for player.

health = 25
mana = 25
attack = 8
weapon = "null"
enemy = "null"
enemyAttack = 1
enemyHealth = 1
enemyXP = 0
xp = 0
level = 1
arrow = 1
  
# This is just a def that makes it look like the game is loading.  
game.loading()

print("You awake in a dark cave. You crawl around the space looking for light.")

game.loading()

print("There are three objects lying on the floor. A sword, bow, and book. They glow dimly.")

game.loading()

print("Do you wish to pick one up?")

game.loading()

# The player chooses their weapon.

weapon = game.weaponYesNo(weapon)

game.loading()

print("The other objects suddenly turn into dust!")

game.loading()

print("After much searching, you find the entrance and leave the cave.")

game.loading()

print("What's that in the distance?")

game.loading()

# Assigning enemies in lists. Names matter. 
# These are used in the loops below. 

enemyWeak = ["trogg", "gnoll", "kobold", "wolf", "dwarf"]
enemyMed = ["troll", "archer", "theif", "wizzard"]
enemyLrg = ["orc", "ogre", "warlock", "warrior"]
weakEnemyList = [random.choice(enemyWeak), random.choice(enemyWeak), random.choice(enemyWeak)]
medEnemyList = [random.choice(enemyMed), random.choice(enemyMed), random.choice(enemyMed)]
lrgEnemyList = [random.choice(enemyLrg), random.choice(enemyMed), random.choice(enemyLrg)]

# Initial stat boost to palyer. 
weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow = gamestats.increase(weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow)


# loop 3 times (a random enemy from enemyWeak)
for enemy in weakEnemyList:
  
  if health > 0:
  
    print("A wild " + enemy + " appears!")
    
    game.loading()
    
    weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow = game.fight(weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow)
    
    game.loading()
    
  else:
    print("...")
    time.sleep(.2)

# Player can gain stats depending on how they answer.
if health > 0:
    
  game.loading()

  print("You are bruised from battle, but you feel like you have become stronger. Should you stop to rest?")
  
  game.loading()
  

    
  # Actual stat boost
  weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow = game.rest(weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow)

  game.loading()
  
  print("You remind yourself to save your mana for the road ahead.")
   
  game.loading()  
    
else:
  print("...")
  time.sleep(2)

# loop 3 times (a random enemy from enemyMed)
for enemy in medEnemyList:

  if health > 0:
    
    print("A wild " + enemy + " appears!")
    
    game.loading()
    
    weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow = game.fight(weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow)
    
    game.loading()
    
  else:
    print(" ")
    time.sleep(.2)

# Another stat boost if the player is still alive.
if health > 0:
    
  game.loading()

  print("Finally you have a break from all that fighting!")

  game.loading()
  
  print("Your path becomes harder to follow as you enter the forest.")
  
  game.loading()

  print("A hooded man offers you a drink. Do you accept?")
    
    # Player has the chance for a stat boost
  weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow = game.rest(weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow)

  game.loading()

# loop 3 times (a random enemy from enemyLrg)    
for enemy in lrgEnemyList:

  if health > 0:
    print("A wild " + enemy + " appears!")
    
    game.loading()
    
    weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow = game.fight(weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow)
  else:
    print(" ")
    time.sleep(.2)

# if the player is still alive congradulate them!
if health > 0:
  print("Congradulations! You've won!")
  
  game.loading()
  
  print("Your final stats :")
  time.sleep(.5)
  print(" Health : " + str(int(health)))
  print(" Mana : " + str(int(mana)))
  print(" Level : " + str(level)) 
  print(" ")

# The place where players go to die...  
else:
  print("You died.")
  print("Your final stats :")
  time.sleep(.5)
  print(" Health : " + str(int(health)))
  print(" Mana : " + str(int(mana)))
  print(" Level : " + str(level)) 
  print(" ")


