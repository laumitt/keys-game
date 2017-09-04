RedMatrix = [[1, 3],
             [5, 2],
             [5, 1]]
OrangeMatrix = [[2, 4],
                [3, 1],
                [2, 1]]
YellowMatrix = [[3, 1],
                [4, 4],
                [4, 5]]
LimeMatrix = [[4, 2],
              [5, 3],
              [5, 4]]
GreenMatrix = [[3, 5],
               [1, 2],
               [1, 1]]
BlueMatrix = [[5, 3],
              [1, 4],
              [1, 5]]
PurpleMatrix = [[4, 4],
                [4, 2],
                [4, 1]]
# keys matrices show position of keys, x and y; square door can be opened from, x and y; square door leads to, x and y
WhiteMatrix = [1, 5]
BrownMatrix = [5, 5]
BlackMatrix = [5, 1]
PinkMatrix = [1,1]
# crystals matrices show position of crystals, x and y
StairsMatrix = [2, 1]
# stairs are at 2,1
StartLocation = [3][3]
# start is at 3, 3
Matrix = [["0010", "0110", "0101", "0011", "0010"],
          # 5, 1;   5, 2;   5, 3;   5, 4;   5, 5
          ["1010", "1000", "0100", "1101", "1011"],
          # 4, 1;   4, 2;   4, 3;   4, 4;   4, 5
          ["1110", "0101", "0011", "0100", "1011"],
          # 3, 1;   3, 2;   3, 3;   3, 4;   3, 5
          ["1010", "0100", "1101", "0111", "1011"],
          # 2, 1;   2, 2;   2, 3;   2, 4;   2, 5
          ["1000", "0100", "0101", "1001", "1000"]]
          # 1, 1;   1, 2;   1, 3;   1, 4;   1, 5
# a 5 by 5 matrix with each row numbered 1-5
# defines each squares's possible movement directions
# at position 1, 3, you can go north, you can go east, you can go south, you can't go west
Inventory = [0, 0, 0, 0, 0, 0, 0, 0]
# inventory is empty
# each 0 represents a key that can be held (red, orange, yellow, lime, green, teal, blue, or purple)
global x
global y
global position
class Movement
    def checkMove(position):
        if position[0] == "1":
            print("You can GO NORTH.")
        elif position[1] == "1":
            print("You can GO EAST.")
        elif position[2] == "1":
            print("You can GO SOUTH.")
        elif position[3] == "1":
            print("You can GO WEST.")
        # say where you can go
    def movement(move):
        if move == "GO NORTH" and position[0] == "1":
        # if you said go north and you can go north
            y = y - 1
            # move the y coordinate 1 north
            position = Matrix[x][y]
            # set your position
            print("You are now at " + str(x) + ", " + str(y))
            # say your new position
        elif move == "GO EAST" and position[1] == "1":
            x = x + 1
            position = Matrix[x][y]
            print("You are now at " + str(x) + ", " + str(y))
        elif move == "GO SOUTH" and position[2] == "1":
            y = y + 1
            position = Matrix[x][y]
            print("You are now at " + str(x) + ", " + str(y))
        elif move == "GO WEST" and position[3] == "1":
             x = x - 1
             position = Matrix[x][y]
             print("You are now at " + str(x) + ", " + str(y))
class Keys
    def inventoryUpdate(position):
        if position == redMatrix[1]:
            inventory[0] = 1
        elif position == orangeMatrix[1]:
            inventory[1] = 1
        elif position == yellowMatrix[1]:
            inventory[2] = 1
        elif position == limeMatrix[1]:
            inventory[3] = 1
        elif position == greenMatrix[1]:
            inventory[4] = 1
        elif position == tealMatrix[1]:
            inventory[5] = 1
        elif position == blueMatrix[1]:
            inventory[6] = 1
        elif position == purpleMatrix[1]:
            inventory[7] = 1
