from pygame.locals import *
import pygame
import sys

pygame.init()
display = pygame.display.set_mode((400,400))
pygame.display.set_caption("ゲーム")

#画像読み込み
maru_skin = pygame.image.load("ゲーム/maru.png")
batu_skin = pygame.image.load("ゲーム/batu.png")
local_skin = pygame.image.load("ゲーム/local.png")
cp_skin = pygame.image.load("ゲーム/cp.png")
retry_skin = pygame.image.load("ゲーム/retry.png")
space_skin = pygame.image.load("ゲーム/space.png")
maru_win_skin = pygame.image.load("ゲーム/maru_win.png")
batu_win_skin = pygame.image.load("ゲーム/batu_win.png")


#リサイズ
long_size = (300, 141)
local_skin = pygame.transform.scale(local_skin, (long_size))
cp_skin = pygame.transform.scale(cp_skin, (long_size))
retry_skin = pygame.transform.scale(retry_skin, (long_size))
maru_win_skin = pygame.transform.scale(maru_win_skin, (long_size))
batu_win_skin = pygame.transform.scale(batu_win_skin, (long_size))

short_size = (100, 100)
maru_skin = pygame.transform.scale(maru_skin, (short_size))
batu_skin = pygame.transform.scale(batu_skin, (short_size))
space_skin = pygame.transform.scale(space_skin, (short_size))

marubatu_pos_list = []
marubatu_list = []
num = 0

def win_check(attack, pos):
    global marubatu_pos_list
    if [attack, pos] in marubatu_pos_list:
        return 1
    
#def win_check_pos(attack, pos):
#    global marubatu_pos_list
    #if pos == 21 or pos == 22 or pos == 23:
        

    

#勝ちの判定
def win(attack, pos):
    global marubatu_pos_list
#    if win_check_pos(attack, pos) == 1:
#        print('win')
    




#○×のリスト
def marubatu_list_check(attack_marubatu):
    global marubatu_list
    global num
    if attack_marubatu in marubatu_list:
        return 0
    if num > 6:
        game_pos(2, marubatu_list[0])
        del marubatu_list[0]
    if not attack_marubatu in marubatu_list:
        marubatu_list.append(attack_marubatu)
        return 1

def i_1():
    global num
    num = num - 1


def game_click_pos(maru_batu_click):#クリック判定
    global marubatu_pos_list
    maru_batu_click = maru_batu_click % 2
    a = True
    while a:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if x < 133 and y < 133:#11
                    if marubatu_list_check(11) == 1:
                        game_pos(maru_batu_click, 11)
                    else:
                        i_1()
                elif x > 133 and x < 266 and y < 133:#12
                    if marubatu_list_check(12) == 1:
                        game_pos(maru_batu_click, 12)
                    else:
                        i_1()
                elif x > 266 and y < 133:#13
                    if marubatu_list_check(13) == 1:
                        game_pos(maru_batu_click, 13)
                    else:
                        i_1()
                if x < 133 and y > 133 and y < 266:#21
                    if marubatu_list_check(21) == 1:
                        game_pos(maru_batu_click, 21)
                    else:
                        i_1()
                elif x > 133 and x < 266 and y > 133 and y < 266:#22
                    if marubatu_list_check(22) == 1:
                        game_pos(maru_batu_click, 22)
                    else:
                        i_1()
                elif x > 266 and y > 133 and y < 266:#23
                    if marubatu_list_check(23) == 1:
                        game_pos(maru_batu_click, 23)
                    else:
                        i_1()
                if x < 133 and y > 266:#31
                    if marubatu_list_check(31) == 1:
                        game_pos(maru_batu_click, 31)
                    else:
                        i_1()
                elif x > 133 and x < 266 and y > 266:#32
                    if marubatu_list_check(32) == 1:
                        game_pos(maru_batu_click, 32)
                    else:
                        i_1()
                elif x > 266 and y > 266:#33
                    if marubatu_list_check(33) == 1:
                        game_pos(maru_batu_click, 33)
                    else:
                        i_1()
                a = False

#座標
# 11 12 13
# 21 22 23
# 31 32 33
def game_pos(maru_batu, pos):
    global display
    global maru_skin
    global batu_skin
    global space_skin
    global marubatu_pos_list
    maru_batu = int(maru_batu)
    pos = int(pos)
    if maru_batu == 1:
        attack_mode = maru_skin
    if maru_batu == 0:
        attack_mode = batu_skin
    if maru_batu == 2:
        attack_mode = space_skin
    #座標を決定
    if pos == 11:
        display.blit(attack_mode, (25, 25))
    if pos == 12:
        display.blit(attack_mode, (150, 25))
    if pos == 13:
        display.blit(attack_mode, (275, 25))
    
    if pos == 21:
        display.blit(attack_mode, (25, 150))
    if pos == 22:
        display.blit(attack_mode, (150, 150))
    if pos == 23:
        display.blit(attack_mode, (275, 150))

    if pos == 31:
        display.blit(attack_mode, (25, 275))
    if pos == 32:
        display.blit(attack_mode, (150, 275))
    if pos == 33:
        display.blit(attack_mode, (275, 275))
    pygame.display.update()
    marubatu_pos_list.append([attack_mode, pos])
    #if win(attack_mode, pos) == 0:



def start():
    global local_skin
    global cp_skin
    global display
    display.fill((255,255,255))
    pygame.display.update()
    display.blit(local_skin, (50, 29.5))
    display.blit(cp_skin, (50, 229.5))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == quit:
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if y < 200:
                    local()

def local():
    global num
    display.fill((255,255,255))
    pygame.display.update()
    while True:
        print(num)
        num = num + 1
        game_click_pos(num)

    

def cp():
    print()

start()