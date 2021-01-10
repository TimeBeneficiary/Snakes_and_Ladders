#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import pygame
import sys
import pygame.freetype


pygame.init()
screen = pygame.display.set_mode((450, 600))
clock = pygame.time.Clock()
fps = 60

image_choice1 = pygame.image.load("0.png")
image_choice2 = pygame.image.load("1.png")
image_choice3 = pygame.image.load("2.png")
image_choice4 = pygame.image.load("3.png")

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z"]

names = []
images = [image_choice1, image_choice2, image_choice3, image_choice4]
flag = True
GOLD = 255,255,0
welcome_str_font = pygame.freetype.Font("Sofadione.ttf", 36)
for i in range(4):
    m = 0
    b = 2
    flag = True
    name_list = []
    while flag:

        clock.tick(fps)
        screen.fill((0, 0, 0))
        correction = 0
        if i == 3:
            correction = -100
        screen.blit(images[i], (100+correction, 0 + m))
        welcome_str_rect1 = welcome_str_font.render_to(screen, (100, 430), str(" ".join(name_list)), fgcolor=GOLD,
                                                       size=40)
        welcome_str_rect2 = welcome_str_font.render_to(screen, (150, 530), "continue", fgcolor=GOLD,
                                                       size=40)
        pygame.display.update()
        m += b
        if m > 12 or m < -24:
            b = -b
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:

                if 122 >= event.key >= 97:
                    name_list.append(alphabet[event.key - 97])
            clock.tick(fps)
            print(pygame.mouse.get_pos())
            if event.type == pygame.MOUSEBUTTONDOWN:
                names.append("".join(name_list))
                flag = False

        pygame.display.update()
print(names)
