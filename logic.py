class Game():
    def __init__(self):
        self.a = {}
        for i in range(9):
            self.a[i] = [0,0,0]

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
        self.player_move(int(loc), s)

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

    def cpu_turn():
        # make winning input_move
        # block winning move


    def run(self):
        running = True
        while running:
            self.input_move()
            running = self.check_win(1)


def main():
    game = Game()
    game.run()

if __name__ == '__main__':
    main()
