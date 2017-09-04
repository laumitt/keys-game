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

StartLocation = [3, 3]
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

InventoryKeys = [0, 0, 0, 0, 0, 0, 0, 0]
# keys inventory is empty
# each 0 represents a key that can be held (red, orange, yellow, lime, green, teal, blue, or purple)

InventoryCrystals = [0, 0, 0, 0]
# crystals inventory is empty
# each 0 represents a crystal that can be held (pink, white, brown, and black)

class Movement:
    global x
    global y
    global position
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
    def go(move):
        global x
        global y
        global position
        if move == "GO NORTH" and position[0] == "1":
        # if you said go north and you can go north
            y = y - 1
            # move the y coordinate 1 north
            position = Matrix[x][y]
            # set your position
            print("You enter a new room.")
        elif move == "GO EAST" and position[1] == "1":
            x = x + 1
            position = Matrix[x][y]
            print("You enter a new room.")
        elif move == "GO SOUTH" and position[2] == "1":
            y = y + 1
            position = Matrix[x][y]
            print("You enter a new room.")
        elif move == "GO WEST" and position[3] == "1":
             x = x - 1
             position = Matrix[x][y]
             print("You enter a new room.")
class Keys:
    def inventoryUpdate(position):
        if position == redMatrix[1]:
        # if you're where the red key is
            InventoryKeys[0] = 1
            # inventory gets the red key
            print("You found a red key.")
            # say you get the red key
        elif position == orangeMatrix[1]:
            InventoryKeys[1] = 1
            print("You found an orange key.")
        elif position == yellowMatrix[1]:
            InventoryKeys[2] = 1
            print("You found a yellow key.")
        elif position == limeMatrix[1]:
            InventoryKeys[3] = 1
            print("You found a lime key.")
        elif position == greenMatrix[1]:
            InventoryKeys[4] = 1
            print("You found a green key.")
        elif position == tealMatrix[1]:
            InventoryKeys[5] = 1
            print("You found a teal key.")
        elif position == blueMatrix[1]:
            InventoryKeys[6] = 1
            print("You found a blue key.")
        elif position == purpleMatrix[1]:
            InventoryKeys[7] = 1
            print("You found a purple key.")
    # def inventoryCheck(Inventory):
        
class Crystals:
    def inventoryCUpdate(position):
        if position == whiteMatrix[1]:
        # if you're where the white crystal is
            InventoryCrystals[0] = 1
            # inventory gets the white crystal
            print("You found a white crystal.")
            # say you get the white crystal
        elif position == pinkMatrix[1]:
            InventoryCrystals[1] = 1
            print("You found a pink crystal.")
        elif position == brownMatrix[1]:
            InventoryCrystals[2] = 1
            print("You found a brown crystal.")
        elif position == blackMatrix[1]:
            InventoryCrystals[3] = 1
            print("You found a black crystal.")

if __name__ == "__main__":
    x, y = 0,0
    position = Matrix[x][y]
    print("Welcome to The Keys. Your objective is to collect the four crystals then reach the stairs. Good luck.")
    game = "inProgress"
    # say where you start
    while game == "inProgress":
        Movement.checkMove(Matrix[x][y])
        move = input()
        Movement.go(move);
        if x == 3 and y == 3 and InventoryCrystals == [1, 1, 1, 1]:
        # if you get to the stairs
            print("Congrats! You won!")
            game = "won"
            # you won
            break
            # end program
