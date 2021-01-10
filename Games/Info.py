#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import pygame
import user


class Info:
    def __init__(self):
        # 4表示的是多人
        # 1表示的单人
        # 0表示的是退出
        self.mode = "a"  # 单人  多人

        # 骰子的显示数字
        self.dice_image1 = pygame.image.load("dice_1.png")
        self.dice_image1 = pygame.transform.scale(self.dice_image1, (100, 100))
        self.dice_image2 = pygame.image.load("dice_2.png")
        self.dice_image2 = pygame.transform.scale(self.dice_image2, (100, 100))
        self.dice_image3 = pygame.image.load("dice_3.png")
        self.dice_image3 = pygame.transform.scale(self.dice_image3, (100, 100))
        self.dice_image4 = pygame.image.load("dice_4.png")
        self.dice_image4 = pygame.transform.scale(self.dice_image4, (100, 100))
        self.dice_image5 = pygame.image.load("dice_5.png")
        self.dice_image5 = pygame.transform.scale(self.dice_image5, (100, 100))
        self.dice_image6 = pygame.image.load("dice_6.png")
        self.dice_image6 = pygame.transform.scale(self.dice_image6, (100, 100))

        # 骰子的模糊图片
        self.dice_animation1 = pygame.image.load("dice_Action_0.png")
        self.dice_animation2 = pygame.image.load("dice_Action_1.png")
        self.dice_animation3 = pygame.image.load("dice_Action_2.png")
        self.dice_animation4 = pygame.image.load("dice_Action_3.png")

        # 设置欢迎界面的三段字的字体大小
        self.welcome_str_rect1_size = 40
        self.welcome_str_rect2_size = 40
        self.welcome_str_rect3_size = 40





    # 游戏进行时的窗口设置
    def game_init(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1500, 800))
        self.map_image = pygame.image.load("map.png")
        self.map_image = pygame.transform.scale(self.map_image, (950, 800))
        self.clock = pygame.time.Clock()

    def welcome_init(self):
        self.screen = pygame.display.set_mode((450, 600))
        self.welcome_image = pygame.image.load("welcome.jpg")
        self.welcome_image = pygame.transform.scale(self.welcome_image, (450, 400))
        self.clock = pygame.time.Clock()








