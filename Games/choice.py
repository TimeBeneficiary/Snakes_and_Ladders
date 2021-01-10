#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import pygame
import sys
import pygame.freetype
import Info
import user


# return list (player_name1~4)

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

images = [image_choice1, image_choice2, image_choice3, image_choice4]

GOLD = 255, 255, 0
welcome_str_font = pygame.freetype.Font("Sofadione.ttf", 36)




def choice(mode):
    pygame.init()

    # 这是一个游戏的界面的设置

    GOLD = 255, 255, 0
    welcome_str_font = pygame.freetype.Font("Sofadione.ttf", 36)

    screen = pygame.display.set_mode((450, 600))
    clock = pygame.time.Clock()
    # 玩家姓名列表
    names = []
    id_array = []
    choice_player = [0, 1, 2, 3]
    # 如果玩家是多人模式
    if mode == 4:
        # 外循环开启标志位
        number_of_players = 0
        # 内循环开启标志位

        print(number_of_players)
        id_number = 5000
        while number_of_players < 4:
            m = 0
            b = 2
            flag = True
            name_list = []
            while flag:
                clock.tick(fps)
                screen.fill((0, 0, 0))
                correction = 0
                # 因为第三张图片太大了，所以要调整位置

                if number_of_players == 3:
                    correction = -100

                screen.blit(images[choice_player[id_number % len(choice_player)]], (100 + correction, 0 + m))

                # 显示这个玩家的名字，以及continue的标志
                welcome_str_font.render_to(screen, (100, 430), "name:" + str(" ".join(name_list)), fgcolor=GOLD,
                                           size=40)
                welcome_str_font.render_to(screen, (150, 530), "continue", fgcolor=GOLD,
                                           size=40)
                welcome_str_font.render_to(screen, (170, 470), "start", fgcolor=GOLD,
                                           size=40)
                welcome_str_font.render_to(screen, (20, 100), "LEFT", fgcolor=GOLD,
                                           size=40)
                welcome_str_font.render_to(screen, (320, 100), "RIGHT", fgcolor=GOLD,
                                           size=40)
                pygame.display.update()

                # 保持抖动的增量
                m += b
                if m > 12 or m < -24:
                    b = -b

                # 监控事件
                for event in pygame.event.get():
                    # 按键为退出，游戏系统推出
                    if event.type == pygame.QUIT:
                        sys.exit()
                    # 检测按下的按键是不是26个字母，系统只会对26个字母作出反应
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            id_number -= 1
                        if event.key == pygame.K_RIGHT:
                            id_number += 1
                        if 122 >= event.key >= 97:
                            # 将名字的一部分推入名字列表
                            name_list.append(alphabet[event.key - 97])
                    clock.tick(fps)
                    # 如果检测到鼠标按下，并且是在continue的区域，将第{}个完整的名字保存在names列表当中
                    # 如果是按下其他的区域，也会触发存储机制，并且再进行一次判断，判断按下的是其他的区域，判断成功之后
                    # 结束外层的循环，整个选人过程结束
                    if event.type == pygame.MOUSEBUTTONDOWN and (
                            570 >= pygame.mouse.get_pos()[1] >= 530) or event.type == pygame.MOUSEBUTTONDOWN and (
                            510 >= pygame.mouse.get_pos()[1] >= 470):
                        names.append("".join(name_list))
                        id_array.append(choice_player[id_number % len(choice_player)])

                        choice_player.remove(choice_player[id_number % len(choice_player)])
                        # while循环结束
                        flag = False
                        if event.type == pygame.MOUSEBUTTONDOWN and (510 >= pygame.mouse.get_pos()[1] >= 470):
                            number_of_players = 4
            id_number += 1
            number_of_players += 1

        print(names, id_array)
        return names, id_array

    elif mode == 1:
        i = 5000
        m = 0
        b = 2
        flag = True
        name_list = []
        names = ["AI"]
        while flag:

            clock.tick(fps)
            screen.fill((0, 0, 0))
            screen.blit(images[i % 3], (100, 0 + m))
            welcome_str_font.render_to(screen, (50, 430), "name:" + str(" ".join(name_list)), fgcolor=GOLD,
                                       size=40)
            welcome_str_font.render_to(screen, (150, 530), "continue", fgcolor=GOLD,
                                       size=40)
            welcome_str_font.render_to(screen, (20, 100), "LEFT", fgcolor=GOLD,
                                       size=40)
            welcome_str_font.render_to(screen, (320, 100), "RIGHT", fgcolor=GOLD,
                                       size=40)
            pygame.display.update()
            m += b
            if m > 12 or m < -24:
                b = -b
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        i -= 1
                    if event.key == pygame.K_RIGHT:
                        i += 1
                    if 122 >= event.key >= 97:
                        name_list.append(alphabet[event.key - 97])
                clock.tick(fps)

                if event.type == pygame.MOUSEBUTTONDOWN and (570 >= pygame.mouse.get_pos()[1] >= 530):
                    names.append("".join(name_list))
                    id_array.append(3)
                    id_array.append(i % 3)
                    flag = False

            pygame.display.update()

    return names,id_array



