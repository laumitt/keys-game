# boolean says is there a wall there?
# the room 1,1 is 11, the room 1,2 is to its right, etc
Row1 = [Room(True, True, False, True),
    Room(True, False, False, True),
    Room(True, False, True, False),
    Room(True, True, False, False),
    Room(True, True, False, True)]
# second row
Row2 = [Room(False, True, False, True),
    Room(False, True, True, True),
    Room(True, False, True, True),
    Room(False, False, True, False),
    Room(False, True, False, False)]
# third row
Row3 = [Room(True, True, False, True),
    Room(True, True, False, True),
    Room(True, True, False, True),
    Room(True, True, False, True),
    Room(True, True, False, True)]
# fourth row, 1-5 right to left
Row4 = [Room(True, True, False, True),
    Room(True, True, False, True),
    Room(True, True, False, True),
    Room(True, True, False, True),
    Room(True, True, False, True)]
# fifth row, 1-5 right to left
Row5 = [Room(True, True, False, True),
    Room(True, True, False, True),
    Room(True, True, False, True),
    Room(True, True, False, True),
    Room(True, True, False, True)]

class Room:
    def __init__(self, state):
        self.state
