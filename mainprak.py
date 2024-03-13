class Chess:
    def __init__(self):
        self.pole = [['.' for j in range(8)] for i in range(8)]
        self.member = {}
        self.player = 0
        self.king_life = True

    def remember(self, old_x, old_y, new_x, new_y):
        self.member[len(self.member) + 1] = [old_x, old_y, new_x, new_y, self.player]

    def show_member(self):
        pass

    def update(self, *cords):
        self.pole[cords[0]][cords[1]].up_cords(cords[0], cords[1])
        self.player = not self.player

    def fill(self):
        self.pole[0][0] = Rook(0, 0, 1)
        self.pole[0][7] = Rook(0, 7, 1)
        self.pole[0][1] = Knight(0, 1, 1)
        self.pole[0][6] = Knight(0, 6, 1)
        self.pole[0][2] = Bishop(0, 2, 1)
        self.pole[0][5] = Bishop(0, 5, 1)
        self.pole[0][3] = Queen(0, 3, 1)
        self.pole[0][4] = King(0, 4, 1)

        self.pole[7][0] = Rook(7, 0, 0)
        self.pole[7][7] = Rook(7, 7, 0)
        self.pole[7][1] = Knight(7, 1, 0)
        self.pole[7][6] = Knight(7, 6, 0)
        self.pole[7][2] = Bishop(7, 2, 0)
        self.pole[7][5] = Bishop(7, 5, 0)
        self.pole[7][3] = Queen(7, 3, 0)
        self.pole[7][4] = King(7, 4, 0)

        for i in range(8):
            self.pole[1][i] = Pawn(1, i, 1)
        for i in range(8):
            self.pole[6][i] = Pawn(6, i, 0)

    def move(self, old_x, old_y, new_x, new_y):
        if not (-1 < old_y < 8 and -1 < new_y < 8):
            print('Вы вышли за игравое поле')
            return False
        if self.pole[old_y][old_x] == '.':
            print('Вы не выбрали фигуру для хода')
            return False
        if self.pole[old_y][old_x].owner != self.player:
            print('Это не выша фигура')
            return False
        if self.pole[new_y][new_x] == '.':
            Chess.remember(self, old_x, old_y, new_x, new_y)
            self.pole[new_y][new_x], self.pole[old_y][old_x] = self.pole[old_y][old_x], '.'
            Chess.update(self, new_y, new_x)
            return True
        if self.pole[new_y][new_x].owner == self.player:
            print('Нельзя атакавать себя')
            return False
        Chess.remember(self, old_x, old_y, new_x, new_y)
        self.king_life = type(self.pole[new_y][new_x]) != King
        self.pole[new_y][new_x], self.pole[old_y][old_x] = self.pole[old_y][old_x], '.'
        Chess.update(self, new_y, new_x)
        return True

    def show(self):
        print('  A B C D E F G H')
        k = 8
        for i in self.pole:
            print(k, end=' ')
            for j in i:
                print(j, end=' ')
            print(k)
            k -= 1
        print('  A B C D E F G H')


class Pawn:
    def __init__(self, x, y, player):
        self.x_pos = x
        self.y_pos = y
        self.owner = player
        self.pos_mv = Pawn.possible_moves(self)

    def possible_moves(self):
        out = []
        if self.y_pos < 2 or self.y_pos > 5:
            out.append([self.x_pos, self.y_pos + 1 * (-1 ** self.owner)])
            out.append([self.x_pos, self.y_pos + 2 * (-1 ** self.owner)])
        else:
            out.append([self.x_pos, self.y_pos + 1 * (-1 ** self.owner)])
        if self.x_pos < 7:
            out.append([self.x_pos + 1, self.y_pos + 1 * (-1 ** self.owner)])
        if self.x_pos > 0:
            out.append([self.x_pos - 1, self.y_pos + 1 * (-1 ** self.owner)])
        return out

    def up_cords(self, x, y):
        self.x_pos = x
        self.y_pos = y
        self.pos_mv = Pawn.possible_moves(self)

    def __str__(self):
        if self.owner:
            return 'P'
        return 'p'


class Rook:
    def __init__(self, x, y, player):
        self.x_pos = x
        self.y_pos = y
        self.owner = player
        self.pos_mv = Rook.possible_moves(self)

    def possible_moves(self):
        out = []
        for i in range(0, self.y_pos):
            out.append([self.x_pos, i])
        for i in range(self.y_pos + 1, 8):
            out.append([self.x_pos, i])
        for i in range(0, self.x_pos):
            out.append([i, self.y_pos])
        for i in range(self.x_pos + 1, 8):
            out.append([i, self.y_pos])
        return out

    def up_cords(self, x, y):
        self.x_pos = x
        self.y_pos = y
        self.pos_mv = Rook.possible_moves(self)

    def __str__(self):
        if self.owner:
            return 'R'
        return 'r'


class Knight:
    def __init__(self, x, y, player):
        self.x_pos = x
        self.y_pos = y
        self.owner = player
        self.pos_mv = Knight.possible_moves(self)

    def possible_moves(self):
        out = []
        out.append([self.x_pos + 2, self.y_pos + 1])
        out.append([self.x_pos + 2, self.y_pos - 1])
        out.append([self.x_pos + 1, self.y_pos + 2])
        out.append([self.x_pos + 1, self.y_pos - 2])
        out.append([self.x_pos - 2, self.y_pos + 1])
        out.append([self.x_pos - 2, self.y_pos - 1])
        out.append([self.x_pos - 1, self.y_pos + 2])
        out.append([self.x_pos - 1, self.y_pos - 2])
        out = list(filter(lambda x: -1 < x[0] < 8 and -1 < x[1] < 8, out))
        return out

    def up_cords(self, x, y):
        self.x_pos = x
        self.y_pos = y
        self.pos_mv = Knight.possible_moves(self)

    def __str__(self):
        if self.owner:
            return 'K'
        return 'k'


class Bishop:
    def __init__(self, x, y, player):
        self.x_pos = x
        self.y_pos = y
        self.owner = player
        self.pos_mv = Bishop.possible_moves(self)

    def possible_moves(self):
        out = []
        a = self.x_pos - 1
        b = self.y_pos - 1
        while a > -1 and b > -1:
            out.append([a, b])
            a -= 1
            b -= 1
        a = self.x_pos + 1
        b = self.y_pos - 1
        while a < 8 and b > -1:
            out.append([a, b])
            a += 1
            b -= 1
        a = self.x_pos + 1
        b = self.y_pos + 1
        while a < 8 and b < 8:
            out.append([a, b])
            a += 1
            b += 1
        a = self.x_pos - 1
        b = self.y_pos + 1
        while a > -1 and b < 8:
            out.append([a, b])
            a -= 1
            b += 1
        return out

    def up_cords(self, x, y):
        self.x_pos = x
        self.y_pos = y
        self.pos_mv = Bishop.possible_moves(self)

    def __str__(self):
        if self.owner:
            return 'B'
        return 'b'


class Queen:
    def __init__(self, x, y, player):
        self.x_pos = x
        self.y_pos = y
        self.owner = player
        self.pos_mv = Queen.possible_moves(self)

    def possible_moves(self):
        out = []
        for i in range(0, self.y_pos):
            out.append([self.x_pos, i])
        for i in range(self.y_pos + 1, 8):
            out.append([self.x_pos, i])
        for i in range(0, self.x_pos):
            out.append([i, self.y_pos])
        for i in range(self.x_pos + 1, 8):
            out.append([i, self.y_pos])
        a = self.x_pos - 1
        b = self.y_pos - 1
        while a > -1 and b > -1:
            out.append([a, b])
            a -= 1
            b -= 1
        a = self.x_pos + 1
        b = self.y_pos - 1
        while a < 8 and b > -1:
            out.append([a, b])
            a += 1
            b -= 1
        a = self.x_pos + 1
        b = self.y_pos + 1
        while a < 8 and b < 8:
            out.append([a, b])
            a += 1
            b += 1
        a = self.x_pos - 1
        b = self.y_pos + 1
        while a > -1 and b < 8:
            out.append([a, b])
            a -= 1
            b += 1
        return out

    def up_cords(self, x, y):
        self.x_pos = x
        self.y_pos = y
        self.pos_mv = Queen.possible_moves(self)

    def __str__(self):
        if self.owner:
            return 'Q'
        return 'q'


class King:
    def __init__(self, x, y, player):
        self.x_pos = x
        self.y_pos = y
        self.owner = player
        self.pos_mv = King.possible_moves(self)

    def possible_moves(self):
        out = []
        out.append([self.x_pos + 1, self.y_pos + 1])
        out.append([self.x_pos + 1, self.y_pos - 1])
        out.append([self.x_pos, self.y_pos + 1])
        out.append([self.x_pos, self.y_pos - 1])
        out.append([self.x_pos - 1, self.y_pos + 1])
        out.append([self.x_pos - 1, self.y_pos - 1])
        out.append([self.x_pos + 1, self.y_pos])
        out.append([self.x_pos - 1, self.y_pos])
        out = list(filter(lambda x: -1 < x[0] < 8 and -1 < x[1] < 8, out))
        return out

    def up_cords(self, x, y):
        self.x_pos = x
        self.y_pos = y
        self.pos_mv = King.possible_moves(self)

    def __str__(self):
        if self.owner:
            return 'W'
        return 'w'


fl_main = True
play = Chess()
play.fill()
print('Чтобы совершить ход введитите позицию из каторый хотите походить,\nа затем позицию куда хотите сходеть\n'
      'Это должно иметь следующий вид: A1 A5')
sl = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
while fl_main:
    play.show()
    fl = True
    while fl:
        i = input('Вверите всой ход\n').split()
        try:
            old_x = sl[i[0][0]]
            old_y = 8 - int(i[0][1])
            new_x = sl[i[1][0]]
            new_y = 8 - int(i[1][1])
            fl = not play.move(old_x, old_y, new_x, new_y)
        except KeyError:
            print('Вы вне игравого поля')
        except Exception as e:
            print('Вы явно ввели что-то не так', e)
    fl_main = play.king_life
    print(2 - play.player, 'gg')