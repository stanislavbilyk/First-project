class Chess:
    color: str = "white"
    x: int = 3
    y: int = 5
    def change_color(self):
        self.color = "black"

    def check_move(self, x: int, y: int) -> bool:
        raise NotImplementedError("check_move() not implemented")

    def _chessboard(self, x: int, y: int) -> bool:
        if x < 0 or x > 8 or y < 0 or y > 8:
            raise ValueError("x and y must be between 0 and 8")
        else:
            return True


    def change_place(self, x: int, y: int) -> None:
        if self._chessboard(x, y):
            self.x = x
            self.y = y
        else:
            raise ValueError("x and y must be between 0 and 8")


class Pawn(Chess):
    def check_move(self, x: int, y: int) -> bool:
        self._chessboard(x, y)
        if x == self.x and y == self.y + 1:
            return True
        else:
            return False

class Rook(Chess):
    def check_move(self, x: int, y: int) -> bool:
        self._chessboard(x, y)
        if x == self.x or y == self.y:
            return True
        else:
            return False

class Bishop(Chess):
    def check_move(self, x: int, y: int) -> bool:
        self._chessboard(x, y)
        if abs(x - self.x) == abs(y - self.y):
            return True
        else:
            return False

class Knight(Chess):
    def check_move(self, x: int, y: int) -> bool:
        self._chessboard(x, y)
        if (x == self.x + 2 or x == self.x - 2) and (y == self.y + 1 or y == self.y - 1):
            return True
        elif (y == self.y + 2 or y == self.y - 2) and (x == self.x + 1 or x == self.x - 1):
            return True
        else:
            return False

class Queen(Chess):
    def check_move(self, x: int, y: int) -> bool:
        self._chessboard(x, y)
        if x == self.x or y == self.y:
            return True
        elif abs(x - self.x) == abs(y - self.y):
            return True
        else:
            return False

class King(Chess):
    def check_move(self, x: int, y: int) -> bool:
        self._chessboard(x, y)
        if x == self.x and y == self.y + 1 or x == self.x and y == self.y - 1:
            return True
        if y == self.y and x == self.x + 1 or y == self.y and x == self.x - 1:
            return True
        if x == self.x + 1 and y == self.y + 1 or x == self.x - 1 and y == self.y - 1:
            return True
        if x == self.x - 1 and y == self.y + 1 or x == self.x + 1 and y == self.y - 1:
            return True
        else:
            return False



pawn = Pawn()
rook = Rook()
bishop = Bishop()
knight = Knight()
queen = Queen()
king = King()

figures = [pawn, rook, bishop, knight, queen, king]
print(figures)

new_list = []
def lets_play(x: int, y: int, f: list) -> list:
    for figure in f:
        if figure.check_move(x, y) == True:
            new_list.append(figure.__class__.__name__)


lets_play(1, 4, figures)
print(new_list)
# print(knight.check_move(1, 9))


# def change_place(self, x: int, y: int) -> None:
#     if x < 0 and x > 8:
#         raise ValueError("x must be between 0 and 8")
#     else:
#         self.x = x
#     if y < 0 and y > 8:
#         raise ValueError("y must be between 0 and 8")
#     else:
#         self.y = y

# queen.change_place(2, 8)
# print(queen.x, queen.y)