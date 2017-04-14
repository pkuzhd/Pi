import pygame
import pyaudio
import struct
from pygame.locals import *
from DXK import *
import random

map_list = ((1, 1, 1, 1, 0), (1, 0, 1, 0, 1), (1, 0, 0, 1, 1), (1, 0, 0, 0, 1))


def main():
    pygame.init()
    screen_size = (800, 600)
    screen = pygame.display.set_mode(screen_size)
    #初始化界面
    pa = pyaudio.PyAudio()
    SAMPLING_RATE = int(pa.get_device_info_by_index(0)['defaultSampleRate'])
    NUM_SAMPLES = 1000
    stream = pa.open(format=pyaudio.paInt16, channels=1, rate=SAMPLING_RATE, input=True, frames_per_buffer=NUM_SAMPLES)
    #初始化声音输入

    while True:
        #游戏总循环
        dxk = DXK("dxk1.png")
        block = Block("black.png", 0)
        map_queue_1 = list()
        map_queue_2 = list()
        for i in range(9):
            map_queue_1.append(1)

        for i in map_list[2]:
            map_queue_2.append(i)
        #地图初始化

        h = screen_size[1]-dxk.height-100
        reset = False
        Fullscreen = False
        clock = pygame.time.Clock()

        block_s = 0.
        fall = False
        while True:
            #当前游戏循环

            for event in pygame.event.get():
                #事件处理
                if event.type == QUIT:
                    exit()
                if event.type == KEYDOWN:
                    if event.key == 285 and event.mod == 256:
                        exit()
                    if event.key == K_r:
                        reset = True
                    if event.key == K_UP:
                        dxk.jump(2.5)
                    if event.key == K_SPACE:
                        dxk.move()
                    if event.key == K_f:
                        Fullscreen = not Fullscreen
                        if Fullscreen:
                            screen = pygame.display.set_mode(screen_size, FULLSCREEN | HWSURFACE, 32)
                        else:
                            screen = pygame.display.set_mode(screen_size, 0, 32)
                if event.type == KEYUP:
                    if event.key == K_SPACE:
                        dxk.stop()
            if reset:
                break
            if Fullscreen:
                screen.fill((255, 255, 255))
            else:
                screen.fill((255, 255, 255))

            # string_audio_data = stream.read(NUM_SAMPLES)
            # k = max(struct.unpack('1000h', string_audio_data))
            # print(k)
            


            # if k <= 2000:
            #     dxk.stop()
            # else:
            #     dxk.move()
            #     if not fall and k > 8000:
            #         dxk.jump(2.5)
            #         if k > 20000:
            #             dxk.fly()
            time_passed = clock.tick()
            time_passed_seconds = time_passed / 1000.0
            t = time_passed_seconds * 100
            if fall:
                if map_queue_1[5]==1 and block_s < -78:
                    dxk.stop()
                dxk.speed_y = -2.5
                if h < 600-53:
                    h -= dxk.speed_y * t
                else:
                    dxk.stop()

            
            
            if not dxk.can_jump and not fall:
                h -= dxk.speed_y * t
                dxk.speed_y -= dxk.g * t
                if h >= screen_size[1]-dxk.height-100 - 0.000001:
                        dxk.land()
                        dxk.can_jump = True
                        h = screen_size[1]-dxk.height-100
            if h >= screen_size[1]-dxk.height-100 - 0.000001:
                
                if map_queue_1[4]==0: 
                    if block_s < -22 and block_s > -78:
                        fall = True
                    elif map_queue_1[5]==0 and block_s <=-78:
                        fall = True
                    elif map_queue_1[3]==0 and block_s > -22:
                        fall = True
            screen.blit(dxk.image, (screen_size[0]/2-dxk.width/2, h))

            block_s += dxk.speed_x * t / 2
            if block_s <= -100.:
                map_queue_1.pop(0)
                map_queue_1.append(map_queue_2.pop(0))
                block_s += 100.
            for i in range(9):
                if map_queue_1[i]!=0:
                    screen.blit(block.image, (i * 100. + block_s, block.y))

            
            while len(map_queue_2) < 2:
                rand = random.randrange(6) % 3
                for i in map_list[rand]:
                    map_queue_2.append(i)
            pygame.display.update()

if __name__ == '__main__':
    main()
