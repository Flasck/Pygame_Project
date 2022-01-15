import pygame


class Left_Jack(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.type = 0
        self.variation = {1: pygame.transform.scale(pygame.image.load("Jack_Images/L_j.png"), (400, 400)),
                          2: pygame.transform.scale(pygame.image.load("Jack_Images/L_j_deal.png"), (400, 400)),
                          3: pygame.transform.scale(pygame.image.load("Jack_Images/L_j_eat.png"), (400, 400))}

    def Refactor(self):
        self.image = self.variation[self.type]
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 620

    def Stand(self):
        self.type = 1

    def Throw(self):
        self.type = 2

    def Eat(self):
        self.type = 3
