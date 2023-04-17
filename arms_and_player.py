import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, *groups):
        super().__init__(*groups)
        self.image = pygame.Surface((20, 20))
        self.image.fill(pygame.Color('black'))
        self.rect = self.image.get_rect(center=pos)


class Arm(pygame.sprite.Sprite):
    def __init__(self, pos, power, prop, number, *groups):
        super().__init__(*groups)

        self.number_card = None
        self.prop = prop
        self.number = number
        self.power = power
        self.font_ship = pygame.font.SysFont('Times New Roman', 15)
        self.number_card = self.font_ship.render("{0}".format(self.number), 1, (255, 255, 255))

        self.image = pygame.Surface((80, 140))

        self.card1 = pygame.image.load('card1w.png')
        self.card1 = pygame.transform.scale(self.card1, (80, 140))
        self.card2 = pygame.image.load('card1r.png')
        self.card2 = pygame.transform.scale(self.card2, (80, 140))
        self.card3 = pygame.image.load('card2r.png')
        self.card3 = pygame.transform.scale(self.card3, (80, 140))
        self.card4 = pygame.image.load('card4r.png')
        self.card4 = pygame.transform.scale(self.card4, (80, 140))
        self.card5 = pygame.image.load('cardshield.png')
        self.card5 = pygame.transform.scale(self.card5, (80, 140))
        self.card6 = pygame.image.load('card2porCW.png')
        self.card6 = pygame.transform.scale(self.card6, (80, 140))
        self.card7 = pygame.image.load('cardrort3c.png')
        self.card7 = pygame.transform.scale(self.card7, (80, 140))

        self.card1s = pygame.image.load('card1ws.png')
        self.card1s = pygame.transform.scale(self.card1s, (80, 120))
        self.card2s = pygame.image.load('card1rs.png')
        self.card2s = pygame.transform.scale(self.card2s, (80, 120))
        self.card3s = pygame.image.load('card2rs.png')
        self.card3s = pygame.transform.scale(self.card3s, (80, 120))
        self.card4s = pygame.image.load('card4rs.png')
        self.card4s = pygame.transform.scale(self.card4s, (80, 120))
        self.card5s = pygame.image.load('cardshields.png')
        self.card5s = pygame.transform.scale(self.card5s, (80, 120))
        self.card6s = pygame.image.load('card2porCWs.png')
        self.card6s = pygame.transform.scale(self.card6s, (80, 120))
        self.card7s = pygame.image.load('cardrort3cs.png')
        self.card7s = pygame.transform.scale(self.card7s, (80, 120))

        self.data_c_p = {'cards': [self.card1, self.card2, self.card3, self.card4, self.card5, self.card6, self.card7],
                         'cardss': [self.card1s, self.card2s, self.card3s, self.card4s, self.card5s, self.card6s,
                                    self.card7s],
                         'property': ['1w', '1r', '2r', '4r', '0s', '0pt_or_cw', '0r_or_ttc']}

        self.show()
        self.rect = self.image.get_rect(topleft=pos)

    def change_number(self, k):
        self.number += k
        self.show()

    def show(self):

        t = self.data_c_p['property'].index(str(self.power) + self.prop)
        if self.number == 0:
            self.image.blit(self.data_c_p['cardss'][t], (0, 0))
            self.number_card = self.font_ship.render("{0}".format(self.number), 1, (255, 255, 255))
            self.image.blit(self.number_card, (37, 122))
        else:
            self.image.blit(self.data_c_p['cards'][t], (0, 0))
            self.number_card = self.font_ship.render("{0}".format(self.number), 1, (255, 255, 255))
            self.image.blit(self.number_card, (37, 122))