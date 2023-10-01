from sb_classes import Tile 

arr_game_grid = [[0, 1, 2], [0, 1, 2], [0, 1, 2]]

arr_game_grid_3_by_3 = [["South West", "West", "North West"], ["South", "Centre", "North"], ["South East", "East", "North East"]]

print(" ")

print(arr_game_grid_3_by_3[0][0])
print(arr_game_grid_3_by_3[0][1])
print(arr_game_grid_3_by_3[0][2])

print(" ")

print(arr_game_grid_3_by_3[1][0])
print(arr_game_grid_3_by_3[1][1])
print(arr_game_grid_3_by_3[1][2])

print(" ")

print(arr_game_grid_3_by_3[2][0])
print(arr_game_grid_3_by_3[2][1])
print(arr_game_grid_3_by_3[2][2])

print(" ")

arr_greed_island_grid = [
                         
                         [Tile(0, 0, "South West"), Tile(0, 1, "West"), Tile(0, 2, "North West")], 
                         [Tile(1, 0, "South"), Tile(1, 1, "Centre"), Tile(1, 2, "North")],
                         [Tile(2, 0, "South East"), Tile(2, 1, "East"), Tile(2, 2, "North East")]

    ]

#A good lesson learned
#Probably the most important code I've ever written (1)
for quad in arr_greed_island_grid:
    print(quad)
print(" ")

#Probably the most important code I've ever written (2)
for x in range(3):
    for y in range(3):
        print(arr_greed_island_grid[x][y])
    print(" ")

#Probably the most important code I've ever written (3)
for x in range(len(arr_greed_island_grid)):
    for y in range(len(arr_greed_island_grid)):
        print(arr_greed_island_grid[x][y])
    print(" ")

try: 
    arr_greed_island_grid[2][3]
except IndexError:
    print("You're heading for uncharted waters Sailor; you will be returned back to your last known location")










