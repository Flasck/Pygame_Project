import pygame


class Button:
    def __init__(self, x, y, width, hieght, text, in_col, act_col, font, action=None):
        self.x = x
        self.y = y
        self.width = width
        self.hieght = hieght
        self.text = text
        self.in_col = in_col
        self.act_col = act_col
        self.action = action
        self.font = font

    def draw(self, screen):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if self.x < mouse[0] < self.x + self.width and self.y < mouse[1] < self.y + self.hieght:
            pygame.draw.rect(screen, self.act_col, (self.x, self.y, self.width, self.hieght))
            if click[0] == 1:
                self.action()
        else:
            pygame.draw.rect(screen, self.in_col, (self.x, self.y, self.width, self.hieght))

        font_type = pygame.font.Font(None, self.font)
        text = font_type.render(self.text, True, (0, 0, 0))
        screen.blit(text, (self.x + 15, self.y + 8))


