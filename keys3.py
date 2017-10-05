Matrix = [["0010", "0110", "0101", "0011", "0010"],
          ["1010", "1000", "0100", "1101", "1011"],
          ["1110", "0101", "0011", "0100", "1011"],
          ["1010", "0100", "1101", "0111", "1011"],
          ["1000", "0100", "0101", "1001", "1000"]]
# a  5 by 5 matrix with each row numbered 1-5
# defines each position's possible movement directions
# 0 means can't go, 1 means can go, NESW

# the room 1,1 is 11, the room 1,2 is 12 and to the right of 11, etc
Crystals = {"pink" : "11",
            "white" : "15",
            "brown" : "55",
            "black" : "51"}
            # where the crystals are
Keys = {"red" : "13",
        "orange" : "24",
        "yellow" : "31",
        "lime" : "42",
        "green" : "35",
        "teal" : "22",
        "blue" : "53",
        "purple" : "44"}
        # where the keys are

class Room:
    def __init__(self):
        self.x = 3
        self.y = 3
        self.position = Matrix[self.x][self.y]
        # start at 3, 3
    def check(self):
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
    def checkCrystal(self):
        location = str(self.x) + str(self.y)
        if location in Crystals:
            print("You collected the " + Crystals(str(self.x) + str(self.y)) + " crystal!")
    def checkKeys(self):
        location = str(self.x) + str(self.y)
        if location in Keys:
            print("You collected the " + Keys(str(self.x) + str(self.y)) + " key!")
# class Wall:
    # something about the doors and needing keys

# class Maze (Wall, Room):
# if the movement is going through a door, check for the key, then move

if __name__ == "__main__":
    maze = Room()
    print("Welcome to The Key Maze. Collect all four crystals and reach 2, 1.")
    print("You are now at " + str(maze.x) + ", " + str(maze.y))
    game = True
    # say where you start
    while game == True :
        maze.check()
        move = input()
        maze.movement(move)
        maze.checkCrystal()
        maze.checkKeys()
        if maze.x == 2 and maze.y == 1 :
        # if you find the end
            print("You found the end!")
            # you won
            break
            # end
