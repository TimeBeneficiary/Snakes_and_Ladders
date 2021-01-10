#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import pygame
import random
import sys
import user
import welcome
import Info
import pygame.freetype
import time

# 加载欢迎界面
# 返回用户刚刚输入的名字存储在names列表当中
# 返回用户的id码，存储在id_array列表当中，用于保证用户选择的角色和实际操纵的角色一致
names, id_array = welcome.welcome()
pygame.quit()


# 生成游戏对象并且存储在游戏角色的列表players当中
players = []
for i in range(len(names)):
    players.append(user.Player(names[i], str(id_array[i])))

info = Info.Info()
info.game_init()
fps = 10
# 走动
a = 100
dice_result = 0

last_x = []
last_y = []
for i in range(len(names)):
    last_x.append(players[i].play_rect.centerx)
for i in range(len(names)):
    last_y.append(players[i].play_rect.centery)

# 加载骰子图片显示素材
dice_images = [info.dice_image1, info.dice_image2, info.dice_image3, info.dice_image4, info.dice_image5,
               info.dice_image6]
# 骰子模糊图片动态素材
dice_animations = [info.dice_animation1, info.dice_animation2, info.dice_animation3, info
    .dice_animation4]


def player_move(num, dice_result, last_x, last_y):
    m = 0
    b = 2
    # 现在的前进长度，加上接下来的前进的长度，没有超过一条直线的限度

    if dice_result * 95 + last_x[num] <= 1140:
        for i in range((dice_result * 95)//3):
            info.clock.tick(60)
            players[num].play_rect = players[num].play_rect.move(3, 0)
            info.screen.blit(info.map_image, (275, 0))
            info.screen.blit(players[num].play_image,
                             (players[num].play_rect.centerx, players[num].play_rect.centery + m))
            for j in range(len(names)):
                if j != num:
                    info.screen.blit(players[j].play_image,
                                     (players[j].play_rect.centerx, players[j].play_rect.centery))
            pygame.display.update()
            m += b
            if m > 0 or m < -24:
                b = -b
        players[num].play_rect = players[num].play_rect.move(last_x[num] + dice_result*95 - players[num].play_rect.centerx, 0)
        last_x[num] = players[num].play_rect.centerx
        last_y[num] = players[num].play_rect.centery
    # 如果是超过了，那么分开进行
    elif dice_result * 95 + last_x[num] > 1140 and players[num].play_rect.centery > 0:
        remainder = last_x[num] + dice_result * 95 - 1140 - 95
        for i in range((1140 - last_x[num])//3):
            info.clock.tick(60)
            players[num].play_rect = players[num].play_rect.move(3, 0)
            info.screen.blit(info.map_image, (275, 0))
            info.screen.blit(players[num].play_image,
                             (players[num].play_rect.centerx, players[num].play_rect.centery + m))
            for j in range(len(names)):
                if j != num:
                    info.screen.blit(players[j].play_image,
                                     (players[j].play_rect.centerx, players[j].play_rect.centery))
            pygame.display.update()
            m += b
            if m > 0 or m < -24:
                b = -b
        ######################################
        players[num].play_rect.centery -= 80
        players[num].play_rect.centerx = 285

        for i in range((remainder)//3):
            info.clock.tick(60)
            players[num].play_rect = players[num].play_rect.move(3, 0)
            info.screen.blit(info.map_image, (275, 0))
            info.screen.blit(players[num].play_image,
                             (players[num].play_rect.centerx, players[num].play_rect.centery + m))
            for j in range(len(names)):
                if j != num:
                    info.screen.blit(players[j].play_image,
                                     (players[j].play_rect.centerx, players[j].play_rect.centery))
            pygame.display.update()
            m += b
            if m > 0 or m < -24:
                b = -b
        last_x[num] = players[num].play_rect.centerx
        last_y[num] = players[num].play_rect.centery

    if 505 >= players[num].play_rect.centerx >= 445 and 725 >= players[num].play_rect.centery >= 705:
        # 梯子3原坐标（475，715）
        # 指向285 315
        for i in range(20):
            info.clock.tick(60)
            players[num].play_rect = players[num].play_rect.move(-9, -20)
            info.screen.blit(info.map_image, (275, 0))
            info.screen.blit(players[num].play_image, (players[num].play_rect.centerx, players[num].play_rect.centery))
            for j in range(len(names)):
                if j != num:
                    info.screen.blit(players[j].play_image,
                                     (players[j].play_rect.centerx, players[j].play_rect.centery))
            pygame.display.update()
        players[num].play_rect = players[num].play_rect.move(285-players[num].play_rect.centerx, 315-players[num].play_rect.centery)
        info.screen.blit(players[num].play_image, (players[num].play_rect.centerx, players[num].play_rect.centery))
        last_x[num] = players[num].play_rect.centerx
        last_y[num] = players[num].play_rect.centery
    if 790 >= players[num].play_rect.centerx >= 730 and 725 >= players[num].play_rect.centery >= 705:
        # 梯子6原坐标（760，715）
        # 指向855 555
        for i in range(20):
            info.clock.tick(60)
            players[num].play_rect = players[num].play_rect.move(5, -8)
            info.screen.blit(info.map_image, (275, 0))
            info.screen.blit(players[num].play_image, (players[num].play_rect.centerx, players[num].play_rect.centery))
            for j in range(len(names)):
                if j != num:
                    info.screen.blit(players[j].play_image,
                                     (players[j].play_rect.centerx, players[j].play_rect.centery))
            pygame.display.update()
        players[num].play_rect = players[num].play_rect.move(855-players[num].play_rect.centerx, 555-players[num].play_rect.centery)
        info.screen.blit(players[num].play_image, (players[num].play_rect.centerx, players[num].play_rect.centery))
        last_x[num] = players[num].play_rect.centerx
        last_y[num] = players[num].play_rect.centery

    if 1170 >= players[num].play_rect.centerx >= 1110 and 645 >= players[num].play_rect.centery >= 625:
        # 梯子20原坐标（1140，635）
        # 指向1140 235
        for i in range(20):
            info.clock.tick(60)
            players[num].play_rect = players[num].play_rect.move(0, -20)
            info.screen.blit(info.map_image, (275, 0))
            info.screen.blit(players[num].play_image, (players[num].play_rect.centerx, players[num].play_rect.centery))
            for j in range(len(names)):
                if j != num:
                    info.screen.blit(players[j].play_image,
                                     (players[j].play_rect.centerx, players[j].play_rect.centery))
            pygame.display.update()
        last_x[num] = players[num].play_rect.centerx
        last_y[num] = players[num].play_rect.centery
    if 790 >= players[num].play_rect.centerx >= 730 and 485 >= players[num].play_rect.centery >= 465:
        # 梯子36原坐标（760，475）
        # 指向665 315
        # 36
        for i in range(20):
            info.clock.tick(60)
            players[num].play_rect = players[num].play_rect.move(-5, -8)
            info.screen.blit(info.map_image, (275, 0))
            info.screen.blit(players[num].play_image, (players[num].play_rect.centerx, players[num].play_rect.centery))
            pygame.display.update()
        players[num].play_rect = players[num].play_rect.move(665-players[num].play_rect.centerx, 315-players[num].play_rect.centery)
        info.screen.blit(players[num].play_image, (players[num].play_rect.centerx, players[num].play_rect.centery))
        for j in range(len(names)):
            if j != num:
                info.screen.blit(players[j].play_image, (players[j].play_rect.centerx, players[j].play_rect.centery))
        last_x[num] = players[num].play_rect.centerx
        last_y[num] = players[num].play_rect.centery
    if 505 >= players[num].play_rect.centerx >= 445 and 245 >= players[num].play_rect.centery >= 225:
        # 梯子63原坐标（475，235）
        # 指向665 -5
        for i in range(20):
            info.clock.tick(60)
            players[num].play_rect = players[num].play_rect.move(10, -12)
            info.screen.blit(info.map_image, (275, 0))
            info.screen.blit(players[num].play_image, (players[num].play_rect.centerx, players[num].play_rect.centery))
            pygame.display.update()
        players[num].play_rect = players[num].play_rect.move(665 - players[num].play_rect.centerx,
                                                             -5 - players[num].play_rect.centery)
        info.screen.blit(players[num].play_image, (players[num].play_rect.centerx, players[num].play_rect.centery))
        for j in range(len(names)):
            if j != num:
                info.screen.blit(players[j].play_image, (players[j].play_rect.centerx, players[j].play_rect.centery))
        last_x[num] = players[num].play_rect.centerx
        last_y[num] = players[num].play_rect.centery
    if 980 >= players[num].play_rect.centerx >= 920 and 245 >= players[num].play_rect.centery >= 225:
        # 梯子68原坐标(950,235)
        # 指向950 -5
        for i in range(20):
            info.clock.tick(60)
            players[num].play_rect = players[num].play_rect.move(0, -12)
            info.screen.blit(info.map_image, (275, 0))
            info.screen.blit(players[num].play_image, (players[num].play_rect.centerx, players[num].play_rect.centery))
            for j in range(len(names)):
                if j != num:
                    info.screen.blit(players[j].play_image,
                                     (players[j].play_rect.centerx, players[j].play_rect.centery))
            pygame.display.update()
        last_x[num] = players[num].play_rect.centerx
        last_y[num] = players[num].play_rect.centery
    ##############################################################################################
    if 600 >= players[num].play_rect.centerx >= 540 and 485 >= players[num].play_rect.centery >= 465:
        # 蛇34原坐标（570，475）
        # 指向285 715
        for i in range(20):
            info.clock.tick(60)
            players[num].play_rect = players[num].play_rect.move(-14, 12)
            info.screen.blit(info.map_image, (275, 0))
            info.screen.blit(players[num].play_image,
                             (players[num].play_rect.centerx, players[num].play_rect.centery))
            for j in range(len(names)):
                if j != num:
                    info.screen.blit(players[j].play_image,
                                     (players[j].play_rect.centerx, players[j].play_rect.centery))
            pygame.display.update()
        players[num].play_rect = players[num].play_rect.move(285-players[num].play_rect.centerx, 0)
        last_x[num] = players[num].play_rect.centerx
        last_y[num] = players[num].play_rect.centery

    if 695 >= players[num].play_rect.centerx >= 635 and 565 >= players[num].play_rect.centery >= 545:
        # 蛇25原坐标（665，555）
        # 指向665 715
        for i in range(20):
            info.clock.tick(60)
            players[num].play_rect = players[num].play_rect.move(0, 8)
            info.screen.blit(info.map_image, (275, 0))
            info.screen.blit(players[num].play_image,
                             (players[num].play_rect.centerx, players[num].play_rect.centery))
            for j in range(len(names)):
                if j != num:
                    info.screen.blit(players[j].play_image,
                                     (players[j].play_rect.centerx, players[j].play_rect.centery))
            pygame.display.update()
        last_x[num] = players[num].play_rect.centerx
        last_y[num] = players[num].play_rect.centery

    if 885 >= players[num].play_rect.centerx >= 825 and 405 >= players[num].play_rect.centery >= 385:
        # 蛇47原坐标（855，395）
        # 指向1045 635
        for i in range(20):
            info.clock.tick(60)
            players[num].play_rect = players[num].play_rect.move(9, 12)
            info.screen.blit(info.map_image, (275, 0))
            info.screen.blit(players[num].play_image,
                             (players[num].play_rect.centerx, players[num].play_rect.centery))
            for j in range(len(names)):
                if j != num:
                    info.screen.blit(players[j].play_image,
                                     (players[j].play_rect.centerx, players[j].play_rect.centery))
            pygame.display.update()
        players[num].play_rect = players[num].play_rect.move(1045-players[num].play_rect.centerx, 635-players[num].play_rect.centery)
        last_x[num] = players[num].play_rect.centerx
        last_y[num] = players[num].play_rect.centery

    if 695 >= players[num].play_rect.centerx >= 635 and 245 >= players[num].play_rect.centery >= 225:
        # 蛇65原坐标（665，235）
        # 指向（380，315）
        for i in range(20):
            info.clock.tick(60)
            players[num].play_rect = players[num].play_rect.move(-14, 4)
            info.screen.blit(info.map_image, (275, 0))
            info.screen.blit(players[num].play_image,
                             (players[num].play_rect.centerx, players[num].play_rect.centery))
            for j in range(len(names)):
                if j != num:
                    info.screen.blit(players[j].play_image,
                                     (players[j].play_rect.centerx, players[j].play_rect.centery))


            pygame.display.update()
        players[num].play_rect = players[num].play_rect.move(380-players[num].play_rect.centerx, 315-players[num].play_rect.centery)
        last_x[num] = players[num].play_rect.centerx
        last_y[num] = players[num].play_rect.centery

    if 315 >= players[num].play_rect.centerx >= 255 and 5 >= players[num].play_rect.centery >= -15:

        # 指向665 715
        for i in range(20):
            info.clock.tick(60)
            players[num].play_rect = players[num].play_rect.move(0, 12)
            info.screen.blit(info.map_image, (275, 0))
            info.screen.blit(players[num].play_image,
                             (players[num].play_rect.centerx, players[num].play_rect.centery))
            for j in range(len(names)):
                if j != num:
                    info.screen.blit(players[j].play_image,
                                     (players[j].play_rect.centerx, players[j].play_rect.centery))
            pygame.display.update()
        last_x[num] = players[num].play_rect.centerx
        last_y[num] = players[num].play_rect.centery

    if 885 >= players[num].play_rect.centerx >= 825 and 85 >= players[num].play_rect.centery >= 65:
        # 指向665 715
        for i in range(20):
            info.clock.tick(60)
            players[num].play_rect = players[num].play_rect.move(0, 12)
            info.screen.blit(info.map_image, (275, 0))
            info.screen.blit(players[num].play_image,
                             (players[num].play_rect.centerx, players[num].play_rect.centery))
            for j in range(len(names)):
                if j != num:
                    info.screen.blit(players[j].play_image,
                                     (players[j].play_rect.centerx, players[j].play_rect.centery))
            pygame.display.update()
        last_x[num] = players[num].play_rect.centerx
        last_y[num] = players[num].play_rect.centery
    ####################################################################################################################################
    if 1075 >= players[num].play_rect.centerx >= 1015 and 5 >= players[num].play_rect.centery >= -15:
        # 指向665 715
        for i in range(20):
            info.clock.tick(60)
            players[num].play_rect = players[num].play_rect.move(0, 12)
            info.screen.blit(info.map_image, (275, 0))
            info.screen.blit(players[num].play_image,
                             (players[num].play_rect.centerx, players[num].play_rect.centery))
            for j in range(len(names)):
                if j != num:
                    info.screen.blit(players[j].play_image,
                                     (players[j].play_rect.centerx, players[j].play_rect.centery))
            pygame.display.update()
        last_x[num] = players[num].play_rect.centerx
        last_y[num] = players[num].play_rect.centery

    return last_x, last_y




for i in range(len(names)):
    players[i].score = 0


def show_score():
    x = 0
    for i in range(len(names)):
        welcome_str_font.render_to(info.screen, (1300, 50 + x), str(players[i].name) + ":" + str(int(players[i].score)),
                                   fgcolor=GOLD,
                                   size=40)
        x += 100


welcome_str_font = pygame.freetype.Font("Sofadione.ttf", 36)
GOLD = 255, 255, 0


def main(n, last_x, last_y, dice_result=1):
    global id_array
    global names
    global players
    global info
    x = 0
    y = 3
    k = 0

    while True:
        k += 1
        info.screen.fill((0, 0, 0))
        info.screen.blit(dice_images[dice_result - 1], (50, 670))
        info.screen.blit(info.map_image, (275, 0))
        for i in range(len(names)):

            info.screen.blit(players[i].play_image, (players[i].play_rect.centerx, players[i].play_rect.centery))
        h = 0

        for i in range(len(names)):
            info.screen.blit(players[i].play_image, (50, 50 + y + h))
            h += 100
        info.screen.blit(dice_animations[0], (50, 670))

        x += y
        if x > 10 or x < -240:
            y = -y
        num = n % len(names)
        # 显示分数
        show_score()
        info.screen.blit(dice_animations[(k // 20) % 4], (50, 670))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if "AI" not in players[num].name:
                if event.type == pygame.MOUSEBUTTONDOWN:

                    dice_result = random.randint(1, 6)
                    info.screen.blit(dice_images[dice_result - 1], (50, 670))

                    last_x, last_y = player_move(num, dice_result, last_x, last_y)
                    players[num].score = round(((players[num].play_rect.centerx - 285) / 95),0) + round(((
                            715 - players[num].play_rect.centery) / 8 + 1),0)
                    info.screen.fill((0, 0, 0))
                    info.screen.blit(dice_animations[2], (50, 670))
                    h = 0
                    for i in range(len(names)):
                        info.screen.blit(players[i].play_image, (50, 50 + y + h))
                        h += 100
                    show_score()
                    n += 1
                    if last_x[num] == 1140 and last_y[num] == -5:
                        print("恭喜你{}，获得胜利".format(num))
                if 1165 >= last_x[num] >= 1115 and 0 >= last_y[num] >= -10:
                    pygame.quit()
                    info.game_init()
                    while True:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                sys.exit()
                        if event.type == pygame.MOUSEBUTTONDOWN and 400 >= pygame.mouse.get_pos()[0] >= 200:

                            last_x = []
                            last_y = []
                            n = 0
                            players = []
                            names, id_array = welcome.welcome()

                            for i in range(len(names)):
                                players.append(user.Player(names[i], str(id_array[i])))
                            for i in range(len(names)):
                                last_x.append(players[i].play_rect.centerx)
                            for i in range(len(names)):
                                last_y.append(players[i].play_rect.centery)

                            info = Info.Info()
                            info.game_init()
                            main(n,last_x,last_y)
                        if event.type == pygame.MOUSEBUTTONDOWN and 1000 >= pygame.mouse.get_pos()[0] >= 900:
                            flag_start = False
                            return flag_start


                        vector = user.Player(players[num].name, str(id_array[num]))
                        vector.play_image = pygame.transform.scale(vector.play_image, (300, 300))
                        info.screen.blit(vector.play_image, (100, 100))
                        welcome_str_font.render_to(info.screen, (200, 400), "YOU WIN :  " + str(players[num].name),
                                                   fgcolor=GOLD,
                                                   size=120)
                        welcome_str_font.render_to(info.screen, (200, 500), "continue : ",
                                                   fgcolor=GOLD,
                                                   size=60)
                        welcome_str_font.render_to(info.screen, (900, 500), "exit: ",
                                                   fgcolor=GOLD,
                                                   size=60)
                        pygame.display.update()
            num = n % len(names)
            if "AI" in players[num].name:
                dice_result = random.randint(1, 6)
                info.screen.blit(dice_images[dice_result - 1], (50, 670))

                last_x, last_y = player_move(num, dice_result, last_x, last_y)
                players[num].score = round(((players[num].play_rect.centerx - 285) / 95),0) + round(((
                        715 - players[num].play_rect.centery) / 8 + 1),0)
                info.screen.fill((0, 0, 0))
                info.screen.blit(dice_animations[3], (50, 670))
                h = 0
                for i in range(len(names)):
                    info.screen.blit(players[i].play_image, (50, 50 + y + h))
                    h += 100
                show_score()
                n += 1

                if 1165 >= last_x[num] >= 1115 and 0 >= last_y[num] >= -10:
                    pygame.quit()
                    info.game_init()
                    while True:
                        print(pygame.mouse.get_pos())
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                sys.exit()
                            if event.type == pygame.MOUSEBUTTONDOWN and 550 >= pygame.mouse.get_pos()[0] >= 50:
                                pygame.quit()
                                last_x = []
                                last_y = []
                                n = 0
                                players = []
                                names, id_array = welcome.welcome()

                                for i in range(len(names)):
                                    players.append(user.Player(names[i], str(id_array[i])))

                                for i in range(len(names)):
                                    last_x.append(players[i].play_rect.centerx)
                                for i in range(len(names)):
                                    last_y.append(players[i].play_rect.centery)

                                info = Info.Info()
                                info.game_init()
                                main(n, last_x, last_y)
                            if event.type == pygame.MOUSEBUTTONDOWN and 1000 >= pygame.mouse.get_pos()[0] >= 600:
                                flag_start = False
                                return flag_start



                        vector = user.Player(players[num].name,str(id_array[num]))
                        vector.play_image = pygame.transform.scale(vector.play_image,(300,300))
                        info.screen.blit(vector.play_image,(100,100))
                        welcome_str_font.render_to(info.screen, (200, 400), "YOU WIN : " + str(players[num].name), fgcolor=GOLD,
                                           size=120)
                        welcome_str_font.render_to(info.screen, (200, 500), "continue : " ,
                                                   fgcolor=GOLD,
                                                   size=60)
                        welcome_str_font.render_to(info.screen, (900, 500), "exit: " ,
                                                   fgcolor=GOLD,
                                                   size=60)

                        pygame.display.update()
                pygame.display.update()
        pygame.display.update()









n = 0
if __name__ == '__main__':
    flag_start = True
    while flag_start:
        flag_start = main(n, last_x, last_y)

