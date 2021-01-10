#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import pygame



class Player:
    def __init__(self,name,pick):
        self.name = name
        self.play_image = pygame.image.load("{}.png".format(pick))
        self.play_image = pygame.transform.scale(self.play_image, (90, 90))
        self.play_rect = self.play_image.get_rect()
        # 起始位置设置成240，670
        # 单个方块之间的距离是95
        # 第一个方块的中心的是285 715
        self.play_rect = self.play_rect.move(240-95, 670)
        self.x = self.play_rect.centerx
        self.y = self.play_rect.centery
        self.score = 0
        self.belong = "a"





