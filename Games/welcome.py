#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import pygame

import pygame.freetype
import choice
import Info
import sys
import time





def welcome():
    pygame.init()

    # 这是一个游戏的界面的设置


    GOLD = 255, 255, 0
    welcome_str_font = pygame.freetype.Font("Sofadione.ttf", 36)


    welcome_info = Info.Info()
    welcome_info.welcome_init()

    while True:
        welcome_info.screen.fill((0,0,0))
        welcome_info.screen.blit(welcome_info.welcome_image, (0, 0))
        welcome_str_font.render_to(welcome_info.screen, (80, 430), "Player Vs Player", fgcolor=GOLD, size=welcome_info.welcome_str_rect1_size)
        welcome_str_font.render_to(welcome_info.screen, (50, 480), "Player Vs Computer", fgcolor=GOLD, size=welcome_info.welcome_str_rect2_size)
        welcome_str_font.render_to(welcome_info.screen, (180, 530), "QUIT", fgcolor=GOLD, size=welcome_info.welcome_str_rect3_size)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and (467 >= pygame.mouse.get_pos()[1] >= 427):
                welcome_info.welcome_str_rect1_size = 30
            elif event.type == pygame.MOUSEBUTTONUP and (467 >= pygame.mouse.get_pos()[1] >= 427):
                welcome_info.welcome_str_rect1_size = 40
                welcome_info.mode = 4
                names = choice.choice(welcome_info.mode)
                return names



            elif event.type == pygame.MOUSEBUTTONDOWN and (516 >= pygame.mouse.get_pos()[1] >= 486):
                welcome_info.welcome_str_rect2_size = 30
            elif event.type == pygame.MOUSEBUTTONUP and (516 >= pygame.mouse.get_pos()[1] >= 486):
                welcome_info.welcome_str_rect2_size = 40
                welcome_info.mode = 1
                names = choice.choice(welcome_info.mode)
                return names
            elif event.type == pygame.MOUSEBUTTONDOWN and (562 >= pygame.mouse.get_pos()[1] >= 522):
                welcome_info.welcome_str_rect3_size = 30
            elif event.type == pygame.MOUSEBUTTONUP and (562 >= pygame.mouse.get_pos()[1] >= 522):
                welcome_info.welcome_str_rect3_size = 40
                sys.exit()
        pygame.display.update()

