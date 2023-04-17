import pygame
import random
from pygame.locals import *
from ships import Ship
from shipmiss import ShipMiss
from arms_and_player import Arm, Player
from button import Button
import socket
import pickle
from game import Game
class Buttons:
    def __init__(self, text, x, y, color):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.width = 150
        self.height = 50


    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont("comicsans", 20)
        text = font.render(self.text, 1, (255, 255, 255))
        win.blit(text, (self.x + round(self.width/2) - round(text.get_width()/2), self.y + round(self.height/2) - round(text.get_height()/2)))

    def click(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height:
            return True
        else:
            return False

class BattleShip:

    def __init__(self):
        self.lost = False
        self.win = False
        self.restart = False
        self.dat = 0
        self.start_time = None
        self.collided_enemies_3 = None
        self.remaining_time = None
        self.elapsed_time = None
        self.c_pt_or_cw = None
        self.c_r_or_ttc = None
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = None
        self.port = None
        self.addr = None
        self.p = None
        self.player = None
        self.game = None
        self.nick_name_others = None
        self.start_time_1 = None
        self.start_time_2 = None
        self.collided_enemies_2 = None
        self.collided_enemies = None
        self.column = None
        self.row = None
        self.start = True
        self.start_2 = True
        self.teams = False
        self.teams_2 = True
        self.changee = True
        self.start_color = None
        self.prop_white_to_red = 0
        self.sup_power = 0
        pygame.font.init()
        pygame.display.set_caption('BattleShip')
        pygame.mixer.init()
        self.window_width = 1200
        self.window_height = 800
        self.x = 190
        self.y = 120
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        self.new_window = pygame.display.set_mode((self.window_width, self.window_height))

        self.font_1 = pygame.font.SysFont('arial', 30)
        self.font_2 = pygame.font.SysFont('arial', 50)
        self.text_1 = self.font_1.render("0000", 1, (0, 0, 0))
        self.text_2 = self.font_1.render("0000.", 1, (0, 0, 0))
        self.clock = pygame.time.Clock()

        pygame.time.set_timer(pygame.USEREVENT, 1000)

        self.start_background = pygame.image.load('startbg.png')
        self.start_background = pygame.transform.scale(self.start_background, (self.window_width, self.window_height))

        self.background = pygame.image.load("thunderstorm-at-sea-sounds.jpg")
        self.background = pygame.transform.scale(self.background, (self.window_width, self.window_height))
        self.attention = pygame.image.load('attention.png')
        self.attention = pygame.transform.scale(self.attention, (30, 30))
        self.change_card_back_sound = pygame.mixer.Sound('ocean-wave-1.wav')

        self.S1 = Ship((150, 150), 2, "r", 1, 1)
        self.S2 = Ship((4 * 50 + self.x, 150), 3, "r", 2, 1)
        self.S3 = Ship((5 * 50 + 2 * self.x, 150), 4, "r", 3, 1)
        self.S4 = Ship((6 * 50 + 3 * self.x, 150), 5, "r", 4, 1)
        self.S5 = Ship((150, 4 * 50 + self.y), 3, "w", 5, 1)

        self.M1 = ShipMiss((4 * 50 + self.x, 4 * 50 + self.y), 0, 1, 1)
        self.M2 = ShipMiss((5 * 50 + 2 * self.x, 4 * 50 + self.y), 0, 1, 2)
        self.M3 = ShipMiss((6 * 50 + 3 * self.x, 4 * 50 + self.y), 0, 1, 3)
        self.M4 = ShipMiss((150, 5 * 50 + 2 * self.y), 0, 1, 4)
        self.M5 = ShipMiss((4 * 50 + self.x, 5 * 50 + 2 * self.y), 0, 1, 5)
        self.M6 = ShipMiss((5 * 50 + 2 * self.x, 5 * 50 + 2 * self.y), 0, 1, 6)
        self.M7 = ShipMiss((6 * 50 + 3 * self.x, 5 * 50 + 2 * self.y), 0, 1, 7)

        self.ships = [self.S1, self.S2, self.S3, self.S4, self.S5, self.M1, self.M2, self.M3, self.M4, self.M5, self.M6, self.M7]
        self.list_ship_coo = [(150, 150), (390, 150), (630, 150), (870, 150),
                              (150, 320), (390, 320), (630, 320), (870, 320),
                              (150, 490), (390, 490), (630, 490), (870, 490)]
        self.S1c = Ship((150, 150), 2, "r", 1, 0)
        self.S2c = Ship((4 * 50 + self.x, 150), 3, "r", 2, 0)
        self.S3c = Ship((5 * 50 + 2 * self.x, 150), 4, "r", 3, 0)
        self.S4c = Ship((6 * 50 + 3 * self.x, 150), 5, "r", 4, 0)
        self.S5c = Ship((150, 4 * 50 + self.y), 3, "w", 5, 0)

        self.M1c = ShipMiss((4 * 50 + self.x, 4 * 50 + self.y), 0, 0, 1)
        self.M2c = ShipMiss((5 * 50 + 2 * self.x, 4 * 50 + self.y), 0, 0, 2)
        self.M3c = ShipMiss((6 * 50 + 3 * self.x, 4 * 50 + self.y), 0, 0, 3)
        self.M4c = ShipMiss((150, 5 * 50 + 2 * self.y), 0, 0, 4)
        self.M5c = ShipMiss((4 * 50 + self.x, 5 * 50 + 2 * self.y), 0, 0, 5)
        self.M6c = ShipMiss((5 * 50 + 2 * self.x, 5 * 50 + 2 * self.y), 0, 0, 6)
        self.M7c = ShipMiss((6 * 50 + 3 * self.x, 5 * 50 + 2 * self.y), 0, 0, 7)

        self.Card1 = Arm((670, 650), 2, "r", 0)
        self.Card2 = Arm((770, 650), 1, "w", 0)
        self.Card3 = Arm((370, 650), 1, "r", 0)
        self.Card4 = Arm((470, 650), 4, "r", 0)
        self.Card5 = Arm((570, 650), 0, "s", 0)
        self.Card6 = Arm((870, 650), 0, 'r_or_ttc', 0)
        self.Card7 = Arm((270, 650), 0, 'pt_or_cw', 0)

        self.total_number_cards = self.Card1.number + self.Card2.number + self.Card3.number + self.Card4.number + \
                                  self.Card5.number + self.Card6.number + self.Card7.number
        self.list_peg_cards_coordinates = [(370, 650), (470, 650), (570, 650), (670, 650), (770, 650), (870, 650)]
        self.list_peg_cards = [[2, "r"], [2, "r"], [2, "r"], [2, "r"], [2, "r"], [1, "r"], [1, "r"], [1, "r"], [1, "r"],
                               [1, "r"], [1, "w"], [1, "w"], [1, "w"], [1, "w"], [1, "w"], [1, "w"], [1, "w"], [1, "w"],
                               [1, "w"], [0, "s"], [0, "s"], [0, "c_or_pt"], [0, "c_or_pt"], [0, "ttc_or_r"],
                               [2, "ttc_or_r"]]
        self.list_peg_cards_2 = [self.Card1, self.Card1, self.Card1, self.Card1, self.Card1, self.Card2, self.Card2,
                                 self.Card2, self.Card2, self.Card2, self.Card2, self.Card2, self.Card2, self.Card2,
                                 self.Card3, self.Card3, self.Card3, self.Card3, self.Card3, self.Card4, self.Card4,
                                 self.Card5, self.Card5, self.Card6, self.Card6, self.Card7, self.Card7]

        self.all_sprites = pygame.sprite.Group()
        self.Ships_groups = pygame.sprite.Group(self.S1, self.S2, self.S3, self.S4, self.S5, self.M1, self.M2, self.M3,
                                                self.M4, self.M5, self.M6, self.M7)
        self.all_sprites.add(self.Ships_groups)
        self.Player = Player((0, 0), self.all_sprites)
        self.list_client = [self.S1c, self.S2c, self.S3c, self.S4c, self.S5c, self.M1c, self.M2c, self.M3c,
                            self.M4c, self.M5c, self.M6c, self.M7c]
        self.Ships_groups_client = pygame.sprite.Group(self.S1c, self.S2c, self.S3c, self.S4c, self.S5c, self.M1c,
                                                       self.M2c, self.M3c, self.M4c, self.M5c, self.M6c, self.M7c)
        self.card_groups = pygame.sprite.Group(self.Card1, self.Card2, self.Card3, self.Card4, self.Card5, self.Card6,
                                               self.Card7)
        self.all_sprites_2 = pygame.sprite.Group()
        self.all_sprites_2.add(self.card_groups)
        self.all_sprites_2.add(self.Ships_groups_client)
        self.Player_2 = Player((0, 0), self.all_sprites_2)
        self.Player_3 = Player((0, 0), self.all_sprites)

        self.Button_1 = Button((100, 100), 1, 0)
        self.button_1 = self.Button_1.call_button()
        self.Button_2 = Button((100, 100), 2, 0)
        self.button_2 = self.Button_2.call_button()
        self.Button_3 = Button((100, 100), 3, 0)
        self.button_3 = self.Button_3.call_button()
        self.Button_4 = Button((100, 100), 4, 0)
        self.button_4 = self.Button_4.call_button()
        self.Button_5 = Button((100, 100), 5, 0)
        self.button_5 = self.Button_5.call_button()

        self.button_6 = Button((50, 50), 6, 0).call_button()
        self.button_7 = Button((50, 50), 7, 0).call_button()
        self.button_8 = Button((50, 50), 8, 0).call_button()
        self.button_9 = Button((80, 80), 9, 0).call_button()

        self.button_random_img = pygame.image.load('buttonrandom.png')
        self.button_random_img = pygame.transform.scale(self.button_random_img, (100, 50))
        self.button_random = Rect(550, 700, 100, 50)

        self.button_ok_img = pygame.image.load('buttonok.png')
        self.button_ok_img = pygame.transform.scale(self.button_ok_img, (75, 50))
        self.button_ok = Rect(1000, 700, 75, 50)

        self.main_base_img = pygame.image.load('harmor.png')
        self.main_base_img = pygame.transform.scale(self.main_base_img, (50, 50))
        self.main_base_rect = self.main_base_img.get_rect()
        self.main_base_rect.topleft = (1050, 680)
        self.center_main_base = self.main_base_rect.center

        self.img_return = pygame.image.load('return.jpg')
        self.img_return = pygame.transform.scale(self.img_return, (50, 50))
        self.button_return = self.img_return.get_rect()
        self.button_return.topleft = (50, 680)
        self.center_return = self.button_return.center

        self.img_return_2 = pygame.image.load('return_but.png')
        self.img_return_2 = pygame.transform.scale(self.img_return_2, (75, 50))
        self.button_return_2 = Rect(1000, 700, 75, 50)

        self.setting = False
        self.setting_button = self.button_7.get_rect()
        self.setting_button.topleft = (1100, 50)
        self.setting_base_bg = pygame.image.load('Resim1.jpg')
        self.setting_base_bg = pygame.transform.scale(self.setting_base_bg, (self.window_width, self.window_height))

        self.button_1_rect = self.button_1.get_rect()
        self.button_1_rect.topleft = (250, 20)
        self.center_button_1 = self.button_1_rect.center

        self.button_2_rect = self.button_2.get_rect()
        self.button_2_rect.topleft = (400, 20)
        self.center_button_2 = self.button_2_rect.center

        self.button_3_rect = self.button_3.get_rect()
        self.button_3_rect.topleft = (550, 20)
        self.center_button_3 = self.button_3_rect.center

        self.button_4_rect = self.button_4.get_rect()
        self.button_4_rect.topleft = (700, 20)
        self.center_button_4 = self.button_4_rect.center

        self.button_5_rect = self.button_5.get_rect()
        self.button_5_rect.topleft = (850, 20)
        self.center_button_5 = self.button_5_rect.center

        self.button_8_rect = self.button_8.get_rect()
        self.button_8_rect.topleft = (100, 680)
        self.center_button_8 = self.button_8_rect.center

        self.button_9_rect = self.button_9.get_rect()
        self.button_9_rect.topleft = (580, 700)
        self.center_button_9 = self.button_9_rect.center

        self.r_u_w = 0
        self.repair_using_white_bool = False

        self.player_1 = Rect(450, 700, 100, 50)
        self.player_2 = Rect(650, 700, 100, 50)

        self.list_control = []
        self.list_control_2 = []
        self.repair_shield_control = []
        self.a = None
        self.b = None
        self.c = None
        self.player_choose = None
        self.start_number_of_cards = 5
        self.number_of_cards = 0
        self.list_c = self.list_arms_cards()

        self.bool_r_or_ttc = False
        self.bool_pt_or_cw = False
        self.repair = pygame.image.load('repair.png')
        self.repair = pygame.transform.scale(self.repair, (270, 200))
        self.ttc = pygame.image.load('ttc.png')
        self.ttc = pygame.transform.scale(self.ttc, (270, 200))
        self.r_repair = pygame.rect.Rect(500, 220, 270, 200)
        self.r_ttc = pygame.rect.Rect(500, 420, 270, 200)
        self.pt = pygame.image.load('pt.png')
        self.pt = pygame.transform.scale(self.pt, (270, 200))
        self.cw = pygame.image.load('cw.png')
        self.cw = pygame.transform.scale(self.cw, (270, 200))
        self.r_pt = Rect(500, 220, 270, 200)
        self.r_cw = Rect(500, 420, 270, 200)
        self.up = 0
        self.down = 0
        self.decide = 0

        self.see_main_base = True
        self.see_game_area = True

        self.clock_image = pygame.image.load('timeclock.png')
        self.clock_image = pygame.transform.scale(self.clock_image, (100, 100))
        self.tick_yes = pygame.image.load('tick.png')
        self.tick_yes = pygame.transform.scale(self.tick_yes, (20, 20))
        self.tick_no = pygame.image.load('tıck2.png')
        self.tick_no = pygame.transform.scale(self.tick_no, (20, 20))
        self.seat = pygame.image.load('seat.png')
        self.seat = pygame.transform.scale(self.seat, (40, 40))
        self.seat_button = self.seat.get_rect()
        self.seat_button.topleft = (50, 100)
        self.center_seat = self.seat_button.center

        self.move_data = []
        self.h_m_t = 0
        self.data_client = []
        self.data_client_ships = []

        self.btns = [Buttons("Red", 450, 700, (255, 0, 0)), Buttons("Blue", 650, 700, (0, 0, 255))]

        self.font_1 = pygame.font.SysFont('arial', 20)
        self.start_background = pygame.image.load('startbg1.png')
        self.start_background = pygame.transform.scale(self.start_background, (self.window_width, self.window_height))
        self.new_game_bg = pygame.image.load('df1.png')
        self.new_game_bg = pygame.transform.scale(self.new_game_bg, (self.window_width, self.window_height))
        self.img_button_ok = pygame.image.load('buttonok.png')
        self.img_button_ok = pygame.transform.scale(self.img_button_ok, (60, 40))
        self.button_ok_rect = pygame.Rect(800, 540, 60, 40)
        self.new_game_text = self.font_1.render("New Game", 1, (0, 0, 0))
        self.join_game_text = self.font_1.render("Join Game", 1, (255, 255, 255))
        self.bool_new_game = False
        self.bool_join_game = False
        self.posx = None
        self.posy = None
        self.bool_nick_name = False
        self.bool_time_for_change_card = False
        self.bool_time_for_game = False
        self.bool_client_ip = False
        self.bool_port = False
        self.nick_name_text = self.font_1.render("Nickname :", 1, (255, 255, 255))
        self.time_for_change_card_text = self.font_1.render("Card Shuffle Time :", 1, (255, 255, 255))
        self.time_for_game_text = self.font_1.render("Time of Move :", 1, (255, 255, 255))
        self.client_ip_text = self.font_1.render("Client IP :", 1, (255, 255, 255))
        self.port_text = self.font_1.render("Port :", 1, (255, 255, 255))
        self.port_input = ''
        self.port_default = "5552"
        self.client_ip = ''
        self.time_for_game = ''
        self.time_for_change_card = ''
        self.nick_name = ''
        self.nick_name_default = 'creator'
        self.time_for_change_card_default = '30'
        self.time_for_game_default = '20'
        self.nick_name_client_default = 'client'
        self.client_ip_default = str(socket.gethostbyname(socket.gethostname()))
        self.nick_input_rect = pygame.Rect(520, 295, 140, 30)
        self.time_1_input_rect = pygame.Rect(520, 345, 140, 30)
        self.time_2_input_rect = pygame.Rect(520, 395, 140, 30)
        self.client_ip_rect = pygame.Rect(520, 345, 140, 30)
        self.port_rect = pygame.Rect(520,445, 140, 30)
        self.client_port_rect = pygame.Rect(520, 395, 140, 30)

        self.how_image = pygame.image.load('how.jpg')
        self.how_image = pygame.transform.scale(self.how_image, (50, 50))
        self.bool_how = False
        self.color_active = pygame.Color(255, 200, 12)
        self.color_passive = pygame.Color(12, 200, 10)
        self.color = self.color_passive
        self.color_2 = self.color_passive
        self.color_3 = self.color_passive
        self.color_4 = self.color_passive
        self.active = False
        self.active_2 = False
        self.active_3 = False
        self.active_4 = False
        self.number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.error_msg = False
        self.img_tick_no = pygame.image.load('tıck2.png')
        self.img_tick_no = pygame.transform.scale(self.img_tick_no, (40, 40))
        self.tick_no = pygame.Rect(860, 200, 40, 40)
        self.text = ''

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(4096).decode()
        except:
            pass

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return pickle.loads(self.client.recv(2048 * 2))
        except socket.error as e:
            print(e)

    def draw_start(self):

        self.window.blit(self.start_background, (0, 0))
        if self.start_2 is not False:
            pygame.draw.rect(self.window, (205, 205, 14), (80, 630, 120, 40))
            self.window.blit(self.new_game_text, (100, 640))
            pygame.draw.rect(self.window, (15, 5, 14), (80, 680, 120, 40))
            self.window.blit(self.join_game_text, (100, 690))
            self.window.blit(self.button_9, self.button_9_rect)
            pygame.draw.circle(self.window, (205, 205, 0), self.center_button_9, 40, 1)
            self.window.blit(self.how_image, (1100, 30))

        else:
            font_1 = pygame.font.SysFont('arial', 30)
            pygame.draw.rect(self.window, (205, 205, 0), (520, 650, 200, 100))
            t = font_1.render('Play', 1, (139, 54, 38))
            self.window.blit(t, (590, 680))
        self.clock.tick(60)
        pygame.display.update()

    def start_loop(self):
        if self.start is not False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.posx, self.posy = event.pos
                    if self.start_2 is not False:
                        if self.posx in range(80, 200) and self.posy in range(630, 670):
                            self.bool_new_game = True
                            self.start = False
                        elif self.posx in range(80, 200) and self.posy in range(680, 720):
                            self.bool_join_game = True
                            self.start = False

                        elif self.posx in range(1100, 1150) and self.posy in range(30, 80):
                            self.bool_how = True
                            self.start = False
                    else:
                        if self.posx in range(520, 720) and self.posy in range(650, 750):
                            self.teams = True
                            self.start = False


            self.draw_start()
        else:
            if self.bool_new_game is not False:
                self.new_game()

            if self.bool_join_game is not False:
                self.join_game()

            if self.bool_how is not False:
                self.how_to_play()

            if self.teams is not False:
                self.main()

    def how_to_play(self):
        if self.bool_how is not False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_return_2.collidepoint(event.pos):
                        self.start = True
                        self.bool_how  = False
            self.draw_how()
        else:
            self.start_loop()
    def draw_how(self):
        self.window.blit(self.new_game_bg, (0, 0))
        self.clock.tick(60)
        pygame.draw.rect(self.window, (255, 0, 3), self.button_return_2)
        self.window.blit(self.img_return_2, self.button_return_2)
        pygame.display.update()
    def draw_new_game(self):
        self.window.blit(self.new_game_bg, (0, 0))
        self.clock.tick(60)

        pygame.draw.rect(self.window, (61, 61, 61), (300, 200, 600, 400))
        pygame.draw.rect(self.window, (115, 115, 115), (300, 200, 600, 40))
        pygame.draw.rect(self.window, (207, 207, 207), self.tick_no)
        self.window.blit(self.img_tick_no, self.tick_no)
        pygame.draw.rect(self.window, (207, 207, 207), self.button_ok_rect)
        self.window.blit(self.img_button_ok, self.button_ok_rect)
        pygame.draw.rect(self.window, (15, 5, 14), (350, 290, 150, 40))
        self.window.blit(self.nick_name_text, (360, 300))
        pygame.draw.rect(self.window, (15, 5, 14), (350, 340, 150, 40))
        self.window.blit(self.time_for_change_card_text, (360, 350))
        pygame.draw.rect(self.window, (15, 5, 14), (350, 390, 150, 40))
        self.window.blit(self.time_for_game_text, (360, 400))
        pygame.draw.rect(self.window, (15, 5, 14), (350, 440, 150, 40))
        self.window.blit(self.port_text, (360, 450))

        pygame.draw.rect(self.window, self.color, self.nick_input_rect)
        if self.nick_name == '':
            text_surface = self.font_1.render(self.nick_name_default, True, (255, 255, 255))

        else:
            text_surface = self.font_1.render(self.nick_name, True, (255, 255, 255))
        self.window.blit(text_surface, (self.nick_input_rect.x + 5, self.nick_input_rect.y + 5))
        self.nick_input_rect.w = max(100, text_surface.get_width() + 10)

        pygame.draw.rect(self.window, self.color_2, self.time_1_input_rect)
        if self.time_for_change_card == '':
            text_surface_2 = self.font_1.render(self.time_for_change_card_default, True, (255, 255, 255))
        else:
            text_surface_2 = self.font_1.render(self.time_for_change_card, True, (255, 255, 255))
        self.window.blit(text_surface_2, (self.time_1_input_rect.x + 5, self.time_1_input_rect.y + 5))
        self.time_1_input_rect.w = max(100, text_surface_2.get_width() + 10)

        pygame.draw.rect(self.window, self.color_3, self.time_2_input_rect)
        if self.time_for_game == '':
            text_surface_3 = self.font_1.render(self.time_for_game_default, True, (255, 255, 255))
        else:
            text_surface_3 = self.font_1.render(self.time_for_game, True, (255, 255, 255))
        self.window.blit(text_surface_3, (self.time_2_input_rect.x + 5, self.time_2_input_rect.y + 5))
        self.time_2_input_rect.w = max(100, text_surface_3.get_width() + 10)

        pygame.draw.rect(self.window, self.color_4, self.port_rect)
        if self.port_input == '':
            text_surface_4 = self.font_1.render(self.port_default, True, (255, 255, 255))
        else:
            text_surface_4 = self.font_1.render(self.port_input, True, (255, 255, 255))
        self.window.blit(text_surface_4, (self.port_rect.x + 5, self.port_rect.y + 5))
        self.port_rect.w = max(100, text_surface_4.get_width() + 10)

        if self.text != '':
            error_text = self.font_1.render(self.text, 1, (0, 5, 55))

            pygame.draw.rect(self.window, (201, 11, 130),
                             (380, 280, 200, 100))
            self.window.blit(error_text, (400, 300))
        pygame.display.flip()
        pygame.display.update()

    def new_game(self):
        if self.bool_new_game is not False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.text = ''
                    if self.nick_input_rect.collidepoint(event.pos):
                        self.bool_nick_name = True
                        self.bool_time_for_change_card = False
                        self.bool_time_for_game = False
                        self.active = True
                        self.active_2 = False
                        self.active_3 = False
                        self.bool_port = False
                        self.active_4 = False
                    elif self.time_1_input_rect.collidepoint(event.pos):
                        self.bool_time_for_change_card = True
                        self.bool_nick_name = False
                        self.bool_time_for_game = False
                        self.active_2 = True
                        self.active_3 = False
                        self.active = False
                        self.bool_port = False
                        self.active_4 = False
                    elif self.time_2_input_rect.collidepoint(event.pos):
                        self.bool_nick_name = False
                        self.bool_time_for_change_card = False
                        self.bool_time_for_game = True
                        self.active_3 = True
                        self.active = False
                        self.active_2 = False
                        self.bool_port = False
                        self.active_4 = False
                    elif self.port_rect.collidepoint(event.pos):
                        self.bool_nick_name = False
                        self.bool_time_for_change_card = False
                        self.bool_time_for_game = False
                        self.bool_port = True
                        self.active_4 = True
                        self.active_3 = False
                        self.active = False
                        self.active_2 = False
                    elif self.tick_no.collidepoint(event.pos):
                        self.bool_nick_name = False
                        self.bool_time_for_change_card = False
                        self.bool_time_for_game = False
                        self.active = False
                        self.active_2 = False
                        self.active_3 = False
                        self.bool_port = False
                        self.active_4 = False
                        self.bool_new_game = False
                        self.start = True
                    elif self.button_ok_rect.collidepoint(event.pos):
                        #self.net = Network(str(socket.gethostbyname(socket.gethostname())))
                        #self.player = int(self.net.getP())
                        if self.port_input == '':
                            self.port_input = self.port_default
                        self.port = int(self.port_input)
                        self.server = socket.gethostbyname(socket.gethostname())
                        self.addr = (self.server, self.port)
                        self.p = self.connect()
                        self.player = int(self.p)
                        self.game = self.send('get')
                        if self.nick_name == '':
                            self.nick_name = self.nick_name_default
                        if self.time_for_change_card == '':
                            self.time_for_change_card = self.time_for_change_card_default
                        if self.time_for_game == '':
                            self.time_for_game = self.time_for_game_default

                        self.bool_new_game = False
                        self.start_2 = False
                        self.start = True

                    else:
                        self.bool_nick_name = False
                        self.bool_time_for_change_card = False
                        self.bool_time_for_game = False
                        self.active = False
                        self.active_2 = False
                        self.active_3 = False
                        self.bool_port = False
                        self.active_4 = False

                if event.type == pygame.KEYDOWN:
                    if self.bool_nick_name:
                        if event.key == pygame.K_BACKSPACE:
                            self.nick_name = self.nick_name[:-1]
                        else:
                            self.nick_name += event.unicode

                    if self.bool_time_for_game:
                        if event.key == pygame.K_BACKSPACE:
                            self.time_for_game = self.time_for_game[:-1]
                        else:
                            if event.unicode in self.number:
                                self.text = ''
                                self.time_for_game += event.unicode

                            else:
                                self.text = 'Please Entry Number'


                    elif self.bool_time_for_change_card:
                        if event.key == pygame.K_BACKSPACE:
                            self.time_for_change_card = self.time_for_change_card[:-1]
                        else:
                            if event.unicode in self.number:
                                self.text = ''
                                self.time_for_change_card += event.unicode
                            else:
                                self.text = 'Please Entry Number'

                    elif self.bool_port:
                        if event.key == pygame.K_BACKSPACE:
                            self.port_input = self.port_input[:-1]
                        else:
                            if event.unicode in self.number:
                                self.text = ''
                                self.port_input += event.unicode
                            else:
                                self.text = 'Please Entry Number'

            if self.bool_time_for_game is False and self.time_for_game != '':
                if int(self.time_for_game) < 10:
                    self.text = 'The move time cannot be less than 10 seconds.'
                elif int(self.time_for_game) > 50:
                    self.text = 'The move time cannot exceed 50 seconds.'
                else:
                    self.text = ''
            if self.bool_time_for_change_card is False and self.time_for_change_card != '':
                if int(self.time_for_change_card) < 10:
                    self.text = 'The move time cannot be less than 10 seconds.'
                elif int(self.time_for_change_card) > 30:
                    self.text = 'The move time cannot exceed 30 seconds.'
                else:
                    self.text = ''
            if self.active:
                self.color = self.color_active
            else:
                self.color = self.color_passive
            if self.active_2:
                self.color_2 = self.color_active
            else:
                self.color_2 = self.color_passive
            if self.active_3:
                self.color_3 = self.color_active
            else:
                self.color_3 = self.color_passive

            if self.active_4:
                self.color_4 = self.color_active
            else:
                self.color_4 = self.color_passive
            self.draw_new_game()
        else:
            self.start_loop()

    def draw_join_game(self):
        self.window.blit(self.new_game_bg, (0, 0))
        pygame.draw.rect(self.window, (61, 61, 61), (300, 200, 600, 400))
        pygame.draw.rect(self.window, (115, 115, 115), (300, 200, 600, 40))
        pygame.draw.rect(self.window, (207, 207, 207), self.tick_no)
        self.window.blit(self.img_tick_no, self.tick_no)
        pygame.draw.rect(self.window, (207, 207, 207), self.button_ok_rect)
        self.window.blit(self.img_button_ok, self.button_ok_rect)
        pygame.draw.rect(self.window, (15, 5, 14), (350, 290, 150, 40))
        self.window.blit(self.nick_name_text, (360, 300))
        pygame.draw.rect(self.window, (15, 5, 14), (350, 340, 150, 40))
        self.window.blit(self.client_ip_text, (360, 350))
        pygame.draw.rect(self.window, (15, 5, 14), (350, 390, 150, 40))
        self.window.blit(self.port_text, (360, 400))

        pygame.draw.rect(self.window, self.color, self.nick_input_rect)
        if self.nick_name == '':
            text_surface = self.font_1.render(self.nick_name_client_default, True, (255, 255, 255))
        else:
            text_surface = self.font_1.render(self.nick_name, True, (255, 255, 255))
        self.window.blit(text_surface, (self.nick_input_rect.x + 5, self.nick_input_rect.y + 5))
        self.nick_input_rect.w = max(100, text_surface.get_width() + 10)

        pygame.draw.rect(self.window, self.color_2, self.client_ip_rect)
        if self.client_ip == '':
            text_surface_2 = self.font_1.render(self.client_ip_default, True, (255, 255, 255))
        else:
            text_surface_2 = self.font_1.render(self.client_ip, True, (255, 255, 255))
        self.window.blit(text_surface_2, (self.client_ip_rect.x + 5, self.client_ip_rect.y + 5))
        self.client_ip_rect.w = max(100, text_surface_2.get_width() + 10)

        pygame.draw.rect(self.window, self.color_4, self.client_port_rect)
        if self.port_input == '':
            text_surface_4 = self.font_1.render(self.port_default, True, (255, 255, 255))
        else:
            text_surface_4 = self.font_1.render(self.port_input, True, (255, 255, 255))
        self.window.blit(text_surface_4, (self.client_port_rect.x + 5, self.client_port_rect.y + 5))
        self.client_port_rect.w = max(100, text_surface_4.get_width() + 10)

        if self.text != '':
            error_text = self.font_1.render(self.text, 1, (0, 5, 55))

            pygame.draw.rect(self.window, (201, 11, 130),
                             (380, 280, 200, 100))
            self.window.blit(error_text, (400, 300))
        self.clock.tick(60)
        pygame.display.update()

    def join_game(self):
        if self.bool_join_game is not False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.text = ''
                    if self.nick_input_rect.collidepoint(event.pos):
                        self.bool_nick_name = True
                        self.bool_client_ip = False
                        self.active = True
                        self.active_2 = False
                        self.bool_port = False
                        self.active_4 = False
                    elif self.client_ip_rect.collidepoint(event.pos):
                        self.bool_client_ip = True
                        self.bool_nick_name = False
                        self.active_2 = True
                        self.active = False
                        self.bool_port = False
                        self.active_4 = False
                    elif self.client_port_rect.collidepoint(event.pos):
                        self.bool_nick_name = False
                        self.bool_client_ip = False
                        self.bool_port = True
                        self.active_4 = True
                        self.active = False
                        self.active_2 = False

                    elif self.tick_no.collidepoint(event.pos):
                        self.bool_nick_name = False
                        self.bool_client_ip = False
                        self.active = False
                        self.active_2 = False
                        self.bool_port = False
                        self.active_4 = False
                        self.bool_join_game = False
                        self.start = True
                    elif self.button_ok_rect.collidepoint(event.pos):
                        # self.net = Network(str(self.client_ip))
                        # self.player = int(self.net.getP())
                        if self.port_input == '':
                            self.port_input = self.port_default
                        self.port = int(self.port_input)
                        self.server = str(self.client_ip)
                        self.addr = (self.server, self.port)
                        self.p = self.connect()
                        self.player = int(self.p)
                        self.game = self.send('get')

                        if self.nick_name == '':
                            self.nick_name = self.nick_name_client_default

                        self.bool_join_game = False
                        self.start_2 = False
                        self.start = True

                    else:
                        self.bool_nick_name = False
                        self.bool_client_ip = False
                        self.active = False
                        self.active_2 = False
                        self.bool_port = False
                        self.active_4 = False

                if event.type == pygame.KEYDOWN:
                    if self.bool_nick_name:
                        if event.key == pygame.K_BACKSPACE:
                            self.nick_name = self.nick_name[:-1]
                        else:
                            self.nick_name += event.unicode

                    elif self.bool_client_ip:
                        if event.key == pygame.K_BACKSPACE:
                            self.client_ip = self.client_ip[:-1]
                        else:
                            self.client_ip += event.unicode
                    elif self.bool_port:
                        if event.key == pygame.K_BACKSPACE:
                            self.port_input = self.port_input[:-1]
                        else:
                            if event.unicode in self.number:
                                self.text = ''
                                self.port_input += event.unicode
                            else:
                                self.text = 'Please Entry Number'

            if self.active:
                self.color = self.color_active
            else:
                self.color = self.color_passive
            if self.active_2:
                self.color_2 = self.color_active
            else:
                self.color_2 = self.color_passive
            if self.active_4:
                self.color_4 = self.color_active
            else:
                self.color_4 = self.color_passive

            self.draw_join_game()
        else:
            self.start_loop()

    def redrawWindow(self):
        self.window.blit(self.start_background, (0, 0))

        if not (self.game.connected()):
            text = self.font_1.render("Waiting for Player...", 1, (255, 0, 0), True)
            self.window.blit(text, (510, 610))
        else:

            move1 = self.game.get_player_move(0)
            move2 = self.game.get_player_move(1)
            if self.game.bothWent():
                text1 = self.font_1.render('Locked In', 1, (0, 0, 0))
                text2 = self.font_1.render('Locked In', 1, (0, 0, 0))
            else:
                if self.game.p1Went and self.player == 0:
                    text1 = self.font_1.render('Selected', 1, (0, 0, 0))
                elif self.game.p1Went:
                    text1 = self.font_1.render("Locked In", 1, (0, 0, 0))
                else:
                    text1 = self.font_1.render("Waiting...", 1, (0, 0, 0))

                if self.game.p2Went and self.player == 1:
                    text2 = self.font_1.render('Selected', 1, (0, 0, 0))
                elif self.game.p2Went:
                    text2 = self.font_1.render("Locked In", 1, (0, 0, 0))
                else:
                    text2 = self.font_1.render("Waiting...", 1, (0, 0, 0))

            if self.player == 1:
                self.window.blit(text1, (480, 630))
                self.window.blit(text2, (680, 630))
            else:
                self.window.blit(text2, (680, 630))
                self.window.blit(text1, (480, 630))

            for btn in self.btns:
                btn.draw(self.window)

        pygame.display.update()

    def main(self):
        if self.teams_2 is not False:
            self.clock.tick(60)
            try:
                self.game = self.send("get")
            except:
                self.teams_2 = False

            if self.game.bothWent():
                self.redrawWindow()
                pygame.time.delay(500)

                font = pygame.font.SysFont("comicsans", 40)
                if (self.game.winner() == 1 and self.player == 1) or (self.game.winner() == 0 and self.player == 0):
                    text = font.render("You are Red! Game is Starting...", 1, (255, 0, 0))
                    self.teams_2 = False
                    self.start_color = 0


                elif self.game.winner() == -1:
                    text = font.render("Both of you don't choose same team!", 1, (255, 0, 0))
                    self.game = self.send("reset")
                else:
                    text = font.render("You are Blue! Game is Starting...", 1, (255, 0, 0))
                    self.teams_2 = False
                    self.start_color = 1

                self.window.blit(text, (
                    self.window_width / 2 - text.get_width() / 2, self.window_height / 2 - text.get_height() / 2))
                pygame.display.update()
                pygame.time.delay(2000)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    for btn in self.btns:
                        if btn.click(pos) and self.game.connected():
                            if self.player == 0:
                                if self.time_for_game != '' and self.time_for_change_card != '':
                                    self.send('j' + ':' + str(self.player) + ':' + str(self.nick_name) + ":" + str(self.time_for_game) + ":" + str(self.time_for_change_card))
                                else:
                                    self.send('h' + ':' + str(self.player) + ':' + str(self.nick_name))
                                if not self.game.p1Went:
                                    self.send(btn.text)

                            else:
                                if self.time_for_game != '' and self.time_for_change_card != '':
                                    self.send('j' + ':' + str(self.player) + ':' + str(self.nick_name) + ":" + str(self.time_for_game) + ":" + str(self.time_for_change_card))
                                else:
                                    self.send('h' + ':' + str(self.player) + ':' + str(self.nick_name))
                                if not self.game.p2Went:
                                    self.send(btn.text)
            if self.player == 0 and self.game.nick_p1 is not None:
                self.nick_name_others = self.game.nick_p1
            if self.player == 1 and self.game.nick_p0 is not None:
                self.nick_name_others = self.game.nick_p0
            if self.game.time_for_game is not None and self.game.time_for_game is not None:

                self.start_time_1 = int(self.game.time_for_change_card)
                self.start_time_2 = int(self.game.time_for_game)

            self.redrawWindow()

        else:
            self.remaining_time = self.start_time_1
            self.game_loop()

    def menu_screen(self):
        if self.start is not False:
            self.clock.tick(60)
            self.window.fill((128, 128, 128))
            font = pygame.font.SysFont("comicsans", 60)
            text = font.render("Click to Play!", 1, (255, 0, 0))
            self.window.blit(text, (100, 200))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.start = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.start = False


        else:
            self.main()

    def list_arms_cards(self):
        list_kaos = []
        for i in range(5):
            random.shuffle(self.list_peg_cards_2)
            random.shuffle(self.list_peg_cards_2)
            random.shuffle(self.list_peg_cards_2)
            list_kaos.extend(self.list_peg_cards_2)
        return list_kaos

    def draw_setting_area(self):
        self.window.blit(self.setting_base_bg, (0, 0))
        self.window.blit(self.img_return, self.button_return)
        self.window.blit(self.seat, self.seat_button)

        pygame.display.update()

    def setting_area(self):
        if self.setting is not False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.Player.rect.center = event.pos

                    if self.Player.rect.x in range(self.button_return.x,
                                                     self.button_return.x + self.button_return.width):
                        if self.Player.rect.y in range(self.setting_button.y,
                                                       self.button_return.y + self.button_return.height):
                            self.setting = False
                            self.start = True

            self.draw_setting_area()
        else:
            self.start_loop()

    def draw(self):
        self.window.blit(self.background, (0, 0))
        self.all_sprites.draw(self.window)
        if self.start_time_1 > 10:
            text = self.font_2.render(str(int(self.start_time_1)), True, (255, 255, 255))
            text_rect = text.get_rect()
            text_rect.center = (600, 80)
            self.window.blit(self.clock_image, (550, 30))
            self.window.blit(text, text_rect)  # draw the remaining time on the screen
        if self.start_time_1 <= 10:
            text = self.font_2.render(str(int(self.start_time_1)), True, (255, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = (600, 80)
            self.window.blit(self.clock_image, (550, 30))
            self.window.blit(text, text_rect)  # draw the remaining time on the screen

        if self.start_color is not None:
            for i in range(len(self.list_client)):
                self.list_client[i].sw(self.start_color)

        # draw rect
        if self.collided_enemies is not None:
            for select in self.collided_enemies:
                if select not in self.list_control:
                    self.list_control.append(select)
                    if len(self.list_control) == 2:
                        self.change()
                    else:
                        continue
        if (self.player == 0 and self.game.game_loop_p0 is False) or (self.player == 1 and self.game.game_loop_p1 is False):
            pygame.draw.rect(self.window, (255, 0, 3), self.button_random)
            self.window.blit(self.button_random_img, self.button_random)

            pygame.draw.rect(self.window, (255, 0, 3), self.button_ok)
            self.window.blit(self.button_ok_img, self.button_ok)

        if (self.player == 0 and self.game.game_loop_p0) or (self.player == 1 and self.game.game_loop_p1):
            pygame.draw.rect(self.window, (255, 0, 3), self.button_return_2)
            self.window.blit(self.img_return_2, self.button_return_2)

        if self.game.game_loop_p0 and self.game.game_loop_p1:
            self.window.blit(self.attention, (50, 720))
            text = self.font_1.render('Game is Starting....', 1, (0, 0, 0))
            self.window.blit(text, (80, 700))

        if self.player == 0:
            if self.game.game_loop_p0 and self.game.game_loop_p1 is False:
                self.window.blit(self.attention, (40, 710))
                text_1 = self.font_1.render('You are Ready, Waiting for ' + str(self.nick_name_others), 1, (250, 250, 250))
                self.window.blit(text_1, (80, 700))
            if self.game.game_loop_p1 and self.game.game_loop_p0 is False:
                self.window.blit(self.attention, (40, 710))
                text_1 = self.font_1.render(str(self.nick_name_others) + ' is Ready', 1, (250, 250, 250))
                self.window.blit(text_1, (80, 700))
        else:
            if self.game.game_loop_p1 and self.game.game_loop_p0 is False:
                self.window.blit(self.attention, (40, 710))
                text_1 = self.font_1.render('You are Ready, Waiting for ' + str(self.nick_name_others), 1, (250, 250, 250))
                self.window.blit(text_1, (80, 700))
            if self.game.game_loop_p0 and self.game.game_loop_p1 is False:
                self.window.blit(self.attention, (40, 710))
                text_1 = self.font_1.render(str(self.nick_name_others) + ' is Ready', 1, (250, 250, 250))
                self.window.blit(text_1, (80, 700))



        self.clock.tick(60)
        pygame.display.update()

    def game_loop(self):

        if self.changee is not False:
            try:
                data = str(self.p) + ":" + str(self.S1.rect.topleft) + "," + str(self.S2.rect.topleft) + ',' + str(
                    self.S3.rect.topleft) + ',' + str(self.S4.rect.topleft) + ',' + str(
                    self.S5.rect.topleft) + ',' + str(
                    self.M1.rect.topleft) + ',' + str(self.M2.rect.topleft) + ',' + str(
                    self.M3.rect.topleft) + ',' + str(
                    self.M4.rect.topleft) + ',' + str(self.M5.rect.topleft) + ',' + str(
                    self.M6.rect.topleft) + ',' + str(
                    self.M7.rect.topleft)
                self.game = self.send(data)
            except:
                self.changee = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.USEREVENT:
                    self.start_time_1 -= 1
                    if self.start_time_1 <= 0:
                        self.kaos()
                        self.changee = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.Player.rect.center = event.pos
                    if (self.player == 0 and self.game.game_loop_p0 is False) or (
                            self.player == 1 and self.game.game_loop_p1 is False):
                        if self.Player.rect.x in range(self.button_random.x,
                                                       self.button_random.x + self.button_random.width):
                            if self.Player.rect.y in range(self.button_random.y,
                                                           self.button_random.y + self.button_random.height):
                                self.random_change()
                        elif self.Player.rect.x in range(self.button_ok.x, self.button_ok.x + self.button_ok.width):
                            if self.Player.rect.y in range(self.button_ok.y, self.button_ok.y + self.button_ok.height):
                                self.kaos()
                                self.game = self.send("c" + ":" + str(self.p))


                        self.collided_enemies = pygame.sprite.spritecollide(self.Player, self.Ships_groups, False)
                    else:
                        if self.Player.rect.x in range(self.button_return_2.x, self.button_return_2.x + self.button_return_2.width):
                            if self.Player.rect.y in range(self.button_return_2.y, self.button_return_2.y + self.button_return_2.height):
                                self.game = self.send("c" + ":" + str(self.p))

            if self.game.game_loop_p1 and self.game.game_loop_p0:
                self.kaos()
                self.changee = False
                pygame.time.delay(1000)
            self.all_sprites.update()
            # self.change_card_back_sound.play()
            self.kaos()
            self.draw()

        else:
            # self.change_card_back_sound.stop()

            self.game_loop_2()

    def kaos(self):
        if self.player == 0:
            if self.game.control_position(1):
                self.data_client_ships = self.game.positions1
                self.S1c.rect.topleft, self.S2c.rect.topleft, self.S3c.rect.topleft, self.S4c.rect.topleft, self.S5c.rect.topleft, \
                self.M1c.rect.topleft, self.M2c.rect.topleft, self.M3c.rect.topleft, self.M4c.rect.topleft, self.M5c.rect.topleft, \
                self.M6c.rect.topleft, self.M7c.rect.topleft = self.parse_data(self.game.positions1)
            else:
                return False

        else:
            if self.game.control_position(0):
                self.data_client_ships = self.game.positions0
                self.S1c.rect.topleft, self.S2c.rect.topleft, self.S3c.rect.topleft, self.S4c.rect.topleft, self.S5c.rect.topleft, \
                self.M1c.rect.topleft, self.M2c.rect.topleft, self.M3c.rect.topleft, self.M4c.rect.topleft, self.M5c.rect.topleft, \
                self.M6c.rect.topleft, self.M7c.rect.topleft = self.parse_data(self.game.positions0)

            else:
                return False

    def parse_data(self, data):
        try:
            d = self.split_data(data)
            return d[0], d[1], d[2], d[3], d[4], d[5], d[6], d[7], d[8], d[9], d[10], d[11]
        except:
            return self.list_ship_coo[0], self.list_ship_coo[1], self.list_ship_coo[2], self.list_ship_coo[3], \
                   self.list_ship_coo[4], self.list_ship_coo[5], self.list_ship_coo[6], self.list_ship_coo[7], \
                   self.list_ship_coo[8], self.list_ship_coo[9], self.list_ship_coo[10], self.list_ship_coo[11]

    def split_data(self, data):
        k = data[0]

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

    def change(self):
        a, b = self.list_control[0], self.list_control[1]
        a.rect.topleft, b.rect.topleft = b.rect.topleft, a.rect.topleft
        self.collided_enemies = None
        self.list_control.clear()

    def random_change(self):
        for i in range(len(self.Ships_groups)):
            j = random.randint(0, 11)
            k = random.randint(0, 11)
            r_0 = self.Ships_groups.sprites()[j]
            r_1 = self.Ships_groups.sprites()[k]
            r_0.rect.topleft, r_1.rect.topleft = r_1.rect.topleft, r_0.rect.topleft

    def draw_main_game(self):

        self.window.blit(self.background, (0, 0))
        self.all_sprites_2.draw(self.window)

        if self.number_of_cards < self.start_number_of_cards:
            self.card_add(self.start_number_of_cards - self.number_of_cards)
            self.number_of_cards = self.start_number_of_cards

        self.win_lost()
        if self.win_lost_restart():
            font_1 = pygame.font.SysFont('arial', 30)
            pygame.draw.rect(self.window, (205, 205, 0), (520, 450, 200, 100))
            t = font_1.render('Restart', 1, (139, 54, 38))
            self.window.blit(t, (590, 480))
        else:
            if self.h_m_t != 0:
                text_2 = "Your turn "
                font_1 = pygame.font.SysFont('arial', 30)

                t2 = font_1.render(text_2, 1, (255, 254, 238))

                self.window.blit(t2, (20, 20))
            else:
                text = str(self.nick_name_others) + " is playing "
                font_1 = pygame.font.SysFont('arial', 30)
                t = font_1.render(text, 1, (255, 254, 38))
                self.window.blit(t, (20, 20))

        if self.match() is True:
            self.action()

        if self.bool_pt_or_cw is True:
            if self.up == 1 and self.down == 0:
                pygame.draw.rect(self.window, (0, 0, 255), self.r_pt)
                self.window.blit(self.pt, self.r_pt)
                pygame.draw.rect(self.window, (150, 150, 10), self.r_pt, 5)
                pygame.draw.rect(self.window, (255, 0, 0), self.r_cw)
                self.window.blit(self.cw, self.r_cw)
            elif self.up == 0 and self.down == 1:
                pygame.draw.rect(self.window, (0, 0, 255), self.r_pt)
                self.window.blit(self.pt, self.r_pt)
                pygame.draw.rect(self.window, (255, 0, 0), self.r_cw)
                self.window.blit(self.cw, self.r_cw)
                pygame.draw.rect(self.window, (150, 150, 10), self.r_cw, 5)
            else:
                pygame.draw.rect(self.window, (0, 0, 255), self.r_pt)
                self.window.blit(self.pt, self.r_pt)
                pygame.draw.rect(self.window, (255, 0, 0), self.r_cw)
                self.window.blit(self.cw, self.r_cw)
        if self.bool_r_or_ttc is True:
            if self.up == 1 and self.down == 0:
                pygame.draw.rect(self.window, (0, 0, 255), self.r_repair)
                self.window.blit(self.repair, self.r_repair)
                pygame.draw.rect(self.window, (150, 150, 10), self.r_repair, 5)
                pygame.draw.rect(self.window, (255, 0, 0), self.r_ttc)
                self.window.blit(self.ttc, self.r_ttc)
            elif self.up == 0 and self.down == 1:
                pygame.draw.rect(self.window, (0, 0, 255), self.r_repair)
                self.window.blit(self.repair, self.r_repair)
                pygame.draw.rect(self.window, (255, 0, 0), self.r_ttc)
                self.window.blit(self.ttc, self.r_ttc)
                pygame.draw.rect(self.window, (150, 150, 10), self.r_ttc, 5)
            else:
                pygame.draw.rect(self.window, (0, 0, 255), self.r_repair)
                self.window.blit(self.repair, self.r_repair)
                pygame.draw.rect(self.window, (255, 0, 0), self.r_ttc)
                self.window.blit(self.ttc, self.r_ttc)




        self.window.blit(self.main_base_img, self.main_base_rect)
        pygame.draw.circle(self.window, (205, 205, 0), self.center_main_base, 30, 5)
        self.window.blit(self.button_1, self.button_1_rect)
        pygame.draw.circle(self.window, (205, 205, 0), self.center_button_1, 50, 1)
        self.window.blit(self.button_2, self.button_2_rect)
        pygame.draw.circle(self.window, (205, 205, 0), self.center_button_2, 50, 1)
        self.window.blit(self.button_3, self.button_3_rect)
        pygame.draw.circle(self.window, (205, 205, 0), self.center_button_3, 50, 1)
        self.window.blit(self.button_4, self.button_4_rect)
        pygame.draw.circle(self.window, (205, 205, 0), self.center_button_4, 50, 1)
        self.window.blit(self.button_5, self.button_5_rect)
        pygame.draw.circle(self.window, (205, 205, 0), self.center_button_5, 50, 1)


        self.draw_prop_2()



        self.clock.tick(60)
        pygame.display.update()

    def control_order(self):
        if len(self.data_client) != 0:
            played = 't' + ":" + str(self.p)
            a = self.data_client[-1]
            if self.player == 0 and self.game.played1 == 1:
                self.kaos_3(a)
                self.game = self.send(played)
            elif self.player == 1 and self.game.played0 == 1:
                self.kaos_3(a)
                self.game = self.send(played)

        if self.h_m_t == 0 and len(self.move_data) != 0:
            if self.game.cont_order(self.player) is True and self.game.others(self.player) is False:
                # play
                data = 'p' + ":" + str(self.p) + ":" + str(self.move_data)
                self.game = self.send(data)
                self.move_data.clear()

        if self.h_m_t == 0 and len(self.move_data) == 0:
            if self.game.others(self.player) is False and self.game.cont_order(self.player):
                self.h_m_t = 1

        else:
            self.game = self.send("get")

    def game_loop_2(self):
        if self.see_game_area is not False:
            try:
                self.game = self.send("get")
            except:
                self.see_game_area = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                elif event.type == pygame.KEYDOWN:
                    if self.bool_pt_or_cw or self.bool_r_or_ttc:
                        if event.key == pygame.K_UP:
                            self.up = 1
                            self.down = 0
                        elif event.key == pygame.K_DOWN:
                            self.down = 1
                            self.up = 0
                        elif event.key == pygame.K_SPACE:
                            self.decide = 1
                            self.choose()
                            self.bool_r_or_ttc = False
                            self.bool_pt_or_cw = False
                    if self.b is not None:
                        if event.key == pygame.K_BACKSPACE or event.key == pygame.K_DELETE:
                            self.pass_card()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.b is not None:
                        if self.b.prop == 'pt_or_cw' or self.b.prop == 'r_or_ttc':
                            self.bool_r_or_ttc = False
                            self.bool_pt_or_cw = False
                            self.collided_enemies = None
                            self.collided_enemies_2 = None
                            self.b = None
                            self.up = None
                            self.down = None
                            self.list_control.clear()
                            self.list_control_2.clear()
                    self.Player_2.rect.center = event.pos
                    if self.win_lost_restart():
                        if self.Player_2.rect.centerx in range(520, 720) and self.Player_2.rect.centery in range(450, 550):
                            self.send('a' + ':' + str(self.player))
                            self.see_game_area = False
                            self.restart = True

                    if self.in_circle(self.Player_2.rect.centerx, self.Player_2.rect.centery) is True:
                        self.see_game_area = False
                        self.see_main_base = True
                    if (self.player == 0 and self.game.p0) or (self.player == 1 and self.game.p1):
                        self.bool_r_or_ttc = False
                        self.bool_pt_or_cw = False
                        if self.repair_using_white_bool is True:
                            if self.button_8_rect.collidepoint(event.pos) and self.Card2.number != 0:
                                self.r_u_w = 1
                                self.see_game_area = False
                                self.see_main_base = True
                        self.collided_enemies_2 = pygame.sprite.spritecollide(self.Player_2, self.card_groups, False)

                        if len(self.list_control_2) != 0:
                            self.collided_enemies = pygame.sprite.spritecollide(self.Player_2, self.Ships_groups_client,
                                                                                False)
                        else:
                            self.collided_enemies = None
            self.control_order()
            self.data_client = self.game.send_data(self.player)

            self.all_sprites.update()
            self.all_sprites_2.update()
            self.draw_main_game()

        else:
            if self.restart:
                self.reset()
                self.main()
            else:
                self.open_harbor()

    def repair_using_white(self):
        self.c.health_change(self.c.health+1)
        self.move_data.append(['repair', 1, self.c.health, self.c.rect.topleft, self.c.cover])
        self.h_m_t -= 1
        self.Card2.change_number(-1)
        self.number_of_cards -= 1
        self.collided_enemies = None
        self.collided_enemies_2 = None
        self.collided_enemies_3 = None
        self.a = None
        self.b = None
        self.c = None
        self.up = None
        self.down = None
        self.r_u_w = 0
        self.list_control.clear()
        self.list_control_2.clear()
        self.repair_shield_control.clear()
        self.see_game_area = True
        self.see_main_base = False

    def find_ship(self, x):
        ships = [self.S1, self.S2, self.S3, self.S4, self.S5, self.M1, self.M2, self.M3, self.M4, self.M5, self.M6,
                      self.M7]
        ships_coordinate = [self.S1.rect.topleft, self.S2.rect.topleft, self.S3.rect.topleft, self.S4.rect.topleft,
                                 self.S5.rect.topleft,
                                 self.M1.rect.topleft, self.M2.rect.topleft, self.M3.rect.topleft, self.M4.rect.topleft,
                                 self.M5.rect.topleft,
                                 self.M6.rect.topleft, self.M7.rect.topleft]
        index = None
        for cor in ships_coordinate:
            if x[0] == cor[0] and x[1] == cor[1]:
                index = ships_coordinate.index(cor)
        if index is not None:
            return ships[index]
        else:
            return False

    def find_ship_client(self, x):
        ships_client = [self.S1c, self.S2c, self.S3c, self.S4c, self.S5c, self.M1c, self.M2c, self.M3c, self.M4c,
                             self.M5c, self.M6c, self.M7c]
        ships_client_coordinate = [self.S1c.rect.topleft, self.S2c.rect.topleft, self.S3c.rect.topleft,
                                        self.S4c.rect.topleft,
                                        self.S5c.rect.topleft,
                                        self.M1c.rect.topleft, self.M2c.rect.topleft, self.M3c.rect.topleft,
                                        self.M4c.rect.topleft,
                                        self.M5c.rect.topleft,
                                        self.M6c.rect.topleft, self.M7c.rect.topleft]
        index = None
        for cor in ships_client_coordinate:
            if x[0] == cor[0] and x[1] == cor[1]:
                index = ships_client_coordinate.index(cor)
        if index is not None:
            return ships_client[index]
        else:
            return False

    def kaos_3(self, data):
        data_client = data
        a = len(data_client)
        for i in range(a):
            prop = data_client[i][0]
            power = data_client[i][1]
            x = data_client[i][3]
            y = data_client[i][4]
            health = data_client[i][2]
            if prop == 'w' or prop == 'r':
                ship = self.find_ship((int(x), int(y)))
                if health != 'miss' and ship.shield == 0:
                    ship.seen()
                    ship.which_card_was_hit_with(int(power))
                    ship.health_change(int(health))
                elif ship.shield != 0 and ship.prop == 'w' and health != 'miss':
                    ship.health_change(int(power))
                else:
                    ship.seen()
                    ship.opening()
            else:

                if prop == 's':

                    c = (int(x), int(y))
                    ship = self.find_ship_client(c)

                    if health != 'miss':
                        ship.shield_change()

                elif prop == 'r_or_ttc':

                    c = (int(x), int(y))
                    ship = self.find_ship_client(c)

                    if health != "miss":
                        ship.health_change(health)

                else:
                    print("nothing")

    def in_circle(self, x, y):
        if (x - self.center_main_base[0])**2 + (y - self.center_main_base[1])**2 <= 900:
            return True
        else:
            return False

    def in_circle_2(self, x, y):
        if (x-self.center_return[0])**2 + (y - self.center_return[1])**2 <= 900:
            return True
        else:
            return False

    def draw_prop(self):

        if self.S1c.cover == 1 and self.S1c.health > 0:
            self.button_1 = self.Button_1.call_button_2()
            self.window.blit(self.button_1, self.button_1_rect)
            pygame.draw.circle(self.window, (205, 205, 0), self.center_button_1, 50, 1)
        if self.S1c.cover == 0 or self.S1c.health <= 0:
            self.button_1 = self.Button_1.call_button()
            self.window.blit(self.button_1, self.button_1_rect)
            pygame.draw.circle(self.window, (205, 205, 0), self.center_button_1, 50, 1)
        if self.S2c.cover == 1 and self.S2c.health > 0:
            self.button_2 = self.Button_2.call_button_2()
            self.window.blit(self.button_2, self.button_2_rect)
            pygame.draw.circle(self.window, (205, 205, 0), self.center_button_2, 50, 1)
        if self.S2c.cover == 0 or self.S2c.health <= 0:
            self.button_2 = self.Button_2.call_button()
            self.window.blit(self.button_2, self.button_2_rect)
            pygame.draw.circle(self.window, (205, 205, 0), self.center_button_2, 50, 1)
        if self.S3c.cover == 1 and self.S3c.health > 0:
            self.button_3 = self.Button_3.call_button_2()
            self.window.blit(self.button_3, self.button_3_rect)
            pygame.draw.circle(self.window, (205, 205, 0), self.center_button_3, 50, 1)
        if self.S3c.cover == 0 or self.S3c.health <= 0:
            self.button_3 = self.Button_3.call_button()
            self.window.blit(self.button_3, self.button_3_rect)
            pygame.draw.circle(self.window, (205, 205, 0), self.center_button_3, 50, 1)
        if self.S4c.cover == 1 and self.S4c.health > 0:
            self.button_4 = self.Button_4.call_button_2()
            self.window.blit(self.button_4, self.button_4_rect)
            pygame.draw.circle(self.window, (205, 205, 0), self.center_button_4, 50, 1)
        if self.S4c.cover == 0 or self.S4c.health <= 0:
            self.button_4 = self.Button_4.call_button()
            self.window.blit(self.button_4, self.button_4_rect)
            pygame.draw.circle(self.window, (205, 205, 0), self.center_button_4, 50, 1)
        if self.S5c.cover == 1 and self.S5c.health > 0:
            self.button_5 = self.Button_5.call_button_2()
            self.window.blit(self.button_5, self.button_5_rect)
            pygame.draw.circle(self.window, (205, 205, 0), self.center_button_5, 50, 1)
        if self.S5c.cover == 0 or self.S5c.health <= 0:
            self.button_5 = self.Button_5.call_button()
            self.window.blit(self.button_5, self.button_5_rect)
            pygame.draw.circle(self.window, (205, 205, 0), self.center_button_5, 50, 1)

    def draw_prop_2(self):
        if self.S1.seen_control == 1 and self.S1.health > 0:

            self.button_1 = self.Button_1.call_button_2()
            self.window.blit(self.button_1, self.button_1_rect)
            pygame.draw.circle(self.window, (205, 205, 0), self.center_button_1, 50, 1)
            self.repair_using_white_bool = True
            self.window.blit(self.button_8, self.button_8_rect)
            pygame.draw.circle(self.window, (205, 205, 0), self.center_button_8, 40, 1)

        if self.S1.seen_control == 0 or self.S1.health <= 0:
            self.repair_using_white_bool = False
            self.button_1 = self.Button_1.call_button()
            self.window.blit(self.button_1, self.button_1_rect)
            pygame.draw.circle(self.window, (205, 205, 0), self.center_button_1, 50, 1)
        if self.S2.seen_control == 1 and self.S2.health > 0:
            self.prop_white_to_red = 1
            self.button_2 = self.Button_2.call_button_2()
            self.window.blit(self.button_2, self.button_2_rect)
            pygame.draw.circle(self.window, (205, 205, 0), self.center_button_2, 50, 1)
        if self.S2.seen_control == 0 or self.S2.health <= 0:
            self.prop_white_to_red = 0
            self.button_2 = self.Button_2.call_button()
            self.window.blit(self.button_2, self.button_2_rect)
            pygame.draw.circle(self.window, (205, 205, 0), self.center_button_2, 50, 1)
        if self.S3.seen_control == 1 and self.S3.health > 0:
            self.sup_power = 1
            self.button_3 = self.Button_3.call_button_2()
            self.window.blit(self.button_3, self.button_3_rect)
            pygame.draw.circle(self.window, (205, 205, 0), self.center_button_3, 50, 1)
        if self.S3.seen_control == 0 or self.S3.health <= 0:
            self.sup_power = 0
            self.button_3 = self.Button_3.call_button()
            self.window.blit(self.button_3, self.button_3_rect)
            pygame.draw.circle(self.window, (205, 205, 0), self.center_button_3, 50, 1)
        if self.S4.seen_control == 1 and self.S4.health > 0:
            self.start_number_of_cards = 7
            self.button_4 = self.Button_4.call_button_2()
            self.window.blit(self.button_4, self.button_4_rect)
            pygame.draw.circle(self.window, (205, 205, 0), self.center_button_4, 50, 1)
        if self.S4.seen_control == 0 or self.S4.health <= 0:
            self.start_number_of_cards = 5
            self.button_4 = self.Button_4.call_button()
            self.window.blit(self.button_4, self.button_4_rect)
            pygame.draw.circle(self.window, (205, 205, 0), self.center_button_4, 50, 1)
        if self.S5.seen_control == 1 and self.S5.health > 0:
            self.button_5 = self.Button_5.call_button_2()
            self.window.blit(self.button_5, self.button_5_rect)
            pygame.draw.circle(self.window, (205, 205, 0), self.center_button_5, 50, 1)
        if self.S5.seen_control == 0 or self.S5.health <= 0:
            self.button_5 = self.Button_5.call_button()
            self.window.blit(self.button_5, self.button_5_rect)
            pygame.draw.circle(self.window, (205, 205, 0), self.center_button_5, 50, 1)

    def draw_open_harbor(self):
        self.window.blit(self.background, (0, 0))
        self.all_sprites.draw(self.window)

        for i in self.ships:
            if i.seen_control == 1:
                pygame.draw.rect(self.window, (15, 150, 10), i.rect, 5)

        if self.match_2() is True:
            self.repair_or_shield()

        if self.match_3() is True:
            self.repair_using_white()

        self.window.blit(self.img_return, self.button_return)
        pygame.draw.circle(self.window, (205, 205, 0), self.center_return, 30, 5)

        self.draw_prop()
        self.clock.tick(60)
        pygame.display.update()

    def open_harbor(self):

        if self.see_main_base is not False:
            try:
                self.game = self.send("get")
            except:
                self.see_game_area = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.Player_3.rect.center = event.pos
                    if self.in_circle_2(self.Player_3.rect.centerx, self.Player_3.rect.centery) is True:
                        self.see_main_base = False
                        self.see_game_area = True
                    self.collided_enemies_3 = pygame.sprite.spritecollide(self.Player_3, self.Ships_groups, False)
            self.control_order()
            self.data_client = self.game.send_data(self.player)
            self.all_sprites.update()
            self.draw_open_harbor()
        else:
            self.game_loop_2()

    def action(self):
        ship_health = self.a.health
        card_power = self.b.power
        card_prop = self.b.prop
        if self.sup_power == 1 and card_prop == 'r':
            card_power += 1
        ship_cover = self.a.cover

        if self.prop_white_to_red == 0:
            if ship_cover == 1:

                if self.a.prop == card_prop == 'w' or self.a.prop == card_prop == 'r':
                    if self.a.prop == 'w' and self.a.shield != 0:
                        self.collided_enemies = None
                        self.collided_enemies_2 = None
                        self.a = None
                        self.b = None
                        self.list_control.clear()
                        self.list_control_2.clear()
                    else:
                        self.a.health_change(ship_health - card_power)
                        self.move_data.append([card_prop, card_power, self.a.health, self.a.rect.topleft, self.a.cover])
                        self.h_m_t -= 1
                        self.b.change_number(-1)
                        self.number_of_cards -= 1
                        self.collided_enemies = None
                        self.collided_enemies_2 = None
                        self.a = None
                        self.b = None
                        self.list_control.clear()
                        self.list_control_2.clear()

                else:
                    if self.a.prop == 'w' and card_prop == 'r' and self.a.shield != 0:
                        self.a.health_change(card_power)
                        self.move_data.append([card_prop, card_power, self.a.health, self.a.rect.topleft, self.a.cover])
                        self.h_m_t -= 1
                        self.b.change_number(-1)
                        self.number_of_cards -= 1
                        self.collided_enemies = None
                        self.collided_enemies_2 = None
                        self.a = None
                        self.b = None
                        self.list_control.clear()
                        self.list_control_2.clear()
                    else:
                        self.collided_enemies = None
                        self.collided_enemies_2 = None
                        self.a = None
                        self.b = None
                        self.list_control.clear()
                        self.list_control_2.clear()


            else:
                if card_prop == 'w' or card_prop == 'r':
                    if ship_health > 0:
                        if self.a.prop == card_prop:
                            self.a.health_change(ship_health - card_power)
                            self.move_data.append(
                                [card_prop, card_power, self.a.health, self.a.rect.topleft, self.a.cover])
                            self.h_m_t -= 1
                            self.b.change_number(-1)
                            self.number_of_cards -= 1
                            self.collided_enemies = None
                            self.collided_enemies_2 = None
                            self.a = None
                            self.b = None
                            self.list_control.clear()
                            self.list_control_2.clear()
                        else:
                            self.a.health_change(ship_health)
                            self.move_data.append(
                                [card_prop, card_power, self.a.health, self.a.rect.topleft, self.a.cover])
                            self.h_m_t -= 1
                            self.b.change_number(-1)
                            self.number_of_cards -= 1
                            self.collided_enemies = None
                            self.collided_enemies_2 = None
                            self.a = None
                            self.b = None
                            self.list_control.clear()
                            self.list_control_2.clear()

                    else:
                        self.a.opening()
                        self.move_data.append([card_prop, card_power, 'miss', self.a.rect.topleft, self.a.cover])
                        self.h_m_t -= 1
                        self.b.change_number(-1)
                        self.number_of_cards -= 1
                        self.collided_enemies = None
                        self.collided_enemies_2 = None
                        self.a = None
                        self.b = None
                        self.list_control.clear()
                        self.list_control_2.clear()

        else:
            if ship_cover == 1:

                if self.a.prop == 'r' or (self.a.prop == 'w' and self.a.shield != 0):
                    self.a.health_change(ship_health - card_power)
                    self.move_data.append([card_prop, card_power, self.a.health, self.a.rect.topleft, self.a.cover])
                    self.h_m_t -= 1
                    self.b.change_number(-1)
                    self.number_of_cards -= 1
                    self.collided_enemies = None
                    self.collided_enemies_2 = None
                    self.a = None
                    self.b = None
                    self.list_control.clear()
                    self.list_control_2.clear()
                elif self.a.prop == 'w' and self.a.shield <= 0:

                    if card_prop == 'r':
                        self.collided_enemies = None
                        self.collided_enemies_2 = None
                        self.a = None
                        self.b = None
                        self.list_control.clear()
                        self.list_control_2.clear()
                    elif card_prop == 'w':
                        self.a.health_change(ship_health - card_power)
                        self.move_data.append([card_prop, card_power, self.a.health, self.a.rect.topleft, self.a.cover])
                        self.h_m_t -= 1
                        self.b.change_number(-1)
                        self.number_of_cards -= 1
                        self.collided_enemies = None
                        self.collided_enemies_2 = None
                        self.a = None
                        self.b = None
                        self.list_control.clear()
                        self.list_control_2.clear()

            else:
                if card_prop == 'w' or card_prop == 'r':
                    if ship_health > 0:
                        if self.a.prop == card_prop or (card_prop == 'w'):
                            self.a.health_change(ship_health - card_power)
                            self.move_data.append(
                                [card_prop, card_power, self.a.health, self.a.rect.topleft, self.a.cover])
                            self.h_m_t -= 1
                            self.b.change_number(-1)
                            self.number_of_cards -= 1
                            self.collided_enemies = None
                            self.collided_enemies_2 = None
                            self.a = None
                            self.b = None
                            self.list_control.clear()
                            self.list_control_2.clear()
                        else:
                            self.a.health_change(ship_health)
                            self.move_data.append(
                                [card_prop, card_power, self.a.health, self.a.rect.topleft, self.a.cover])
                            self.h_m_t -= 1
                            self.b.change_number(-1)
                            self.number_of_cards -= 1
                            self.collided_enemies = None
                            self.collided_enemies_2 = None
                            self.a = None
                            self.b = None
                            self.list_control.clear()
                            self.list_control_2.clear()

                    else:
                        self.a.opening()
                        self.move_data.append([card_prop, card_power, 'miss', self.a.rect.topleft, self.a.cover])
                        self.h_m_t -= 1
                        self.b.change_number(-1)
                        self.number_of_cards -= 1
                        self.collided_enemies = None
                        self.collided_enemies_2 = None
                        self.a = None
                        self.b = None
                        self.list_control.clear()
                        self.list_control_2.clear()

    def match(self):

        if self.collided_enemies_2 is not None:
            for select_2 in self.collided_enemies_2:
                if select_2.number != 0:
                    pygame.draw.rect(self.window, (15, 150, 10), select_2.rect, 5)
                    self.list_control_2.append(select_2)
                    self.b = self.list_control_2[-1]
                    if self.b.prop == 's':
                        self.shield()
                    elif self.b.prop == 'r_or_ttc':
                        self.choose_r_or_ttc()
                    elif self.b.prop == 'pt_or_cw':
                        self.choose_pt_or_cw()



        if self.collided_enemies is not None:
            for select in self.collided_enemies:
                if select.cover == 0:
                    pygame.draw.rect(self.window, (15, 150, 10), select.rect, 5)
                    if len(self.list_control) < 1:
                        self.list_control.append(select)
                        self.a = self.list_control[0]
                else:
                    if select.health > 0:
                        pygame.draw.rect(self.window, (15, 150, 10), select.rect, 5)
                        if len(self.list_control) < 1:
                            self.list_control.append(select)
                            self.a = self.list_control[0]

        if self.a is not None and self.b is not None:
            return True
        else:
            return False

    def match_2(self):

        if self.collided_enemies_3 is not None:
            for select in self.collided_enemies_3:
                if len(select.battle) != 0 and self.b.prop == 'r_or_ttc':
                    if select.seen_control == 1 and select.health > 0:
                        pygame.draw.rect(self.window, (400, 32, 0), select.rect, 5)
                        if len(self.repair_shield_control) < 1:
                            self.repair_shield_control.append(select)
                            self.c = self.repair_shield_control[0]
                elif self.b.prop == 's':
                    if select.seen_control == 1 and select.health> 0:
                        pygame.draw.rect(self.window, (400, 32, 0), select.rect, 5)
                        if len(self.repair_shield_control) < 1:
                            self.repair_shield_control.append(select)
                            self.c = self.repair_shield_control[0]

        if self.c is not None and self.b is not None:
            if self.b.prop == 's' or (self.b.prop == 'r_or_ttc' and self.up == 1):
                return True
            else:
                return False
        else:
            return False

    def match_3(self):
        if self.collided_enemies_3 is not None:
            for select in self.collided_enemies_3:
                if select.seen_control == 1 and select.start_health > select.health:
                    pygame.draw.rect(self.window, (150, 1, 0), select.rect, 5)
                    if len(self.repair_shield_control) < 1:
                        self.repair_shield_control.append(select)
                        self.c = self.repair_shield_control[0]
        if self.r_u_w == 1 and self.c is not None:
            return True
        else:
            return False

    def choose(self):
        if self.c_pt_or_cw is not None:
            if self.up == 1:
                self.play_twice()
                self.c_pt_or_cw = None
            elif self.down == 1:
                self.change_whites()
                self.c_pt_or_cw = None
        elif self.c_r_or_ttc is not None:
            if self.up == 1:
                self.repair_ships()
                self.c_r_or_ttc = None
            elif self.down == 1:
                self.t_t_c()
                self.c_r_or_ttc = None

    def choose_r_or_ttc(self):
        self.bool_r_or_ttc = True
        self.c_r_or_ttc = 1

    def pass_card(self):
        self.move_data.append(["pass", 0, 0, (100, 100), 0])
        self.h_m_t -= 1
        self.b.change_number(-1)
        self.number_of_cards -= 1
        self.collided_enemies = None
        self.collided_enemies_2 = None
        self.collided_enemies_3 = None
        self.a = None
        self.b = None
        self.c = None
        self.up = None
        self.down = None
        self.list_control.clear()
        self.list_control_2.clear()
        self.repair_shield_control.clear()

    def repair_or_shield(self):
        card_power = self.b.power
        card_prop = self.b.prop
        if self.b.prop == 'r_or_ttc' and self.up == 1:
            self.c.find_max_and_remove()
            self.move_data.append([card_prop, card_power, self.c.health, self.c.rect.topleft, self.c.cover])
            self.b.change_number(-1)
            self.number_of_cards -= 1
            self.collided_enemies = None
            self.collided_enemies_2 = None
            self.collided_enemies_3 = None
            self.a = None
            self.b = None
            self.c = None
            self.up = None
            self.down = None
            self.list_control.clear()
            self.list_control_2.clear()
            self.repair_shield_control.clear()
            self.see_game_area = True
            self.see_main_base = False
        else:
            self.c.shield_change()
            self.move_data.append([card_prop, card_power, self.c.health, self.c.rect.topleft, self.c.cover])
            self.h_m_t -= 1
            self.b.change_number(-1)
            self.number_of_cards -= 1
            self.collided_enemies = None
            self.collided_enemies_2 = None
            self.collided_enemies_3 = None
            self.a = None
            self.b = None
            self.c = None
            self.up = None
            self.down = None
            self.list_control.clear()
            self.list_control_2.clear()
            self.repair_shield_control.clear()
            self.see_game_area = True
            self.see_main_base = False

    def repair_ships(self):
        self.see_game_area = False
        self.see_main_base = True

    def shield(self):
        self.see_game_area = False
        self.see_main_base = True

    def play_twice(self):
        self.move_data.append(["pt", 0, 0, (100, 100), 0])
        self.h_m_t += 1
        self.b.change_number(-1)
        self.number_of_cards -= 1
        self.collided_enemies = None
        self.collided_enemies_2 = None
        self.collided_enemies_3 = None
        self.a = None
        self.b = None
        self.c = None
        self.up = None
        self.down = None
        self.list_control.clear()
        self.list_control_2.clear()

    def change_whites(self):
        a = self.Card2.number
        if a == 0:
            self.collided_enemies = None
            self.collided_enemies_2 = None
            self.collided_enemies_3 = None
            self.a = None
            self.b = None
            self.c = None
            self.up = None
            self.down = None
            self.list_control.clear()
            self.list_control_2.clear()
        else:
            self.card_add(a)
            self.Card2.change_number(-a)
            self.move_data.append(["cw", 0, 0, (100, 100), 0])
            self.h_m_t -= 1
            self.b.change_number(-1)
            self.number_of_cards -= 1
            self.number_of_cards += a
            self.collided_enemies = None
            self.collided_enemies_2 = None
            self.collided_enemies_3 = None
            self.a = None
            self.b = None
            self.c = None
            self.up = None
            self.down = None
            self.list_control.clear()
            self.list_control_2.clear()

    def t_t_c(self):
        self.card_add(3)
        self.move_data.append(["ttc", 0, 0, (100, 100), 0])
        self.b.change_number(-1)
        self.number_of_cards += 2
        self.collided_enemies = None
        self.collided_enemies_2 = None
        self.collided_enemies_3 = None
        self.a = None
        self.b = None
        self.c = None
        self.up = None
        self.down = None
        self.list_control.clear()
        self.list_control_2.clear()

    def choose_pt_or_cw(self):
        self.bool_pt_or_cw = True
        self.c_pt_or_cw = 1

    def card_add(self, x):
        for i in range(x):
            card = self.list_c[0]
            card.change_number(1)
            self.list_c.pop(0)

        self.all_sprites_2.update()

    def win_lost_restart(self):
        if self.lost or self.win:
            return True
        return False

    def reset(self):

        self.all_sprites = None
        self.all_sprites_2 = None
        self.S1 = Ship((150, 150), 2, "r", 1, 1)
        self.S2 = Ship((4 * 50 + self.x, 150), 3, "r", 2, 1)
        self.S3 = Ship((5 * 50 + 2 * self.x, 150), 4, "r", 3, 1)
        self.S4 = Ship((6 * 50 + 3 * self.x, 150), 5, "r", 4, 1)
        self.S5 = Ship((150, 4 * 50 + self.y), 3, "w", 5, 1)

        self.M1 = ShipMiss((4 * 50 + self.x, 4 * 50 + self.y), 0, 1, 1)
        self.M2 = ShipMiss((5 * 50 + 2 * self.x, 4 * 50 + self.y), 0, 1, 2)
        self.M3 = ShipMiss((6 * 50 + 3 * self.x, 4 * 50 + self.y), 0, 1, 3)
        self.M4 = ShipMiss((150, 5 * 50 + 2 * self.y), 0, 1, 4)
        self.M5 = ShipMiss((4 * 50 + self.x, 5 * 50 + 2 * self.y), 0, 1, 5)
        self.M6 = ShipMiss((5 * 50 + 2 * self.x, 5 * 50 + 2 * self.y), 0, 1, 6)
        self.M7 = ShipMiss((6 * 50 + 3 * self.x, 5 * 50 + 2 * self.y), 0, 1, 7)

        self.ships = [self.S1, self.S2, self.S3, self.S4, self.S5, self.M1, self.M2, self.M3, self.M4, self.M5, self.M6,
                      self.M7]
        self.list_ship_coo = [(150, 150), (390, 150), (630, 150), (870, 150),
                              (150, 320), (390, 320), (630, 320), (870, 320),
                              (150, 490), (390, 490), (630, 490), (870, 490)]
        self.S1c = Ship((150, 150), 2, "r", 1, 0)
        self.S2c = Ship((4 * 50 + self.x, 150), 3, "r", 2, 0)
        self.S3c = Ship((5 * 50 + 2 * self.x, 150), 4, "r", 3, 0)
        self.S4c = Ship((6 * 50 + 3 * self.x, 150), 5, "r", 4, 0)
        self.S5c = Ship((150, 4 * 50 + self.y), 3, "w", 5, 0)

        self.M1c = ShipMiss((4 * 50 + self.x, 4 * 50 + self.y), 0, 0, 1)
        self.M2c = ShipMiss((5 * 50 + 2 * self.x, 4 * 50 + self.y), 0, 0, 2)
        self.M3c = ShipMiss((6 * 50 + 3 * self.x, 4 * 50 + self.y), 0, 0, 3)
        self.M4c = ShipMiss((150, 5 * 50 + 2 * self.y), 0, 0, 4)
        self.M5c = ShipMiss((4 * 50 + self.x, 5 * 50 + 2 * self.y), 0, 0, 5)
        self.M6c = ShipMiss((5 * 50 + 2 * self.x, 5 * 50 + 2 * self.y), 0, 0, 6)
        self.M7c = ShipMiss((6 * 50 + 3 * self.x, 5 * 50 + 2 * self.y), 0, 0, 7)

        self.Card1 = Arm((670, 650), 2, "r", 0)
        self.Card2 = Arm((770, 650), 1, "w", 0)
        self.Card3 = Arm((370, 650), 1, "r", 0)
        self.Card4 = Arm((470, 650), 4, "r", 0)
        self.Card5 = Arm((570, 650), 0, "s", 0)
        self.Card6 = Arm((870, 650), 0, 'r_or_ttc', 0)
        self.Card7 = Arm((270, 650), 0, 'pt_or_cw', 0)

        self.total_number_cards = self.Card1.number + self.Card2.number + self.Card3.number + self.Card4.number + \
                                  self.Card5.number + self.Card6.number + self.Card7.number
        self.list_peg_cards_coordinates = [(370, 650), (470, 650), (570, 650), (670, 650), (770, 650), (870, 650)]
        self.list_peg_cards = [[2, "r"], [2, "r"], [2, "r"], [2, "r"], [2, "r"], [1, "r"], [1, "r"], [1, "r"], [1, "r"],
                               [1, "r"], [1, "w"], [1, "w"], [1, "w"], [1, "w"], [1, "w"], [1, "w"], [1, "w"], [1, "w"],
                               [1, "w"], [0, "s"], [0, "s"], [0, "c_or_pt"], [0, "c_or_pt"], [0, "ttc_or_r"],
                               [2, "ttc_or_r"]]
        self.list_peg_cards_2 = [self.Card1, self.Card1, self.Card1, self.Card1, self.Card1, self.Card2, self.Card2,
                                 self.Card2, self.Card2, self.Card2, self.Card2, self.Card2, self.Card2, self.Card2,
                                 self.Card3, self.Card3, self.Card3, self.Card3, self.Card3, self.Card4, self.Card4,
                                 self.Card5, self.Card5, self.Card6, self.Card6, self.Card7, self.Card7]

        self.all_sprites = pygame.sprite.Group()
        self.Ships_groups = pygame.sprite.Group(self.S1, self.S2, self.S3, self.S4, self.S5, self.M1, self.M2, self.M3,
                                                self.M4, self.M5, self.M6, self.M7)
        self.all_sprites.add(self.Ships_groups)
        self.Player = Player((0, 0), self.all_sprites)
        self.list_client = [self.S1c, self.S2c, self.S3c, self.S4c, self.S5c, self.M1c, self.M2c, self.M3c,
                            self.M4c, self.M5c, self.M6c, self.M7c]
        self.Ships_groups_client = pygame.sprite.Group(self.S1c, self.S2c, self.S3c, self.S4c, self.S5c, self.M1c,
                                                       self.M2c, self.M3c, self.M4c, self.M5c, self.M6c, self.M7c)
        self.card_groups = pygame.sprite.Group(self.Card1, self.Card2, self.Card3, self.Card4, self.Card5, self.Card6,
                                               self.Card7)
        self.all_sprites_2 = pygame.sprite.Group()
        self.all_sprites_2.add(self.card_groups)
        self.all_sprites_2.add(self.Ships_groups_client)
        self.Player_2 = Player((0, 0), self.all_sprites_2)
        self.Player_3 = Player((0, 0), self.all_sprites)

        self.list_c.clear()
        self.list_c = self.list_arms_cards()

        self.up = 0
        self.down = 0
        self.decide = 0

        self.see_main_base = True
        self.see_game_area = True
        self.lost = False
        self.win = False
        self.restart = False
        self.dat = 0
        self.collided_enemies_3 = None
        self.c_pt_or_cw = None
        self.c_r_or_ttc = None
        self.collided_enemies_2 = None
        self.collided_enemies = None
        self.column = None
        self.row = None
        self.teams_2 = True
        self.changee = True
        self.start_color = None
        self.prop_white_to_red = 0
        self.sup_power = 0
        self.move_data = []
        self.h_m_t = 0
        self.data_client = []
        self.data_client_ships = []

        self.r_u_w = 0
        self.repair_using_white_bool = False

        self.list_control = []
        self.list_control_2 = []
        self.repair_shield_control = []
        self.a = None
        self.b = None
        self.c = None
        self.player_choose = None
        self.start_number_of_cards = 5
        self.number_of_cards = 0
        self.list_c = self.list_arms_cards()

        self.bool_r_or_ttc = False
        self.bool_pt_or_cw = False

    def win_lost(self):
        list_ship = [int(self.S1.health), int(self.S2.health), int(self.S3.health), int(self.S4.health), int(self.S5.health)]
        list_ship_client = [int(self.S1c.health), int(self.S2c.health), int(self.S3c.health), int(self.S4c.health), int(self.S5c.health)]
        if sum(list_ship) <= 0:
            self.lost = True
            self.h_m_t = 0
            text_2 = "You lost  "
            font_1 = pygame.font.SysFont('arial', 30)

            t2 = font_1.render(text_2, 1, (255, 254, 238))

            self.window.blit(t2, (20, 20))

        if sum(list_ship_client) <= 0:
            self.win = True
            self.h_m_t = 0
            text_2 = "You Won"
            font_1 = pygame.font.SysFont('arial', 30)

            t2 = font_1.render(text_2, 1, (255, 254, 238))

            self.window.blit(t2, (20, 20))


a = Game(0)
game = BattleShip()

while True:
    if game.start_loop() is not None:
        break
pygame.quit()
