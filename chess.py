class Chess:
    color: str = "white"
    x: int = 5
    y: int = 3
    def change_color(self):
        if self.color == "black":
            self.color = "white"
        else:
            self.color = "black"

    def check_move(self, x: int, y: int) -> bool:
        self.chessboard(x, y)
        # raise NotImplementedError("check_move() not implemented")
        return True

    def chessboard(self, x: int, y: int) -> bool:
        if x < 0 or x > 7 or y < 0 or y > 7:
            raise ValueError("x and y must be between 0 and 7")
        return True

    def change_place(self, x: int, y: int) -> None:
        if self.chessboard(x, y):
            self.x = x
            self.y = y
        else:
            raise ValueError("x and y must be between 0 and 7")

class Pawn(Chess):
    def check_move(self, x: int, y: int) -> bool:
        super().check_move(x, y)
        if self.color == "white":
            return x == self.x and y == self.y + 1
        if self.color == "black":
            return x == self.x and y == self.y - 1

class Rook(Chess):
    def check_move(self, x: int, y: int) -> bool:
        super().check_move(x, y)
        return x == self.x or y == self.y

class Bishop(Chess):
    def check_move(self, x: int, y: int) -> bool:
        super().check_move(x, y)
        return abs(x - self.x) == abs(y - self.y)

class Knight(Chess):
    def check_move(self, x: int, y: int) -> bool:
        super().check_move(x, y)
        return ((x == self.x + 2 or x == self.x - 2) and (y == self.y + 1 or y == self.y - 1)) or \
        ((y == self.y + 2 or y == self.y - 2) and (x == self.x + 1 or x == self.x - 1))

class Queen(Chess):
    def check_move(self, x: int, y: int) -> bool:
        super().check_move(x, y)
        return (x == self.x or y == self.y) or \
        (abs(x - self.x) == abs(y - self.y))

class King(Chess):
    def check_move(self, x: int, y: int) -> bool:
        super().check_move(x, y)
        move_x = abs(x - self.x)
        move_y = abs(y - self.y)
        return move_x <= 1 and move_y <= 1 and not (move_x == move_y == 0)

pawn = Pawn()
rook = Rook()
bishop = Bishop()
knight = Knight()
queen = Queen()
king = King()

figures = [pawn, rook, bishop, knight, queen, king]

def lets_play(x: int, y: int, f: list) -> list:
    result = []
    for figure in f:
        if figure.check_move(x, y):
            result.append(figure.__class__.__name__)
    return result
new_list = lets_play(3, 4, figures)
print(new_list)


