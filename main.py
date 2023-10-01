from classes import Player
from functions import str_player_name, int_player_age, str_player_location
from data_strucs import arr_player_options 

test_player = Player("Joshua", 29, "LunDun")
print(" ")
print(test_player)
print(" ")

test_player_2 = Player(str_player_name(), int_player_age(), str_player_location())

print(" ")
print(test_player_2)
print("\nYou have the following options available to you Sailor:\n")

for x, option in enumerate(arr_player_options, 1):
    print(f"{x}. Press {option}")
print(" ")






