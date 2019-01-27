import time
import random
import gamestats


def loading():
  print(" ")
  time.sleep(.5)
  for i in range(3):
    print("...")
    time.sleep(.2)
  time.sleep(.5)
  print(" ")
  
def weaponYesNo(weapon):

  weapon = "null"
  time.sleep(.5)
  print("Yes/No?")

  weaponAnswer = input().strip("!@#$%^&*()_+.").lower()

  if weaponAnswer == "yes":
    print("Which will you choose?")
    weapon = weaponChoice(weapon)
  elif weaponAnswer == "no":
    weapon = "unarmed"
  else:
    weapon = weaponYesNo(weapon)
  
  return weapon
    
def weaponChoice(weapon):
  weapon = input().strip("!@#$%^&*()_+.").lower()
  if weapon == "sword" or weapon == "bow" or weapon == "book":
      print("You pick up the " + weapon + ".") 
  else:
    print("Which object will you choose? : Sword, Bow, or Book?")
    weapon = weaponChoice(weapon)
  return weapon
  
def fight(weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow):
  
  if health > 0:
    print("Fight or run?")
    
    fightAnswer = input().strip("!@#$%^&*()_+.").lower()
    
    loading()
    
    enemyAttack, enemyHealth = gamestats.detectEnemy(enemy)
    enemyXP = (enemyHealth + enemyAttack) / 4
    
    if fightAnswer == "fight":
      weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow = battle(weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow)
      
    elif fightAnswer == "run":
      enemyAttack, enemyHealth = gamestats.detectEnemy(enemy)
      print("You receive " + str(2 * enemyAttack) + " damage as you run away.")
      health = (health - (2 * (enemyAttack)))
  
    else:
      weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow = fight(weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow)
  else:
    print(...)
    time.sleep(.2)
    
  return weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow

def battle(weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow):
  
  if health > 0 and enemyHealth > 0:
  
    print("Your stats :")
    time.sleep(.5)
    print(" Health : " + str(int(health)))
    print(" Mana : " + str(int(mana)))
    if weapon == "bow":
      print(" Arrows : " + str(arrow))
    else:
      arrow = 1
    print(" Level : " + str(level)) 
    print(" " + enemy.capitalize() + "'s Health : " + str(int(enemyHealth)))
    print(" ")
    print("What will you do? : Attack, Special, Heal, or Run?")
    
    battleAnswer = input().strip("!@#$%^&*()_+.").lower()
    
    if battleAnswer == "attack":
      weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow = attackBattle(weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow)
    
    if battleAnswer == "special":
      weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow = gamestats.special(weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow)
      
    elif battleAnswer == "heal":
      weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow = gamestats.heal(weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow)
    elif battleAnswer == "run":
      enemyAttack, enemyHealth = gamestats.detectEnemy(enemy)
      print("You receive " + str(enemyAttack) + " damage as you run away.")
      health = (health - (2 * (enemyAttack/enemyHealth)))
    else:
      weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow = battle(weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow)
  
  else:
    print("...")
    time.sleep(.2)
    
  return weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow

def attackBattle(weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow):

  randomMultiplier = [0.5, 0.8, 0.85, 0.9, 0.95, 1, 1.05, 1.1, 2]
  
  print("You attack the " + str(enemy) + ".")
  
  weaponDamage = (attack * random.choice(randomMultiplier))
  weaponDamage = int(weaponDamage)
  enemyHealth = enemyHealth - weaponDamage
  
  loading()
  
  print("You hit " + str(enemy) + " for " + str(weaponDamage) + ".")
  
  loading()
  
  if enemyHealth > 0:
    enemyDamage = (enemyAttack * random.choice(randomMultiplier))
    enemyDamage = int(enemyDamage)
    print(enemy.capitalize() + " hits you for " + str(enemyDamage) + ".") 
    loading()
    health = health - enemyDamage
    weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow = battle(weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow)
  else:
    print(enemy.capitalize() + " falls.")
    loading()
  
    weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow = gainXp(weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow)

  return weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow
    
def gainXp(weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow):
  newXpInt = int(enemyXP)
  newXpStr = str(newXpInt)
  print("You gained, " + newXpStr + " experience!")
  
  xp = xp + enemyXP
  
  if xp >= 20:
    if weapon == "bow":
      arrow = arrow + 1
    else:
      print(" ")
    
    xp = xp - (20 + (level * 4))
    weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow = gamestats.increase(weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow)
    level = level + 1
    print("Ding! You've reached level " + str(level)+ "!")
    if weapon == "sword"or weapon == "unarmed":
      mana = mana + 10
    elif weapon == "bow":
      mana = mana + 5
    elif weapon == "book":
      mana = mana + 20
    else:
      mana = mana + 10
    #weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow = gainXp(weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow)
    #weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow = battle(weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow)
  else:
    xpToGo = 20 - xp
    print("Only " + str(xpToGo) + " experience until your next level!")
    #weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow = battle(weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow)
    
  
  return weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow
  
def rest(weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow):
  print("Yes/No?")
  restAnswer = input().strip("!@#$%^&*()_+.").lower()
  if restAnswer == "yes":
    loading()
    print("You grow stronger.")
    weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow = gamestats.increase(weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow)
  elif restAnswer == "no":
    loading()
    print("You, move forward.")
    attack = attack + 3
  else:
    weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow = rest(weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow)
    
  return weapon, health, mana, attack, enemy, enemyAttack, enemyHealth, enemyXP, xp, level, arrow
  
  