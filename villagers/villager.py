
class Villager:

    def __init__(self,name : str):
        self.name = name
        self.health = 50
        self.defense = 0
        self.attack = 0
        self.is_alive = True

    def check_health(self,incoming_attack_value : int):
        if self.defense >= incoming_attack_value:
            return "Dont hurt me"
        else:
            damage = incoming_attack_value - self.defense 
            self.health -= damage
            self.health = self.health if self.health > 0 else 0
            if self.health == 0:
                self.is_alive = False
                return (False, "Target is dead!")
            else:
                return f"Vida atual: {self.health}"
    def normal_attack(self,target):
       return target.check_health(self.attack)          


class Mage(Villager):

    def __init__(self, name: str):
        super().__init__(name)
        self.attack = 10
        self.mana = 100

    def fire_ball(self,target):
        if self.mana > 20:
            self.mana = self.mana - 20
            return target.check_health(self.attack + 20)
        else:
            return (False, "Target is dead!")    
