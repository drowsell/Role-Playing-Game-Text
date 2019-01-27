import time
import random
import game

def increase(weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow):
  if weapon == "sword":
    attack = attack + (level * 1.5)
    health = health + (level * 1.5)
    mana = mana + level
  elif weapon == "bow":
    attack = attack + (level * 1.75)
    health = health + (level * 1.25)
    mana = mana + (level * 1.5)
    arrow = arrow + 1
  elif weapon == "book":
    attack = attack + (level * 2)
    health = health + level
    mana = mana + (level * 2.5)
  else:
    attack = attack + (level * 1.1)
    health = health + (level * 2)
    mana = mana + (level * .25)
  return weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow
  
def detectEnemy(enemy):
  
  enemyAttackLrg = [7, 9, 10]
  enemyAttackMed = [4, 5, 6]
  enemyAttackSml = [3, 4, 5]
  enemyHealthLrg = [35, 40, 45]
  enemyHealthMed = [25, 30, 35]
  enemyHealthSml = [10, 15, 20]
  
  if enemy == "trogg" or enemy == "dwarf":
    enemyAttack = random.choice(enemyAttackSml)
    enemyHealth = random.choice(enemyHealthMed)
  elif enemy == "kobold" or enemy == "gnoll":
    enemyAttack = random.choice(enemyAttackMed)
    enemyHealth = random.choice(enemyHealthMed)
  elif enemy == "wolf":
    enemyAttack = random.choice(enemyAttackLrg)
    enemyHealth = random.choice(enemyHealthSml)
  elif enemy == "troll":
    enemyAttack = (2 * random.choice(enemyAttackMed))
    enemyHealth = (2 * random.choice(enemyHealthLrg))
  elif enemy == "archer":
    enemyAttack = (2 * random.choice(enemyAttackMed))
    enemyHealth = (2 * random.choice(enemyHealthMed))
  elif enemy == "theif" or enemy == "wizzard":
    enemyAttack = (2 * random.choice(enemyAttackLrg))
    enemyHealth = (2 * random.choice(enemyHealthSml))
  elif enemy == "ogre":
    enemyAttack = (2.5 * random.choice(enemyAttackMed))
    enemyHealth = (2.5 * random.choice(enemyHealthMed))
  elif enemy == "warlock":
    enemyAttack = (3 * random.choice(enemyAttackLrg))
    enemyHealth = (2 * random.choice(enemyHealthMed))
  elif enemy == "warrior" or enemy == "orc":
    enemyAttack = (2.5 * random.choice(enemyAttackMed))
    enemyHealth = (3.5 * random.choice(enemyHealthLrg))
  else:
    print("Error.")
  
  enemyAttack = int(enemyAttack)
    
  return enemyAttack, enemyHealth
  
def heal(weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow):
  
  beforeHealth = health

  if mana < 5:
    print("Not enough mana!")
    weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow = game.battle(weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow)
  else:  
    print("How much mana do you want to use to heal? : 5, 10, 25")
    healAmount = input().strip("!@#$%^&*()_+.").lower()
    if healAmount == "5":
      if mana >= 5:
        mana = mana - 5
        health = int(health + 10 + (0.10 * health))
        healAmount = health - beforeHealth
        print("You healed for " + str(healAmount) + ".")
      else:
        print("Not enough mana!")
    elif healAmount == "10":
      if mana >= 10:
        mana = mana - 10
        health = int(health + 20 + (0.20 * health))
        healAmount = health - beforeHealth
        print("You healed for "+ str(healAmount) + ".")
      else:
        print("Not enough mana!")  
    elif healAmount == "25":
      if mana >= 25:
        mana = mana - 25
        health = int(health + 50 + (0.50 * health))
        healAmount = health - beforeHealth
        print("You healed for " + str(healAmount) + ".")
      else:
        print("Not enough mana!")  
    else:
      weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow = heal(weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow)
  
  randomMultiplier = [0.5, 0.8, 0.85, 0.9, 0.95, 1, 1.05, 1.1, 2]
  
  game.loading()
  
  if enemyHealth > 0:
    enemyDamage = (enemyAttack * random.choice(randomMultiplier))
    enemyDamage = int(enemyDamage)
    print(enemy.capitalize() + " hits you for " + str(enemyDamage) + ".") 
    game.loading()
    health = health - enemyDamage
    weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow = game.battle(weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow)
  else:
    print(enemy.capitalize() + " falls.")
    game.loading()
  
    weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow = game.gainXp(weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow)
  
  weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow = game.battle(weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow)
  
  return weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow
  
def special(weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow):
  if weapon == "sword":
    if mana >= 5:
      print("You use sweeping strike for 5 mana!")
      mana = mana - 5
      
      randomMultiplier = [0.5, 0.8, 0.85, 0.9, 0.95, 1, 1.05, 1.1, 2]
      randomMultiplierSpecial = [1.5, 1.8, 2]
      
      
      weaponDamage = (attack * random.choice(randomMultiplierSpecial))
      weaponDamage = int(weaponDamage)
      enemyHealth = enemyHealth - weaponDamage
      
      game.loading()
      
      print("You hit " + str(enemy) + " for " + str(weaponDamage) + ".")
      
      game.loading()
      
      attack = attack + (2 * level)
      print("Your attack has increased by " + str(2 * level) + ".")
      
      game.loading()
      
      if enemyHealth > 0:
        enemyDamage = (enemyAttack * random.choice(randomMultiplier))
        enemyDamage = int(enemyDamage)
        print(enemy.capitalize() + " hits you for " + str(enemyDamage) + ".") 
        game.loading()
        health = health - enemyDamage
        weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow = game.battle(weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow)
      else:
        print(enemy.capitalize() + " falls.")
        game.loading()
      
        weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow = game.gainXp(weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow)
          
        
    else:
      game.loading()
      print("You need at least 5 mana!")
      game.loading()
      weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow = game.battle(weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow)
  
  elif weapon == "book":
    
    if mana >= 10:
      print("You cast fireball for 10 mana!")
      mana = mana - 10
      
      randomMultiplier = [0.5, 0.6]
      randomMultiplierSpecial = [2, 2.5]
      
      print("You attack the " + str(enemy) + ".")
      
      weaponDamage = (attack * random.choice(randomMultiplierSpecial))
      weaponDamage = int(weaponDamage)
      enemyHealth = enemyHealth - weaponDamage
      
      game.loading()
      
      print("You hit " + str(enemy) + " for " + str(weaponDamage) + ".")
      
      game.loading()
      
      mana = mana + level
      
      print("You gained " + str(level) + " mana.")
      
      game.loading()
      
      if enemyHealth > 0:
        enemyDamage = (enemyAttack * random.choice(randomMultiplier))
        enemyDamage = int(enemyDamage)
        print(enemy.capitalize() + " is momentarily weakened and hits you for " + str(enemyDamage) + ".") 
        game.loading()
        health = health - enemyDamage
        weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow = game.battle(weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow)
      else:
        print(enemy.capitalize() + " falls.")
        game.loading()
        weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow = game.gainXp(weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow)
          
    else:
      game.loading()
      print("You need at least 10 mana!") 
      game.loading()
      weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow = game.battle(weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow)
          
  elif weapon == "bow":
    if arrow >= 1:
      print("You fire an arrow at the " + str(enemy) + "!")
      arrow = arrow - 1
      
      randomMultiplier = [0.5, 0.6]
      randomMultiplierSpecial = [0.5, 0.8, 0.85, 0.9, 0.95, 1, 1.05, 1.1, 2]
      
      weaponDamage = (attack * random.choice(randomMultiplierSpecial))
      weaponDamage = int(weaponDamage)
      enemyHealth = enemyHealth - weaponDamage
      
      game.loading()
      
      print("You hit " + str(enemy) + " for " + str(weaponDamage) + ".")
      
      game.loading()
      
      if enemyHealth > 0:
        
        print(enemy.capitalize() + " is too far away to hit you!") 
        
        game.loading()
        
        weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow = game.battle(weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow)
      else:
        print(enemy.capitalize() + " falls.")
        game.loading()
        weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow = game.gainXp(weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow)
          
    else:
      game.loading()
      print("You need at least 1 arrow!") 
      game.loading()
      weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow = game.battle(weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow)
  else:
    game.loading()
    print("You do not have a weapon!")
    game.loading()
    weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow = game.battle(weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow)
      
  return weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  