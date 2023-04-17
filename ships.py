import pygame

class Ship(pygame.sprite.Sprite):
    def __init__(self, pos, health, prop, number, cover, *groups):
        super().__init__(*groups)
        self.cover = cover
        self.prop = prop
        self.number = number
        self.health = health
        self.start_health = health
        self.seen_control = 0
        self.shield = 0
        self.color = None
        self.x = 190
        self.y = 120
        self.battle = []
        self.image = pygame.Surface((self.x, self.y))

        self.over = pygame.image.load('blackk.png')
        self.over = pygame.transform.rotate(self.over, 90)
        self.over = pygame.transform.scale(self.over, (self.x, self.y))

        self.image_close_ship_red = pygame.image.load('start_game_red.png')
        self.image_close_ship_red = pygame.transform.rotate(self.image_close_ship_red, 90)
        self.image_close_ship_red = pygame.transform.scale(self.image_close_ship_red, (self.x, self.y))

        self.image_close_ship_blue = pygame.image.load('mavi.png')
        self.image_close_ship_blue = pygame.transform.rotate(self.image_close_ship_blue, 90)
        self.image_close_ship_blue = pygame.transform.scale(self.image_close_ship_blue, (self.x, self.y))

        self.image_ship_1 = pygame.image.load('shipred2.png')
        self.image_ship_2 = pygame.image.load('shipred3.png')
        self.image_ship_3 = pygame.image.load('shipred4.png')
        self.image_ship_4 = pygame.image.load('shipred5.png')
        self.image_ship_5 = pygame.image.load('shipwhite3.png')

        self.image_ship_1_6 = pygame.image.load('shiprep/shipred26.png')
        self.image_ship_1_6 = pygame.transform.scale(self.image_ship_1_6, (self.x, self.y))
        self.image_ship_1_5 = pygame.image.load('shiprep/shipred25.png')
        self.image_ship_1_5 = pygame.transform.scale(self.image_ship_1_5, (self.x, self.y))
        self.image_ship_1_4 = pygame.image.load('shiprep/shipred24.png')
        self.image_ship_1_4 = pygame.transform.scale(self.image_ship_1_4, (self.x, self.y))
        self.image_ship_1_3 = pygame.image.load('shiprep/shipred23.png')
        self.image_ship_1_3 = pygame.transform.scale(self.image_ship_1_3, (self.x, self.y))
        self.image_ship_1_1 = pygame.image.load('shiprep/shipred21.png')
        self.image_ship_1_1 = pygame.transform.scale(self.image_ship_1_1, (self.x,self.y))

        self.image_ship_2_7 = pygame.image.load('shipchange/shipred37.png')
        self.image_ship_2_7 = pygame.transform.scale(self.image_ship_2_7, (self.x, self.y))
        self.image_ship_2_6 = pygame.image.load('shipchange/shipred36.png')
        self.image_ship_2_6 = pygame.transform.scale(self.image_ship_2_6, (self.x, self.y))
        self.image_ship_2_5 = pygame.image.load('shipchange/shipred35.png')
        self.image_ship_2_5 = pygame.transform.scale(self.image_ship_2_5, (self.x, self.y))
        self.image_ship_2_4 = pygame.image.load('shipchange/shipred34.png')
        self.image_ship_2_4 = pygame.transform.scale(self.image_ship_2_4, (self.x, self.y))
        self.image_ship_2_2 = pygame.image.load('shipchange/shipred32.png')
        self.image_ship_2_2 = pygame.transform.scale(self.image_ship_2_2, (self.x, self.y))
        self.image_ship_2_1 = pygame.image.load('shipchange/shipred31.png')
        self.image_ship_2_1 = pygame.transform.scale(self.image_ship_2_1, (self.x, self.y))

        self.image_ship_3_8 = pygame.image.load('ship+1/shipred48.png')
        self.image_ship_3_8 = pygame.transform.scale(self.image_ship_3_8, (self.x, self.y))
        self.image_ship_3_7 = pygame.image.load('ship+1/shipred47.png')
        self.image_ship_3_7 = pygame.transform.scale(self.image_ship_3_7, (self.x, self.y))
        self.image_ship_3_6 = pygame.image.load('ship+1/shipred46.png')
        self.image_ship_3_6 = pygame.transform.scale(self.image_ship_3_6, (self.x, self.y))
        self.image_ship_3_5 = pygame.image.load('ship+1/shipred45.png')
        self.image_ship_3_5 = pygame.transform.scale(self.image_ship_3_5, (self.x, self.y))
        self.image_ship_3_3 = pygame.image.load('ship+1/shipred43.png')
        self.image_ship_3_3 = pygame.transform.scale(self.image_ship_3_3, (self.x, self.y))
        self.image_ship_3_2 = pygame.image.load('ship+1/shipred42.png')
        self.image_ship_3_2 = pygame.transform.scale(self.image_ship_3_2, (self.x, self.y))
        self.image_ship_3_1 = pygame.image.load('ship+1/shipred41.png')
        self.image_ship_3_1 = pygame.transform.scale(self.image_ship_3_1, (self.x, self.y))

        self.image_ship_4_9 = pygame.image.load('ship7/shipred59.png')
        self.image_ship_4_9 = pygame.transform.scale(self.image_ship_4_9, (self.x, self.y))
        self.image_ship_4_8 = pygame.image.load('ship7/shipred58.png')
        self.image_ship_4_8 = pygame.transform.scale(self.image_ship_4_8, (self.x, self.y))
        self.image_ship_4_7 = pygame.image.load('ship7/shipred57.png')
        self.image_ship_4_7 = pygame.transform.scale(self.image_ship_4_7, (self.x, self.y))
        self.image_ship_4_6 = pygame.image.load('ship7/shipred56.png')
        self.image_ship_4_6 = pygame.transform.scale(self.image_ship_4_6, (self.x, self.y))
        self.image_ship_4_4 = pygame.image.load('ship7/shipred54.png')
        self.image_ship_4_4 = pygame.transform.scale(self.image_ship_4_4, (self.x, self.y))
        self.image_ship_4_3 = pygame.image.load('ship7/shipred53.png')
        self.image_ship_4_3 = pygame.transform.scale(self.image_ship_4_3, (self.x, self.y))
        self.image_ship_4_2 = pygame.image.load('ship7/shipred52.png')
        self.image_ship_4_2 = pygame.transform.scale(self.image_ship_4_2, (self.x, self.y))
        self.image_ship_4_1 = pygame.image.load('ship7/shipred51.png')
        self.image_ship_4_1 = pygame.transform.scale(self.image_ship_4_1, (self.x, self.y))


        self.image_ship_5_2 = pygame.image.load('shipw/shipwhite32.png')
        self.image_ship_5_2 = pygame.transform.scale(self.image_ship_5_2, (self.x, self.y))
        self.image_ship_5_1 = pygame.image.load('shipw/shipwhite31.png')
        self.image_ship_5_1 = pygame.transform.scale(self.image_ship_5_1, (self.x, self.y))

        # in case of shield for ships whites
        self.image_ship_w_shield_1_1 = pygame.image.load('shipw/shipwhite12.png')
        self.image_ship_w_shield_1_1 = pygame.transform.scale(self.image_ship_w_shield_1_1, (self.x, self.y))
        self.image_ship_w_shield_1_2 = pygame.image.load('shipw/shipwhite13.png')
        self.image_ship_w_shield_1_2 = pygame.transform.scale(self.image_ship_w_shield_1_2, (self.x, self.y))
        self.image_ship_w_shield_1_3 = pygame.image.load('shipw/shipwhite14.png')
        self.image_ship_w_shield_1_3 = pygame.transform.scale(self.image_ship_w_shield_1_3, (self.x, self.y))
        self.image_ship_w_shield_1_4 = pygame.image.load('shipw/shipwhite15.png')
        self.image_ship_w_shield_1_4 = pygame.transform.scale(self.image_ship_w_shield_1_4, (self.x, self.y))
        self.image_ship_w_shield_2_1 = pygame.image.load('shipw/shipwhite23.png')
        self.image_ship_w_shield_2_1 = pygame.transform.scale(self.image_ship_w_shield_2_1, (self.x, self.y))
        self.image_ship_w_shield_2_2 = pygame.image.load('shipw/shipwhite24.png')
        self.image_ship_w_shield_2_2 = pygame.transform.scale(self.image_ship_w_shield_2_2, (self.x, self.y))
        self.image_ship_w_shield_2_3 = pygame.image.load('shipw/shipwhite25.png')
        self.image_ship_w_shield_2_3 = pygame.transform.scale(self.image_ship_w_shield_2_3, (self.x, self.y))
        self.image_ship_w_shield_2_4 = pygame.image.load('shipw/shipwhite26.png')
        self.image_ship_w_shield_2_4 = pygame.transform.scale(self.image_ship_w_shield_2_3, (self.x, self.y))
        self.image_ship_w_shield_3_1 = pygame.image.load('shipw/shipwhite34.png')
        self.image_ship_w_shield_3_1 = pygame.transform.scale(self.image_ship_w_shield_3_1, (self.x, self.y))
        self.image_ship_w_shield_3_2 = pygame.image.load('shipw/shipwhite35.png')
        self.image_ship_w_shield_3_2 = pygame.transform.scale(self.image_ship_w_shield_3_2, (self.x, self.y))
        self.image_ship_w_shield_3_3 = pygame.image.load('shipw/shipwhite36.png')
        self.image_ship_w_shield_3_3 = pygame.transform.scale(self.image_ship_w_shield_3_3, (self.x, self.y))
        self.image_ship_w_shield_3_4 = pygame.image.load('shipw/shipwhite37.png')
        self.image_ship_w_shield_3_4 = pygame.transform.scale(self.image_ship_w_shield_3_4, (self.x, self.y))

        self.image_ship_1 = pygame.transform.scale(self.image_ship_1, (self.x, self.y))
        self.image_ship_2 = pygame.transform.scale(self.image_ship_2, (self.x, self.y))
        self.image_ship_3 = pygame.transform.scale(self.image_ship_3, (self.x, self.y))
        self.image_ship_4 = pygame.transform.scale(self.image_ship_4, (self.x, self.y))
        self.image_ship_5 = pygame.transform.scale(self.image_ship_5, (self.x, self.y))

        self.list_ships = [[self.image_ship_1_6, self.image_ship_1_5, self.image_ship_1_4, self.image_ship_1_3, self.image_ship_1, self.image_ship_1_1],
                           [self.image_ship_2_7, self.image_ship_2_6, self.image_ship_2_5, self.image_ship_2_4, self.image_ship_2, self.image_ship_2_2, self.image_ship_2_1],
                           [self.image_ship_3_8, self.image_ship_3_7, self.image_ship_3_6, self.image_ship_3_5, self.image_ship_3, self.image_ship_3_3, self.image_ship_3_2, self.image_ship_3_1],
                           [self.image_ship_4_9, self.image_ship_4_8, self.image_ship_4_7, self.image_ship_4_6, self.image_ship_4, self.image_ship_4_4, self.image_ship_4_3, self.image_ship_4_2, self.image_ship_4_1],
                           [self.image_ship_5, self.image_ship_5_2, self.image_ship_5_1]]
        self.list_ship_white = [[self.image_ship_w_shield_1_4, self.image_ship_w_shield_1_3, self.image_ship_w_shield_1_2, self.image_ship_w_shield_1_1],
                                [self.image_ship_w_shield_2_4, self.image_ship_w_shield_2_3, self.image_ship_w_shield_2_2, self.image_ship_w_shield_2_1],
                                [self.image_ship_w_shield_3_4, self.image_ship_w_shield_3_3, self.image_ship_w_shield_3_2, self.image_ship_w_shield_3_1]]
        self.show_cover()
        self.font_ship = pygame.font.SysFont('arial', 30)
        self.value_ship = self.font_ship.render("+{0}".format(self.health), 1, (0, 0, 0))
        # self.image.blit(self.value_ship, (1, 20))

        self.rect = self.image.get_rect(topleft=pos)


        self.c = 0

    def show_cover(self):
        if self.prop != 'w' or self.shield == 0:
            if self.cover == 1 or self.seen_control == 1:
                if self.health > 0:
                    a = len(self.list_ships[self.number - 1])
                    self.image.blit(self.list_ships[self.number - 1][a - self.health], (0, 0))
                else:
                    self.health = 0
                    self.image.blit(self.over, (0, 0))
            if self.cover == 0:
                self.image.blit(self.image_close_ship_blue, (0, 0))
        else:
            a = self.health
            b = self.shield
            self.image.blit(self.list_ship_white[a - 1][4-b], (0, 0))

    def health_change(self, x):
        if self.shield == 0:
            self.health = x
            self.cover = 1
            self.show_cover()
        else:
            self.shield -= x
            if self.shield < 0:
                self.shield = 0
            self.show_cover()

    def sw(self, x):
        if x == 0:
            self.image.blit(self.image_close_ship_blue, (0, 0))
        else:
            self.image.blit(self.image_close_ship_red, (0, 0))

    def which_card_was_hit_with(self, k):
        self.battle.append(k)

    def find_max_and_remove(self):
        t = max(self.battle)
        self.battle.remove(t)
        self.health_change(self.health + t)

    def seen(self):
        self.seen_control = 1

    def turn(self):
        if self.cover == 0:
            self.cover = 1
        else:
            self.cover = 0
        self.show_cover()

    def shield_change(self):
        if self.prop != 'w':
            self.health += 2
        else:
            self.shield += 2
        self.show_cover()

