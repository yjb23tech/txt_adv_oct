from classes import Player
from functions import str_player_name, int_player_age, str_player_location, str_player_selection 
from data_strucs import arr_player_options 

def play():

    bool_game_is_on = True 

    test_player = Player("Joshua", 29, "LunDun")
    print(" ")
    print(test_player)
    print(" ")

    test_player_2 = Player(str_player_name(), int_player_age(), str_player_location())

    print(" ")
    print(test_player_2)

    while(bool_game_is_on == True):

        print("\nYou have the following options available to you Sailor:\n")

        for x, option in enumerate(arr_player_options, 1):
            print(f"{x}. Press {option}")
        print(" ")

        test_player.str_player_selection = str_player_selection()
        test_player_2.str_player_selection = str_player_selection()

        print(f"{test_player.str_name} has chosen option {test_player.str_player_selection}")
        print(f"{test_player_2.str_name} has chosen option {test_player_2.str_player_selection}")

        if test_player.str_player_selection in ['North', 'north', 'NORTH', 'N', 'n', '^']:
            print("You're now travelling Norte")
        elif test_player.str_player_selection in ['East', 'east', 'EAST', 'E', 'e', '>']:
            print("You're now travelling East")
        elif test_player.str_player_selection in ['South', 'south', 'SOUTH', 'S', 's', 'v']:
            print("You're now travelling South")
        elif test_player.str_player_selection in ['West', 'west', 'WEST', 'W', 'w', '<']:
            print("You're now travelling West")
        elif test_player.str_player_selection in ['Inventory', 'inventory', 'I', 'i']:
            print("You have access to the following items in your Inventory:\n")
        elif test_player.str_player_selection in ['Quit', 'quit', 'Q', 'q']:
            ui_confirm_quit = input("You have chosen to Quit the game; please type in Q-U-I-T to confirm:\n")
            if ui_confirm_quit == 'QUIT':
                print("Until we meet again Sailor!")
                bool_game_is_on = False
            else:
                print("Back to the sea we go ya matey!")
        else:
            print("Invalid selection; try again")

play()






