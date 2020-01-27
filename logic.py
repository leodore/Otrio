import random

class Game():
    def __init__(self):
        self.a = {}
        cpu_moves = {}
        for i in range(9):
            self.a[i] = [0,0,0]

    # places a player's piece on the board
    def player_move(self, cell, size, player):
        if size == "3":
            if self.a[cell][0] != 0:
                print("invalid move")
            else:
                self.a[cell][0] = player
                print("placed large @ " + str(cell))
        elif size == "2":
            if self.a[cell][1] != 0:
                print("invalid move")
            else:
                self.a[cell][1] = player
                print("placed medium @ " + str(cell))
        elif size == "1":
            if self.a[cell][2] != 0:
                print("invalid move")
            else:
                self.a[cell][2] = player
                print("placed small @ " + str(cell))
        else:
            print("invalid move a")

    # i/o to test logic of game -- remove after link board and logic --
    def input_move(self):
        loc = input ("location: ")
        s = input ("which piece: ")
        self.player_move(int(loc), s, 1)

    # checks if a player has won
    def check_win(self, player):
        b = self.a
        # handles descending/ascending avenues
        if (
            (b[0][2] == b[4][1] == b[8][0] == player) or (b[0][2] == b[1][1] == b[2][0] == player) or
            (b[0][2] == b[3][1] == b[6][2] == player) or (b[0][0] == b[4][1] == b[8][2] == player) or
            (b[0][0] == b[1][1] == b[2][2] == player) or (b[0][0] == b[3][1] == b[6][2] == player) or
            (b[2][0] == b[5][1] == b[8][2] == player) or (b[2][2] == b[5][1] == b[8][0] == player) or
            (b[3][2] == b[4][1] == b[5][0] == player) or (b[3][0] == b[4][1] == b[5][2] == player) or
            (b[6][0] == b[4][1] == b[2][2] == player) or (b[6][2] == b[4][1] == b[2][0] == player) or
            (b[0][2] == b[4][1] == b[8][0] == player) or (b[0][0] == b[4][1] == b[8][2] == player) or
            (b[6][0] == b[7][1] == b[8][2] == player) or (b[6][2] == b[7][1] == b[8][0] == player)
           ):
           return False
        # handles same size avenues
        for i in range(3):
            if (
                (b[0][i] == b[1][i] == b[2][i] == player) or (b[0][i] == b[3][i] == b[6][i] == player) or
                (b[0][i] == b[4][i] == b[8][i] == player) or (b[1][i] == b[4][i] == b[7][i] == player) or
                (b[2][i] == b[4][i] == b[6][i] == player) or (b[2][i] == b[5][i] == b[8][i] == player) or
                (b[3][i] == b[4][i] == b[5][i] == player) or (b[6][i] == b[7][i] == b[8][i] == player)
               ):
               return False
        # concentric circles in same cell
        for x in b:
            if b.get(x) == [player,player,player]:
                return False
        return True

    # if there's an immediate win condition, return the winning move
    def win_condition(self, player):
        b = self.a
        if (
                (b[4][0] == b[8][0] == player) or (b[3][0] == b[6][0] == player) or
                (b[1][0] == b[2][0] == player) or (b[4][1] == b[8][2] == player) or
                (b[3][1] == b[6][2] == player) or (b[1][1] == b[2][2] == player) or
                (b[0][1] == b[0][2] == player)
           ):
            (0,0)
        elif(
                (b[4][1] == b[8][1] == player) or (b[1][1] == b[2][1] == player) or
                (b[3][1] == b[6][1] == player) or (b[0][0] == b[0][2] == player)
            ):
            (0,1)
        elif(
                
            ):
            (0,2)
    def cpu_turn(self):
        # Make winning move
        # Block winning move
        if self.win_condition(1) == None:
            size = random.randint(1,3)
            cell = random.randint(0,8)
            self.player_move(cell, str(size), 2)
            print("cpu moved " + str(cell) + ", " + str(size))
        else:
            block = win_condition(1)
            player_move(block[0], block[1], 2)
    def run(self):
        running = True
        while running:
            self.input_move()
            running = self.check_win(1)
            self.cpu_turn()


def main():
    game = Game()
    game.run()

if __name__ == '__main__':
    main()
