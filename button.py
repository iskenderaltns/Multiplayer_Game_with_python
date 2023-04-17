import pygame

class Button:
    def __init__(self, size, number, cover):

        self.button = None
        self.size = size
        self.number = number
        self.cover = cover

        self.r_plus_1 = pygame.image.load('button/4k.png')  # 1
        self.r_plus_1 = pygame.transform.scale(self.r_plus_1, self.size)
        self.w_to_r = pygame.image.load('button/3k.png')  # 2
        self.w_to_r = pygame.transform.scale(self.w_to_r, self.size)
        self.repair = pygame.image.load('button/2k.png')  # 3
        self.repair = pygame.transform.scale(self.repair, self.size)
        self.collect_seven = pygame.image.load('button/5k.png')  # 4
        self.collect_seven = pygame.transform.scale(self.collect_seven, self.size)
        self.w = pygame.image.load('button/3b.png')  # 5
        self.w = pygame.transform.scale(self.w, self.size)

        self.r_plus_1c = pygame.image.load('button/4kc.png')  # 1c
        self.r_plus_1c = pygame.transform.scale(self.r_plus_1c, self.size)
        self.w_to_rc = pygame.image.load('button/3kc.png')  # 2c
        self.w_to_rc = pygame.transform.scale(self.w_to_rc, self.size)
        self.repair_c = pygame.image.load('button/2kc.png')  # 3c
        self.repair_c = pygame.transform.scale(self.repair_c, self.size)
        self.collect_seven_c = pygame.image.load('button/5kc.png')  # 4c
        self.collect_seven_c = pygame.transform.scale(self.collect_seven_c, self.size)
        self.wc = pygame.image.load('button/3bc.png')  # 5c
        self.wc = pygame.transform.scale(self.wc, self.size)

        self.harbor = pygame.image.load('button/harbor.png')  # 6
        self.harbor = pygame.transform.scale(self.harbor, size)

        self.settings = pygame.image.load('setting.jpg')  # 7
        self.settings = pygame.transform.scale(self.settings, self.size)

        self.repair_button_img = pygame.image.load('repairship.png')
        self.repair_button_img = pygame.transform.scale(self.repair_button_img, self.size)

        self.logo_img = pygame.image.load('logo.png')
        self.logo_img = pygame.transform.scale(self.logo_img, self.size)

        self.list_button = [self.repair, self.w_to_r, self.r_plus_1, self.collect_seven, self.w, self.harbor, self.settings, self.repair_button_img, self.logo_img]
        self.list_button_c = [self.repair_c, self.w_to_rc, self.r_plus_1c, self.collect_seven_c, self.wc, self.harbor, self.settings, self.repair_button_img, self.logo_img]

    def call_button(self):
        self.button = self.list_button_c[self.number - 1]
        return self.button

    def call_button_2(self):
        self.button = self.list_button[self.number - 1]
        return self.button
