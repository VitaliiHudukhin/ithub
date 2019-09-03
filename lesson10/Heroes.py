import math
import random

class Hero:
    def __init__(self, name, health=100, attack_lvl='8-13', defence_lvl='7-11'):
        """Constructor"""
        self.name = name
        self.health = health
        self.attack_lvl = attack_lvl
        self.defence_lvl = defence_lvl

    def get_info(self):
        print("Class: Hero")
        print("Name: "+self.name)
        print("Characteristics: ")
        print("Health: "+str(self.health))
        print("Attack: "+str(self.attack_lvl)+", Defence: "+str(self.defence_lvl))

    def get_health_points(self):
        helthPoints = self.health
        if helthPoints < 0:
            helthPoints = 0
        return str(helthPoints) + " points"

    def hero_attack(self):
        self.attack_lvl = random.randint(8, 13)
        return self.attack_lvl

    def hero_defence(self):
        self.defence_lvl = random.randint(7, 11)
        return self.defence_lvl
        #opponent.health -= math.floor(self.attack_lvl-self.attack_lvl*opponent.defence_lvl/100)

class Dragon:
    def __init__(self, name = ["Drogon", "Rhaegal", "Viserion"], health=100, attack_lvl='10-15',
                 defence_lvl='4-10'):
        """Constructor"""
        self.name = random.choice(name)
        self.health = health
        self.attack_lvl = attack_lvl
        self.defence_lvl = defence_lvl

    def get_info(self):
        print("Class: Dragon")
        print("Name: "+self.name)
        print("Characteristics: ")
        print("Health: "+str(self.health))
        print("Attack: "+str(self.attack_lvl)+", Defence: "+str(self.defence_lvl))

    def get_health_points(self):
        helthPoints = self.health
        if helthPoints < 0:
            helthPoints = 0
        return str(helthPoints) + " points"

    def dragon_attack(self):
        self.attack_lvl = random.randint(10, 15)
        return self.attack_lvl

    def dragon_defence(self):
        self.defence_lvl = random.randint(4, 10)
        return self.defence_lvl
        #opponent.health -= math.floor(self.attack_lvl-self.attack_lvl*opponent.defence_lvl/100)



'''
class Berserker():
   MAX_hp = 250
   base_hp = 250
   base_speed = 75
   priority = 'Normal'
   mindset_multiplier = 1.00
   move = ''

   def Jab(self,opponent):
       """ Jab - A fast, light attack. Does 30 Basic Damage to Opponent"""
       self.priority = 'Fast'
       opponent.base_hp -= math.floor( 30*self.mindset_multiplier )

   def Haymaker(self,opponent):
       """ Haymaker - A Slow, strong attack. Does 65 Base to Opponent and 30 Base Damage to User"""
       self.priority = 'Slow'
       opponent.base_hp -= math.floor (65*self.mindset_multiplier)
       self.base_hp -= math.floor(30*self.mindset_multiplier)

   def PumpUp(self,opponent):
       """ PumpUp - Normal speed. Improves the Mindset of the User ( x 1.25 )"""
       self.priority = 'Normal'
       self.mindset_multiplier *= 1.25

   move_pool = {'1':Jab,'2':Haymaker,'3':PumpUp}
'''