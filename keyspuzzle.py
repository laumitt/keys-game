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
          ["1000", "0100", "0101", "1001", "1000"],
          # 1, 1;   1, 2;   1, 3;   1, 4;   1, 5
# a 5 by 5 matrix with each row numbered 1-5
# defines each squares's possible movement directions
# at position 1, 3, you can go north, you can go east, you can go south, you can't go west
