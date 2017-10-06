Matrix = [["0010c", "0110n", "0101y", "0011n", "0010c"],
          ["1010n", "1000o", "0100n", "1101ln", "1011n"],
          ["1110r", "0101", "0011", "0100", "1011g"],
          ["1010n", "0100p", "1101n", "0111t", "1011n"],
          ["1000c", "0100n", "0101b", "1001n", "1000c"]]
# a  5 by 5 matrix, 0 - 4 by 0 - 4
# defines each position's possible movement directions
# 0 means can't go, 1 means can go, NESW

# the room 1,1 is 11, the room 1,2 is 12 and to the right of 11, etc
#Crystals = {"pink" : "04",
#            "white" : "00",
#            "brown" : "40",
#            "black" : "44"}
            # where the crystals are
# Keys = {"red" : "02",
    #    "orange" : "11",
    #    "yellow" : "24",
    #    "lime" : "33",
    #    "green" : "20",
    #    "teal" : "13",
    #    "blue" : "42",
    #    "purple" : "31"}
        # where the keys are

class Room:
    def __init__(self):
        self.x = 2
        self.y = 2
        self.position = Matrix[self.x][self.y]
        self.numcrystals = 0
        self.inventory = ["inventory"]
        # start at 2, 2
    def checkMoves(self):
        if self.position[0] == "1":
            print("You can GO NORTH.")
        # if the matrix says you can go north, say you can go north
        if self.position[1] == "1":
            print("You can GO EAST.")
        if self.position[2] == "1":
            print("You can GO SOUTH.")
        if self.position[3] == "1":
            print("You can GO WEST.")
        # say where you can go
    def movement(self, move):
        if move == "GO NORTH" and self.position[0] == "1":
        # if you said go north and you can go north
            self.y = self.y - 1
            # move the y coordinate 1 north
            self.position = Matrix[self.x][self.y]
            # set your position
            print("You are now at " + str(self.x) + ", " + str(self.y))
            # say your new position
        elif move == "GO EAST" and self.position[1] == "1":
            self.x = self.x + 1
            self.position = Matrix[self.x][self.y]
            print("You are now at " + str(self.x) + ", " + str(self.y))
        elif move == "GO SOUTH" and self.position[2] == "1":
            self.y = self.y + 1
            self.position = Matrix[self.x][self.y]
            print("You are now at " + str(self.x) + ", " + str(self.y))
        elif move == "GO WEST" and self.position[3] == "1":
            self.x = self.x - 1
            self.position = Matrix[self.x][self.y]
            print("You are now at " + str(self.x) + ", " + str(self.y))
class Objects(Room):
    def checkKey(self):
        if self.position[4] == "r":
            print("Red Key found")
            self.inventory.append["red"]
        elif self.position[4] == "o":
            print("Orange Key found")
            self.inventory.append["orange"]
        elif self.position[4] == "y":
            print("Yellow Key found")
            self.inventory.append["yellow"]
        elif self.position[4] == "l":
            print("Lime Key found")
            self.inventory.append["lime"]
        elif self.position[4] == "g":
            print("Green Key found")
            self.inventory.append["green"]
        elif self.position[4] == "t":
            print("Teal Key found")
            self.inventory.append["teal"]
        elif self.position[4] == "b":
            print("Blue Key found")
            self.inventory.append["blue"]
        elif self.position[4] == "p":
            print("Purple Key found")
            self.inventory.append["purple"]
        elif self.position[4] == "c" and self.numcrystals == 0:
            print("Crystal 1 found")
            self.inventory.append["crystal1"]
            self.numcrystals = 1
        elif self.position[4] == "c" and self.numcrystals == 1:
            print("Crystal 2 found")
            self.inventory.append["crystal2"]
            self.numcrystals = 2
        elif self.position[4] == "c" and self.numcrystals == 2:
            print("Crystal 3 found")
            self.inventory.append["crystal3"]
            self.numcrystals = 3
        elif self.position[4] == "c" and self.numcrystals == 3:
            print("Last Crystal found")
            self.inventory.append["crystal4"]
            self.numcrystals = 4
    def printInventory(self):
        print("Current Inventory: " + self.inventory)

# class Wall:
# if the movement is going through a wall stop the movement

# class Maze (Wall, Room):
# if the movement is going through a door, check for the key, then move

if __name__ == "__main__":
    maze = Room()
    items = Objects()
    print("Welcome to The Key Maze. Collect all four crystals and reach 2, 1.")
    print("You are now at " + str(maze.x) + ", " + str(maze.y))
    game = True
    # say where you start
    while game == True :
        maze.checkMoves()
        move = input()
        maze.movement(move)
        #items.checkCrystal()
        items.checkKey()
        items.printInventory
        if maze.x == 1 and maze.y == 4 :
        # if you find the end
            print("You found the end!")
            # you won
            break
            # end
