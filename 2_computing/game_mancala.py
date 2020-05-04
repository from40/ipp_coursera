

class SolitaireMancala:
    def __init__(self):
        self.board = [0, 0, 0, 0, 0, 0, 0]

    def __str__(self):
        return str(self.board[6]) + ", " + \
               str(self.board[5]) + ", " + \
               str(self.board[4]) + ", " + \
               str(self.board[3]) + ", " + \
               str(self.board[2]) + ", " + \
               str(self.board[1]) + ", " + \
               str(self.board[0]) + ".\n"

    def set_board(self, configuration):
        for i in range(len(self.board)):
            self.board [i] = configuration[i]

    def get_num_seeds(self, house_num):
        return self.board[len(self.board) - house_num]

    def is_legal_move(self, house_num):
        if house_num == 0:
            return False
        else:
            if house_num == get_num_seeds(house_num):
                return True
            else:
                return False

    def apply_move(self, house_num):
        if is_legal_move(house_num) and house_num > 0:
            self.board[len(self.board) - house_num] = 0
            for i in range(house_num):
                self.board[len(self.board) - i] = self.board[len(self.board) - i] + 1
        else:
            print("Move is illigal!")

    def choose_move(self):
        for i in range(1, len(self.board)):
            if self.board[len(self.board) - (i + 1)] == get_num_seeds(i):
                return len(self.board) - (i + 1)

    def is_game_won(self):
        for i in range(1, len(self.board)):
            if self.board[len(self.board) - (i + 1)] != 0:
                return False
        return True

    def plan_moves(self):
        pass
