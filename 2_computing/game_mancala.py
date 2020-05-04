CodeSkulptor3


Code
6
1
"""
2
Student facing implement of solitaire version of Mancala - Tchoukaillon
3
​
4
Goal: Move as many seeds from given houses into the store
5
​
6
In GUI, you make ask computer AI to make move or click to attempt a legal move
7
"""
8
​
9
​
10
class SolitaireMancala:
11
    def __init__(self):
12
        self.board = [0, 0, 0, 0, 0, 0, 0]
13
​
14
    def __str__(self):
15
        return str(self.board[0]) + ", " + \
16
               str(self.board[1]) + ", " + \
17
               str(self.board[2]) + ", " + \
18
               str(self.board[3]) + ", " + \
19
               str(self.board[4]) + ", " + \
20
               str(self.board[5]) + ", " + \
21
               str(self.board[6])
22
​
23
    def set_board(self, configuration):
24
        for i in range(len(self.board)):
25
            self.board [i] = configuration[i]
26
​
27
    def get_num_seeds(self, house_num):
28
        return self.board[house_num]
29
​
30
    def is_legal_move(self, house_num):
31
        if house_num == 0:
32
            return False
33
        else:
34
            if self.get_num_seeds(house_num) > 0:
35
                return True
36
            else:
37
                return False
38
​
39
    def apply_move(self, house_num):
40
        if self.is_legal_move(house_num):
41
            self.board[house_num] = 0
42
            for i in range(house_num):
43
                self.board[i] = self.board[i] + 1
44
        else:
45
            print("Move is illigal!")
46
​
47
    def choose_move(self):
48
        for i in range(1, len(self.board) + 1):
49
            if self.board[i] > 0:
50
                return i
51
​
52
    def is_game_won(self):
53
        for i in range(1, len(self.board)):
54
            if self.board[len(self.board) - (i + 1)] != 0:
55
                return False
56
        return True
57
​
58
    def plan_moves(self):
59
        pass
60

61
​
62
# Create tests to check the correctness of your code
63
​
64
def test_mancala():
65
    """
66
    Test code for Solitaire Mancala
67
    """
68
    # test __init__()
69
    my_game = SolitaireMancala()
70
    print("__init__. # Initialize Mancala game with empty board")
71
    print("Testing init - Expected: 0, 0, 0, 0, 0, 0, 0")
72
    print("Testing init - Computed:", my_game, "\n")
73

Output
__init__. # Initialize Mancala game with empty board
Testing init - Expected: 0, 0, 0, 0, 0, 0, 0
Testing init - Computed: 0, 0, 0, 0, 0, 0, 0

set_board. # Seeds stones inside houses according give config
Testing set_board - Expected: [0, 5, 3, 1, 1, 0, 0]
Testing set_board - Computed: [0, 0, 1, 1, 3, 5, 0]

get_num_seeds. # Return number of seeds in dedicated house
Testing get_num_seeds - Expected: 0
Testing get_num_seeds - Computed: 0
Testing get_num_seeds - Expected: 1
Testing get_num_seeds - Computed: 1
Testing get_num_seeds - Expected: 5
Testing get_num_seeds - Computed: 5

is_legal_move. Calculate if move from give house_num is legal, return True (of False)
Testing is_legal_move - move from Store - Expected: False
Testing is_legal_move - move from Store - Computed: False
Testing is_legal_move - move from 2nd house - Expected: True
Testing is_legal_move - move from 2nd house - Computed: True
Testing is_legal_move - move from 5th house - Expected: True
Testing is_legal_move - move from 5th house - Computed: True

apply_move.Testing move from give house_num
Testing apply_move - situation after move from 1st house - Expected: [1, 1, 2, 2, 4, 0, 0]
Testing apply_move - situation after move from 1st house - Computed: [1, 1, 2, 2, 4, 0, 0]

Testing apply_move - situation after move from 3rd house - Expected: [2, 2, 3, 0, 4, 0, 0]
Testing apply_move - situation after move from 3rd house - Computed: [2, 2, 3, 0, 4, 0, 0]


choose_move. Returns number of house with best move according strategy
Testing choose_move - Expected: 2
Testing choose_move - Computed: 2
Testing choose_move - Expected: 6
Testing choose_move - Computed: 6
