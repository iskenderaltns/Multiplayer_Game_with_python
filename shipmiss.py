import pygame


class ShipMiss(pygame.sprite.Sprite):
    def __init__(self, pos, health, cover, number, *groups):
        super().__init__(*groups)
        self.number = number
        self.cover = cover
        self.color = None
        self.prop = 'miss'
        self.x = 190
        self.y = 120
        self.control = False
        self.battle = []
        self.health = health
        self.shield = 0
        self.seen_control = 0
        self.image = pygame.Surface((self.x, self.y))

        self.image_close_ship_red = pygame.image.load('start_game_red.png')
        self.image_close_ship_red = pygame.transform.rotate(self.image_close_ship_red, 90)
        self.image_close_ship_red = pygame.transform.scale(self.image_close_ship_red, (self.x, self.y))

        self.image_close_ship_blue = pygame.image.load('mavi.png')
        self.image_close_ship_blue = pygame.transform.rotate(self.image_close_ship_blue, 90)
        self.image_close_ship_blue = pygame.transform.scale(self.image_close_ship_blue, (self.x, self.y))

        self.image_ship_miss = pygame.image.load('missss.png')
        self.image_ship_miss = pygame.transform.scale(self.image_ship_miss, (self.x, self.y))
        self.show_cover()
        self.rect = self.image.get_rect(topleft=pos)

    def show_cover(self):
        if self.cover == 1 or self.seen_control == 1:
            self.image.blit(self.image_ship_miss, (0, 0))
        if self.cover == 0:
            self.image.blit(self.image_close_ship_blue, (0, 0))

    def opening(self):
        self.cover = 1
        self.show_cover()

    def sw(self, x):
        if x == 0:
            self.image.blit(self.image_close_ship_blue, (0, 0))
        else:
            self.image.blit(self.image_close_ship_red, (0, 0))

    def seen(self):
        self.seen_control = 1

    def turn(self):
        if self.cover == 0:
            self.cover = 1
        else:
            self.cover = 0
        self.show_cover()

    def which_card_was_hit_with(self, k):
        self.battle.append(k)
