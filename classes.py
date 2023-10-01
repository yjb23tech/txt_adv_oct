import random 

class Player:

    def __init__(self, str_name, int_age, str_location):
        self.str_name = str_name
        self.int_age = int_age
        self.str_location = str_location
        self.str_player_selection = " " 
    
    def __str__(self):
        return (f"Welcome {self.str_name} from {self.str_location}! Who knew a {self.int_age} year old sapling throw in his lot to become Pirate King XD")

class Weapon:

    def __str__(self):

        return (f"{self.str_weapon_name} has an atk pwr of {self.int_atk_pwr} and a def pwr of {self.int_def_pwr}")

class BattleAxe(Weapon):

    def __init__(self):

        self.str_weapon_name = "Battle Axe"
        self.int_atk_pwr = random.randint(1,100)
        self.int_def_pwr = random.randint(1, 100)
        self.int_spez_atk_pwr = random.randint(1, 200)
    


