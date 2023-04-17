from tkinter import *
import socket
from tkinter import messagebox
from _thread import *
import pickle
from game import Game
class Server(Frame):
    def __init__(self, main_screen):
        Frame.__init__(self, main_screen, padx=20, pady=20)
        main_screen.wm_iconbitmap('servericon.ico')
        main_screen.title("Server")
        main_screen.minsize(width=300, height=300)
        main_screen.geometry("300x300")
        self.pack()
        self.info = "Waiting for a connection, Server Started"
        self.addr_list = [None, None]
        self.control = True
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = socket.gethostbyname(socket.gethostname())
        self.port = None
        self.port_var = StringVar()
        self.port_Label = Label(self, relief=GROOVE, text='Entry Port', bg='lemon chiffon')
        self.port_Label.grid(row=0, column=0)
        self.port_entry = Entry(self, textvariable=self.port_var, font=('calibre', 10, 'normal'))
        self.port_entry.grid(row=0, column=1)

        self.start_Label = Label(self, relief=GROOVE, width=20, bg="green")
        self.start_Button = Button(self.start_Label, text='Start Server', command=self.start_server, bg='orange')
        self.start_Label.grid(row=2, column=1)
        self.start_Button.pack()


        self.photo_smile = PhotoImage(file='smile.png')
        self.photo_smile_resizing = self.photo_smile.subsample(10, 10)
        self.photo_sad = PhotoImage(file='sad.png')
        self.photo_sad_resizing = self.photo_sad.subsample(10, 10)

        self.player_0 = Button(self, text='  Player 0\nNon Connected\n', relief=GROOVE, width=120, height=120, bg='snow4', image=self.photo_sad_resizing, compound=TOP)
        self.player_1 = Button(self, text='  Player 1\nNon Connected\n', relief=GROOVE, width=120, height=120, bg='snow4', image=self.photo_sad_resizing, compound=TOP)
        self.info_label = Label(self, text='Both Player are connected', relief='flat', width=200, height=30, bg='gray94', font=('consolos', '9'))


        self.selectableMsg = Text(self, width=35, height=2, relief='flat', bg='gray94', wrap='word', font=('consolos', '9'))

        self.connected = set()
        self.games = {}
        self.idCount = 0

    def restart(self):
        self.port = None
        self.port_var = StringVar()
        self.port_Label = Label(self, relief=GROOVE, text='Entry Port', bg='lemon chiffon')
        self.port_Label.grid(row=0, column=0)
        self.port_entry = Entry(self, textvariable=self.port_var, font=('calibre', 10, 'normal'))
        self.port_entry.grid(row=0, column=1)

        self.start_Label = Label(self, relief=GROOVE, width=20, bg="green")
        self.start_Button = Button(self.start_Label, text='Start Server', command=self.start_server, bg='orange')
        self.start_Label.grid(row=2, column=1)
        self.start_Button.pack()

    def start_server(self):
        a = str(self.port_var.get())

        try:
            if int(a) in range(4000, 6000):
                self.start_Button.destroy()
                self.start_Label.destroy()
                self.port_Label.destroy()
                self.port_entry.destroy()
                self.port = int(a)
                self.kaos()
            else:
                messagebox.showerror('Server Error', 'Error: Please, Entry port number between 4000 and 6000!')
        except ValueError:
            messagebox.showerror('Server Error', 'Error: Please, Entry just number!')


    def kaos(self):
        try:
            self.s.bind((self.server, self.port))
        except socket.error as e:
            str(e)
        try:
            self.s.listen(2)
            start_new_thread(self.start, ())
        except OSError:
            messagebox.showerror('Server Error', 'Error: Please, This port is full. Try another port!')
            self.restart()


    def threaded_client(self, conn, p, gameId):

        conn.send(str.encode(str(p)))


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
                            if id == 0:
                                self.player_0.config(bg='yellow')
                                self.player_1.config(bg='green yellow')
                            else:
                                self.player_1.config(bg='yellow')
                                self.player_0.config(bg='green yellow')
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

        self.info = 'Lost Connection'
        self.selectableMsg.config(state='normal')
        self.selectableMsg.delete("0.0", "end")
        self.selectableMsg.insert("end", self.info)
        self.selectableMsg.configure(state='disabled')
        try:
            del self.games[gameId]
            if gameId == 0:
                self.player_0.config(text='  Player 0\n Closed game:\n', image=self.photo_sad_resizing, bg='gray94')
                self.player_1.config(bg='gray94')
            else:
                self.player_1.config(text='  Player 1\n Closed game:\n', image=self.photo_sad_resizing, bg='gray94')
                self.player_0.config(bg='gray94')
        except:
            pass
        self.idCount -= 1
        conn.close()

    def start(self):

        while True:

            self.selectableMsg.insert(1.0, self.info)
            self.selectableMsg.configure(state='disabled')
            self.selectableMsg.pack(pady=5)
            self.player_0.pack(side=LEFT)
            self.player_1.pack(side=RIGHT)

            conn, addr = self.s.accept()

            self.idCount += 1
            self.addr_list[self.idCount-1] = str(addr)

            if self.addr_list[0] is not None:
                self.player_0.config(text='  Player 0\n Connected to:\n'+str(self.addr_list[0]), image=self.photo_smile_resizing, bg='green yellow')

            if self.addr_list[1] is not None:
                self.info = 'Both Player are connected'
                self.selectableMsg.config(state='normal')
                self.selectableMsg.delete("0.0", "end")
                self.selectableMsg.insert("end", self.info)
                self.selectableMsg.configure(state='disabled')

                self.player_1.config(text='  Player 1\n Connected to:\n'+str(self.addr_list[1]), image=self.photo_smile_resizing, bg='green yellow')


            p = 0
            gameId = (self.idCount - 1) // 2
            if self.idCount % 2 == 1:
                self.games[gameId] = Game(gameId)
            else:
                self.games[gameId].ready = True
                p = 1

            start_new_thread(self.threaded_client, (conn, p, gameId))


root = Tk()
app = Server(root)
app.mainloop()
