from lesson10 import Heroes
from random import randint
from math import floor

def activity(strg):
    try:
        int(strg)
        if (int(strg) >=1 and int(strg)<=2):
            return int(strg)
    except ValueError:
        print("Entered data isn't int")


hero = Heroes.Hero(name = input("Please, enter a Hero name"))
print("Hero "+hero.name+" is ready to fight")
heroInfo = hero.get_info()
print("")

dragon = Heroes.Dragon()
print("Dragon "+dragon.name+" is ready to fight")
dragonInfo = dragon.get_info()
print("")

move_pool = {1: 'Attack', 2: "Defence"}
roundCounter = 1

while not (hero.health <= 0 or dragon.health <= 0):
    print("Round "+str(roundCounter)+"!!!")
    print("Please, enter \'1\' if you want to attack or \'2\' if you want to defence")
    heroActivity = activity(input())
    while heroActivity == None:
        print("Please, enter correct number for activity: ")
        heroActivity = activity(input())
    print('Hero choose: '+move_pool[heroActivity])
    dragonActivity = activity(randint(1, 2))
    print('Dragon choose: ' + move_pool[dragonActivity])

###########   1. when Hero and Dragon choose attack      ###############################
    if heroActivity == dragonActivity == 1:
        dragon_hit = dragon.dragon_attack()
        hero_hit = hero.hero_attack()

###########   1.1. when Hero and Dragon attack is the same    ##########################
        if dragon_hit == hero_hit:
            hero.health -= dragon_hit/2

            print("Dragon hit with "+ str(dragon_hit/2)+" damage")
            print("Hero has left "+hero.get_health_points())
            dragon.health -= hero_hit/2
            print("Hero hit with "+ str(hero_hit/2)+" damage")
            print("Dragon has left "+dragon.get_health_points())
        else:
###########   1.2.1 when Hero attack > then Dragon attack    ##########################
            if hero_hit > dragon_hit:
                dragon.health -= hero_hit
                print("Hero hit with " + str(hero_hit) + " damage")
                print("Dragon has left "+dragon.get_health_points())
            else:
###########   1.2.2 when Hero attack < then Dragon attack    ##########################
                hero.health -= dragon_hit
                print("Dragon hit with " + str(dragon_hit) + " damage")
                print("Hero has left "+hero.get_health_points())



###########   2. when Hero and Dragon choose defence      ###############################
    elif heroActivity == dragonActivity == 2:
        print("Fighters are both in defence")
        print("Hero has left "+hero.get_health_points())
        print("Dragon has left "+dragon.get_health_points())



###########   3. when Hero choose attack and Dragon choose defence   ####################
    elif heroActivity < dragonActivity:
        dragon_def = dragon.dragon_defence()
        hero_hit = hero.hero_attack()

###########   3.1. when Hero attack > Dragon defence   ################################
        if hero_hit > dragon_def:
            dragon.health -= (hero_hit-dragon_def)
            print("Hero hit with " + str(hero_hit-dragon_def) + " damage")
            print("Dragon has left "+dragon.get_health_points())

###########   3.2. when Hero attack < Dragon defence   ################################
        else:
            print("Hero attack was repelled")
            print("Hero has left "+hero.get_health_points())
            print("Dragon has left "+dragon.get_health_points())



###########   4. when Dragon choose attack and Hero choose defence   ###################
    else:
        hero_def = hero.hero_defence()
        dragon_hit = dragon.dragon_attack()

###########   4.1. when Dragon attack > Hero defence   ###################
        if dragon_hit > hero_def:
            dragon.health -= (dragon_hit-hero_def)
            print("Dragon hit with " + str(dragon_hit-hero_def) + " damage")
            print("Hero has left "+hero.get_health_points())

###########   4.2. when Dragon attack < Hero defence   ###################
        else:
            print("Dragon attack was repelled")
            print("Hero has left "+hero.get_health_points())
            print("Dragon has left "+dragon.get_health_points())

    roundCounter+=1


########## Final info block ########################
print("_____________________________")
if hero.health < dragon.health:
    print("The winner is Dragon")
elif hero.health < dragon.health:
    print("Epic fight. Both is dead")
else:
    print("The winner is Hero")
print("_____________________________")
print("Final stat:")
hero.get_info()
dragon.get_info()
