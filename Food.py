import pygame
import random


class Food(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.cooked_lvl = 0
        self.variation = {1: "Food_Images/Meat.png",
                          2: "Food_Images/Pizza.png",
                          3: "Food_Images/Chicken.png",
                          4: "Food_Images/Sushi.png"}

        self.side_coord = {0: 300, 1: 1600}
        self.image = pygame.image.load(self.variation[random.randint(1, 4)])
        self.rect = self.image.get_rect()
        self.side = random.randint(0, 1)
        self.rect.centerx = self.side_coord[self.side]
        self.rect.bottom = 0

        self.x_move = 0
        self.y_move = 5
        self.is_thrown = False

    def Falling(self):
        self.y_move += 2

    def Thrown(self):
        self.y_move += 2.4

    def Move(self):
        self.rect.centerx += self.x_move
        self.rect.bottom += self.y_move

    def Check_Can_Eat(self, all_sprites, l_j, r_j):
        for el in all_sprites:
            if el.rect.bottom > 1000 and el.cooked_lvl >= 2:
                el.kill()
                if self.side == 0:
                    l_j.Eat()
                else:
                    r_j.Eat()
                return True

    def Check_Lose(self, all_sprites):
        for el in all_sprites:
            if el.rect.bottom > 1400:
                for e in all_sprites:
                    e.kill()
                return True