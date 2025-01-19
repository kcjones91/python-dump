class Enemy:
    
    def __init__(self, type_of_enemy, health_points, attack_damage):
        self.__type_of_enemy = type_of_enemy
        self.health_points = health_points
        self.attack_damage = attack_damage
        
    def get_type_enemy(self):
        return self.__type_of_enemy
    
    def talk(self):
        print(f"{self.__type_of_enemy}. parent class definition!")
        
    def walk_forward(self):
        print(f"{self.__type_of_enemy} moves closer to you.")
        
    def attack(self):
        print(f"{self.__type_of_enemy} attacks for {self.attack_damage}.")
            

class Skultula(Enemy):
    
    def __init__(self, health_points, attack_damage):
        super().__init__(type_of_enemy='Skultula', 
                         health_points=health_points,
                         attack_damage=attack_damage)
        
    def talk(self):
        print("*chuckle")
        
    def bone_attack(self):
        print(f"{self.get_type_enemy} is attacking with it's hard bones!")
        
        
class Gannondorf(Enemy):
    
    def __init__(self, health_points, attack_damage):
        super().__init__(type_of_enemy='Gannondorf', 
                        health_points=health_points,
                        attack_damage=attack_damage)
        
    def talk(self):
        print("Muhahahaha!")
    
    def prince_of_darkness(self):
        print(f"{self.get_type_enemy()}'s aura reduces courage...")
        

       

skullkid = Skultula(100, 100)
skullkid.talk()
skullkid.walk_forward()
skullkid.bone_attack()
skullkid.attack()
print(skullkid.get_type_enemy())
print(skullkid.health_points)
print(skullkid.attack_damage)


gannondorf = Gannondorf(1000, 1000)
gannondorf.talk()
gannondorf.prince_of_darkness()
gannondorf.walk_forward()
gannondorf.attack()
print(gannondorf.get_type_enemy())
print(gannondorf.health_points)
print(gannondorf.attack_damage)
