import pygame
import sys
import random
from time import sleep

#BLACK = (0, 0, 0)
pad_witdh = 480
pad_height = 640
rock_image = [
    'imgs/rock01.png','imgs/rock02.png','imgs/rock03.png','imgs/rock04.png','imgs/rock05.png',
    'imgs/rock06.png','imgs/rock07.png','imgs/rock08.png','imgs/rock09.png','imgs/rock10.png',
    'imgs/rock11.png','imgs/rock12.png','imgs/rock13.png','imgs/rock14.png','imgs/rock15.png',
    'imgs/rock16.png','imgs/rock17.png','imgs/rock18.png','imgs/rock19.png','imgs/rock20.png',
    'imgs/rock21.png','imgs/rock22.png','imgs/rock23.png','imgs/rock24.png','imgs/rock25.png',
    'imgs/rock26.png','imgs/rock27.png','imgs/rock28.png','imgs/rock29.png','imgs/rock30.png',
]

def draw_object(obj, x, y):
    global game_pad
    game_pad.blit(obj, (x, y)) #obj를 해당하는 좌표로부터 그려라

def init_game():
    global game_pad, clock, background, fighter, missile, explosion
    pygame.init()
    game_pad = pygame.display.set_mode((pad_witdh, pad_height))
    pygame.display.set_caption("PyShooting") #타이틀
    background = pygame.image.load('imgs/background.png')
    fighter = pygame.image.load('imgs/fighter.png')
    missile = pygame.image.load('imgs/missile.png')
    explosion = pygame.image.load('imgs/explosion.png')
    clock = pygame.time.Clock()

def run_game():
    global game_pad, clock, background, figter, missile, explosion

    fighter_size = fighter.get_rect().size
    fighter_width = fighter_size[0]
    fighter_height = fighter_size[1]

    x = pad_witdh * 0.45 #밑의 부분의 중간에
    y = pad_height * 0.9
    fighter_x = 0

    missile_xy = []

    rock = pygame.image.load(random.choice(rock_image))
    rock_size = rock.get_rect().size
    rock_width = rock_size[0]
    rock_height = rock_size[1]

    rock_x = random.randrange(0, pad_witdh - rock_width)
    rock_y = 0
    rock_speed = 2

    is_shot = False
    shot_count = 0
    rock_passed = 0

    on_game = False
    while not on_game:
        for event in pygame.event.get():
            if event.type in [pygame.QUIT]: #게임 프로그램 종료
                pygame.quit()
                sys.exit()
            if event.type in [pygame.KEYDOWN]:#keydown : 키가 눌리면
                if event.key == pygame.K_LEFT:
                    fighter_x -= 5
                elif event.key == pygame.K_RIGHT:
                    fighter_x += 5
                elif event.key == pygame.K_SPACE:
                    missile_x = x + fighter_width / 2 #비행기 앞부분의 중간에서 나가면 된다
                    missile_y = y - fighter_height    #앞으로만 나가면 된다
                    missile_xy.append([missile_x, missile_y])

            if event.type in [pygame.KEYUP]: #방향키를 떼면 전투기 멈춤
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    fighter_x = 0

        draw_object(background, 0, 0)

        #전투기 위치 재 조정
        x += fighter_x

        if x < 0: #화면 충돌처리
            x = 0
        elif x > pad_witdh - fighter_width: #화면 끝까지 오른쪽으로 갔을때
            x = pad_witdh - fighter_width

        draw_object(fighter, x, y)

        #미사일 발사 그리기
        if len(missile_xy) != 0:
            for i, bxy in enumerate(missile_xy):
                bxy[1] -= 10 #y좌표로 -10씩 빠르게 이동한다
                missile_xy[i][1] = bxy[1]

                if bxy[1] <= 0: #미사일이 화면 밖을 벗어나면
                    try:
                        missile_xy.remove(bxy) #미사일 제거
                    except:
                        pass
        if len(missile_xy) != 0:
            for bx, by in missile_xy:
                draw_object(missile, bx, by)

        rock_y += rock_speed

        if rock_y > pad_height: #운석이 지구로 떨어진경우
            #새 운석을 띄운다
            rock = pygame.image.load(random.choice(rock_image))
            rock_size = rock.get_rect().size
            rock_width = rock_size[0]
            rock_height = rock_size[1]
            rock_x = random.randrange(0, pad_witdh - rock_width)
            rock_y = 0

        draw_object(rock, rock_x, rock_y)

        pygame.display.update()
        clock.tick(60)
    pygame.quit()

init_game()
run_game()

