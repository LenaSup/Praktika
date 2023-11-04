class Chess:
    def __init__(self):
        self.pole = ['.' for i in range(8) for j in range(8)]
        self.member = {}

    def remember(self, old_x, old_y, new_x, new_y, type_p):
        self.member[len(self.member) + 1] = [old_x, old_y, new_x, new_y, type_p]

    def show_member(self):
        pass


class Piece:
    def __init__(self, x, y):
        self.x_pos = x
        self.y_pos = y

    def move(self, new_x, new_y):
        self.x_pos = new_x
        self.y_pos = new_y


