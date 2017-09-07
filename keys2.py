allKeys = [Key(1, 3, "red"),
            Key(2, 4, "orange"),
            Key(3, 1, "yellow"),
            Key(4, 2, "lime"),
            Key(3, 5, "green"),
            Key(2, 2, "teal"),
            Key(5, 3, "blue"),
            Key(4, 4, "purple")]
allCrystals = [Key(1, 5, "white"),
            Key(5, 5, "brown"),
            Key(5, 1, "black"),
            Key(1, 1, "pink")]
# where all the keys and crystals are
class Key:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color
class Crystal:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color
class Wall:
    adjRooms = {
    'north': room,
    'east': ,
    'south': ,
    'west': ,
    }
    solid
    needsKey
    open
class Room:
    adjWalls = []
class Inventory:
    def __init__(self):
        self.keys = [0, 0, 0, 0, 0, 0, 0, 0]
        self.crystals = [0, 0, 0, 0]
class Pos:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.position = Matrix[self.x][self.y]
    def check(self):
        if self.position[0] == "1":
            print("You can GO NORTH.")
        if self.position[1] == "1":
            print("You can GO EAST.")
        if self.position[2] == "1":
            print("You can GO SOUTH.")
        if self.position[3] == "1":
            print("You can GO WEST.")
        # say where you can go
if __name__ == "__main__":
    print("Welcome to The Keys Adventure. Your objective is to collect the four crystals then reach the stairs. Good luck.")
    game = "inProgress"
    currentPos = Pos()
    # say where you start
    while game == "inProgress":
        currentPos.check()
        go = input()
        if currentPos.x == 2 and currentPos.y == 1 and Inventory.crystals == [1, 1, 1, 1]:
        # if you get to the stairs
            print("Congrats! You won!")
            game = "won"
            # you won
            break
            # end program
