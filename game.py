class Game:
    def __init__(self, id):
        self.nick_p0 = None
        self.nick_p1 = None
        self.time_for_change_card = None
        self.time_for_game = None
        self.p1Went = False
        self.p2Went = False
        self.ready = False
        self.id = id
        self.moves = [None, None]
        self.wins = [0, 0]
        self.ties = 0

        self.p0 = False
        self.p1 = True
        self.played0 = 0
        self.played1 = 0


        self.move0 = []
        self.move1 = []

        self.positions0 = []
        self.positions1 = []

        self.game_loop_p0 = False
        self.game_loop_p1 = False

    def game_start_data(self, p, nick, t1, t2):
        if p == 0:
            self.nick_p0 = nick
        else:
            self.nick_p1 = nick
        self.time_for_change_card = t1
        self.time_for_game = t2

    def game_start_data_client(self, p, nick):
        if p == 0:
            self.nick_p0 = nick
        else:
            self.nick_p1 = nick

    def game_loop(self, p):
        if p == 0:
            if self.game_loop_p0 is False:
                self.game_loop_p0 = True
            else:
                self.game_loop_p0 = False
        else:
            if self.game_loop_p1 is False:
                self.game_loop_p1 = True
            else:
                self.game_loop_p1 = False

    def both_game_loop(self):
        return self.game_loop_p0, self.game_loop_p1

    def played(self, p):
        if p == 0:
            self.played1 = 0
            self.move1.clear()
        else:
            self.played0 = 0
            self.move0.clear()

    def get_player_move(self, p):
        """
        :param p: [0,1]
        :return: Move
        """
        return self.moves[p]

    def play(self, player, move):
        self.moves[player] = move
        if player == 0:
            self.p1Went = True
        else:
            self.p2Went = True

    def connected(self):
        return self.ready

    def bothWent(self):
        return self.p1Went and self.p2Went

    def winner(self):

        p1 = self.moves[0].upper()[0]
        p2 = self.moves[1].upper()[0]

        winner = -1
        if p1 == "R" and p2 == "B":
            winner = 0
        elif p1 == "B" and p2 == "R":
            winner = 1

        return winner

    def resetWent(self):
        self.p1Went = False
        self.p2Went = False


    def false(self, p):
        if p == 0:
            self.p0 = False
            self.p1 = True

        else:
            self.p1 = False
            self.p0 = True


    def others(self, p):
        if p == 1:
            return self.p0
        else:
            return self.p1

    def cont_order(self, p):
        if p == 1:
            return self.p1
        else:
            return self.p0

    def control_position(self, p):
        if p == 0:
            if self.positions0 is not None:
                return True
            return False
        else:
            if self.positions1 is not None:
                return True
            return False

    def place_cards(self, data, p):
        if p == 0:
            self.positions0.append(data)
            if len(self.positions0) > 1:
                self.positions0.pop(0)
        else:
            self.positions1.append(data)
            if len(self.positions1) > 1:
                self.positions1.pop(0)

    def parse_data(self, data):
        try:
            d = self.split_data(data)
            return d
        except:
            return None

    def split_data(self, data):
        k = data.split(':')[1]

        number = []
        for j in range(0, 1000):
            number.append(str(j))

        t = []
        for i in range(len(k)):
            if k[i] in ['[', ']', '(', ')']:
                continue
            else:
                t.append(k[i])

        c = t.count(',')
        for i in range(c):
            t.remove(',')
        d = t.count(' ')
        for i in range(d):
            t.remove(' ')

        u = self.intt(t)
        son = []
        for i in range(12):
            son.append((u[0], u[1]))
            u.pop(0)
            u.pop(0)

        return son

    @staticmethod
    def intt(x):
        a = []
        y = ''
        for i in range(len(x)):
            y += str(x[i])
            if len(y) == 3:
                a.append(int(y))
                y = ''
        return a

    def move(self, p, data):
        d = self.remove(data)
        self.move_control(d, p)

    @staticmethod
    def remove(x):
        l = []
        t = ''
        for i in range(len(x)):

            if x[i] not in ['[', ']', ' ', ',', '(', ')', "'"]:

                t += str(x[i])

            else:
                if t != '':
                    l.append(t)
                    t = ''
        number = []
        for j in range(0, 1000):
            number.append(str(j))

        for i in l:
            if i in number:
                index = l.index(i)
                l[index] = int(i)
        return l

    def move_control(self, l, p):
        self.false(p)
        data = []
        a = len(l)//6
        for i in range(a):
            k = l[i*6: ((i+1)*6)]
            data.append(k)
        if p == 0:
            self.move0.append(data)
            self.played0 = 1

        else:
            self.move1.append(data)
            self.played1 = 1


    def send_data(self, p):
        if p == 1:
            return self.move0
        else:
            return self.move1

    def restart_game(self):

        self.p1Went = False
        self.p2Went = False
        self.moves = [None, None]
        self.wins = [0, 0]
        self.ties = 0

        self.p0 = False
        self.p1 = True
        self.played0 = 0
        self.played1 = 0

        self.move0 = []
        self.move1 = []

        self.positions0 = []
        self.positions1 = []

        self.game_loop_p0 = False
        self.game_loop_p1 = False



