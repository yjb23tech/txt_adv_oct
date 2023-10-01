class Player:

    def __init__(self, str_name, int_age, str_location):
        self.str_name = str_name
        self.int_age = int_age
        self.str_location = str_location
        self.str_player_selection = " " 
    
    def __str__(self):
        return (f"Welcome {self.str_name} from {self.str_location}! Who knew a {self.int_age} year old sapling throw in his lot to become Pirate King XD")

