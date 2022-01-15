import pygame


class Right_Jack(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.type = 0
        self.variation = {1: pygame.transform.scale(pygame.transform.flip(pygame.image.load("Jack_Images/R_j.png"),
                                                                          True, False), (400, 400)),
                          2: pygame.transform.scale(pygame.transform.flip(pygame.image.load("Jack_Images/R_j_deal.png"),
                                                                          True, False), (400, 400)),
                          3: pygame.transform.scale(pygame.transform.flip(pygame.image.load("Jack_Images/R_j_eat.png"),
                                                                          True, False), (400, 400))}

    def Refactor(self):
        self.image = self.variation[self.type]
        self.rect = self.image.get_rect()
        self.rect.x = 1400
        self.rect.y = 620

    def Stand(self):
        self.type = 1

    def Throw(self):
        self.type = 2

    def Eat(self):
        self.type = 3
