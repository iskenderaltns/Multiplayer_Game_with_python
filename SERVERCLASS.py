import socket
from _thread import *
import pickle
from game import Game

class Server:
    def __init__(self):

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = socket.gethostbyname(socket.gethostname())
        self.port = 5552

        try:
            self.s.bind((self.server, self.port))
        except socket.error as e:
            str(e)

        self.s.listen(2)
        print("Waiting for a connection, Server Started")

        self.connected = set()
        self.games = {}
        self.idCount = 0
        self.pos = ["0:50,50", "1:100,100"]

    def threaded_client(self, conn, p, gameId):

        conn.send(str.encode(str(p)))

        reply = ''
        while True:
            try:
                data = conn.recv(4096).decode()

                if gameId in self.games:
                    game = self.games[gameId]

                    if not data:
                        break
                    else:
                        if data == "reset":
                            game.resetWent()
                        elif data != "get" and data[0:3] != '0:(' and data[0:3] != '1:(' and data[0] not in ['p', 's',
                                                                                                             'c', 't',
                                                                                                             'h', 'j',
                                                                                                             'a']:
                            game.play(p, data)

                        elif data[0:3] == '0:(' or data[0:3] == '1:(':
                            arr = data.split(":")
                            id = int(arr[0])
                            game.place_cards(arr[1], id)
                        elif data[0] == 'p':
                            arr = data.split(":")
                            id = int(arr[1])
                            game.move(id, arr[2])
                            print('p', id)
                        elif data[0] == 't':
                            arr = data.split(":")
                            id = int(arr[1])
                            game.played(id)
                        elif data[0] == 'c':
                            arr = data.split(":")
                            id = int(arr[1])
                            game.game_loop(id)
                        elif data[0] == 'j':
                            arr = data.split(":")
                            id = int(arr[1])
                            nick = arr[2]
                            t1 = int(arr[3])
                            t2 = int(arr[4])
                            game.game_start_data(id, nick, t2, t1)
                        elif data[0] == 'h':
                            arr = data.split(":")
                            id = int(arr[1])
                            nick = arr[2]
                            game.game_start_data_client(id, nick)

                        elif data[0] == 'a':
                            game.restart_game()
                        conn.sendall(pickle.dumps(game))

            except:
                break

        print("Lost connection")
        try:
            del self.games[gameId]
            print("Closing Game", gameId)
        except:
            pass
        self.idCount -= 1
        conn.close()

    def start(self):
        while True:
            conn, addr = self.s.accept()
            print("Connected to:", addr)

            self.idCount += 1
            p = 0
            gameId = (self.idCount - 1) // 2
            if self.idCount % 2 == 1:
                self.games[gameId] = Game(gameId)
                print("Creating a new game...")
            else:
                self.games[gameId].ready = True
                p = 1

            start_new_thread(self.threaded_client, (conn, p, gameId))



