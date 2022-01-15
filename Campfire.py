import pygame


class Campfire(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.type = 6
        self.variation = {7: pygame.transform.scale(pygame.image.load("Campfire_Images/fire_1.png"), (900, 900)),
                          14: pygame.transform.scale(pygame.image.load("Campfire_Images/fire_2.png"), (900, 900)),
                          21: pygame.transform.scale(pygame.image.load("Campfire_Images/fire_3.png"), (900, 900))}

    def Fire(self):
        self.type += 1
        if self.type > 21:
            self.type = 1
        if self.type % 7 == 0:
            self.image = self.variation[self.type]
            self.rect = self.image.get_rect()
            self.rect.centerx = 910
            self.rect.bottom = 1080
