import pygame
import sys
import random
from Right_Jack import Right_Jack
from Left_Jack import Left_Jack
from Food import Food
from Button import Button
from Campfire import Campfire
import time


def swap():
    global game
    game = not game


def out():
    pygame.quit()
    sys.exit()


def new_game():
    global food_spr
    for f in food_spr:
        f.kill()
    swap()


def menu_cycle():
    global losed
    screen.blit(image, (0, 0))

    l_j.Refactor()
    r_j.Refactor()
    another_spr.draw(screen)
    food_spr.draw(screen)

    if losed:
        font_type = pygame.font.Font(None, 160)
        text = font_type.render("YOU LOSE", True, (255, 255, 255))
        screen.blit(text, (650, 400))
        pygame.display.flip()
        time.sleep(2)
        losed = False

    pygame.draw.rect(screen, (25, 25, 25), (650, 80, 620, 920))
    pygame.draw.rect(screen, (100, 100, 100), (700, 130, 520, 820))

    font_type = pygame.font.Font(None, 120)
    text = font_type.render("MENU", True, (0, 0, 0))
    screen.blit(text, (840, 200))

    font_type = pygame.font.Font(None, 45)
    text = ["You have to throw food through",
            "the rocket turbine, prepare,",
            "and eat it. You can't skip it!",
            "Gather all your attentiveness and",
            "feed the hungry Amongasics!!!"]
    y = 680

    for el in text:
        text = font_type.render(el, True, (0, 0, 0))
        screen.blit(text, (720, y))
        y += 40

    new_game.draw(screen)
    out.draw(screen)
    pygame.display.flip()


def game_cycle():
    global max_score
    screen.blit(image, (0, 0))
    l_j.Refactor()
    r_j.Refactor()
    fire.Fire()
    another_spr.draw(screen)
    food_spr.draw(screen)
    pause.draw(screen)

    font_type = pygame.font.Font(None, 80)
    sp = [(0, 150, 0), (150, 0, 0)]
    result = font_type.render(f"Current score: {score}", True, sp[score % 2])
    with open('Score.txt', 'r+') as f:
        s = f.read()
        max_score = font_type.render(f"Maximum score: {s}", True, sp[score % 2])
    screen.blit(result, (1300, 30))
    screen.blit(max_score, (1300, 100))

    pygame.display.flip()


game = False
losed = False

pygame.init()
screen = pygame.display.set_mode((0, 0))

img = pygame.image.load('Back.png')
image = pygame.transform.scale(img, (1920, 1080))

clock = pygame.time.Clock()
FPS = 100

pause = Button(20, 20, 50, 50, "||", (120, 120, 120), (255, 255, 255), 50,  swap)
new_game = Button(780, 350, 350, 70, "NEW GAME", (0, 150, 0), (200, 0, 0), 80, new_game)
out = Button(780, 500, 350, 70, "EXIT GAME", (0, 150, 0), (200, 0, 0), 80, out)

pygame.time.set_timer(pygame.USEREVENT, random.randint(2, 5) * 1000)

food_spr = pygame.sprite.Group()
another_spr = pygame.sprite.Group()

l_j = Left_Jack()
r_j = Right_Jack()
fire = Campfire()
another_spr.add(l_j)
another_spr.add(r_j)
another_spr.add(fire)

u = 4
score = 0
fire.Fire()

if __name__ == '__main__':

    while True:

        while game:
            # Основной процесс игры
            u += 1
            if u == 5:
                l_j.Stand()
                r_j.Stand()
                u = 0
            losed = False
            # Поверка нажатых клавиш
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    swap()

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    l_j.Throw()
                    for el in food_spr:
                        if el.rect.bottom > 650 and el.rect.centerx < 450 and el.side != 1:
                            el.is_thrown = True
                            el.y_move = -el.y_move
                            el.x_move = 28
                            el.cooked_lvl += 1
                            el.side = 1

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                    r_j.Throw()
                    for el in food_spr:
                        if el.rect.bottom > 650 and el.rect.centerx > 1450 and el.side != 0:
                            el.is_thrown = True
                            el.y_move = -el.y_move
                            el.x_move = -28
                            el.cooked_lvl += 1
                            el.side = 0

                if event.type == pygame.USEREVENT:
                    food_spr.add(Food())
                    pygame.time.set_timer(pygame.USEREVENT, random.randint(2, 5) * 1000)

            for el in food_spr:
                if el.is_thrown:
                    el.Thrown()
                else:
                    el.Falling()
                el.Move()
                if el.Check_Can_Eat(food_spr, l_j, r_j):
                    score += 1
                if el.Check_Lose(food_spr):
                    swap()
                    losed = True
                    with open('Score.txt', 'r+') as f:
                        if score > int(*f):
                            f.seek(0)
                            f.write(str(score))
                    score = 0

            game_cycle()
            clock.tick(FPS)

        while not game:
            l_j.Eat()
            r_j.Eat()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    swap()

            menu_cycle()
            clock.tick(FPS)
