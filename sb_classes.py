class Tile:

    def __init__(self, int_loc_x, int_loc_y, str_loc_quadrant):

        self.int_loc_x = int_loc_x 
        self.int_loc_y = int_loc_y 
        self.str_loc_quadrant = str_loc_quadrant
    
    def __str__(self):
        return (f"You're in the {self.str_loc_quadrant} quadrant of the map, co-ordinates [{self.int_loc_x}, {self.int_loc_y}]")





