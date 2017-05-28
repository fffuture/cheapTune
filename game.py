#! /usr/bin/python2

import pygame

WIN_WIDTH = 41
WIN_HEIGHT = 41
WINDOW = (WIN_WIDTH, WIN_HEIGHT)
NOFRAME = 'NOFRAME'
BG_COLOR = "#ff7f7f"
PAD_COLOR = (45,45,45)
PRESSED_PAD_COLOR = (255,0,0)

def main():
    pygame.mixer.pre_init(44100, -16, 1, 512)
    pygame.init()
    screen = pygame.display.set_mode(WINDOW, pygame.NOFRAME)
    bg = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
    bg.fill(pygame.Color(BG_COLOR))
    clock = pygame.time.Clock()

    buttons = create_buttons()
    samples = load_samples()

    RUN = True
    while RUN:
        pressed = None
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    RUN = False
                if e.key == pygame.K_z:
                    pressed = (0,3)
                if e.key == pygame.K_x:
                    pressed = (1,3)
                if e.key == pygame.K_c:
                    pressed = (2,3)
                if e.key == pygame.K_v:
                    pressed = (3,3)
                if e.key == pygame.K_a:
                    pressed = (0,2)
                if e.key == pygame.K_s:
                    pressed = (1,2)
                if e.key == pygame.K_d:
                    pressed = (2,2)
                if e.key == pygame.K_f:
                    pressed = (3,2)
                if e.key == pygame.K_q:
                    pressed = (0,1)
                if e.key == pygame.K_w:
                    pressed = (1,1)
                if e.key == pygame.K_e:
                    pressed = (2,1)
                if e.key == pygame.K_r:
                    pressed = (3,1)
                if e.key == pygame.K_1:
                    pressed = (0,0)
                if e.key == pygame.K_2:
                    pressed = (1,0)
                if e.key == pygame.K_3:
                    pressed = (2,0)
                if e.key == pygame.K_4:
                    pressed = (3,0)
        if pressed:
            samples[pressed[1]][pressed[0]].play()

        draw_button(buttons, bg, pressed)
        screen.blit(bg, (0, 0))
        pygame.display.update()
        clock.tick(40)

def create_buttons():
    arr = [[],[],[],[]]
    for x in range(0,4):
        arr[x] = [pygame.Rect(1+x*10, 1+y*10, 9, 9) for y in range(0,4)]
    return arr

def load_samples():
    arr = [['samples/kick1.wav','samples/kick2.wav','samples/kick3.wav','samples/kick4.wav'],
           ['samples/hihat1.wav','samples/hihat2.wav','samples/tom1.wav','samples/tom2.wav'],
           ['samples/snare1.wav','samples/snare4.wav','samples/clap.wav','samples/kick7.wav'],
           ['samples/snare2.wav','samples/snare3.wav','samples/cowbell.wav','samples/kick8.wav']]
    for x in range(0,4):
        arr[x] = [pygame.mixer.Sound(arr[x][y]) for y in range(0,4)]
    return arr

def draw_button(outside, bg, pressed=None):
    for line in outside:
        for item in line:
            if pressed:
                if (outside.index(line) == pressed[0] and line.index(item) == pressed[1]):
                    pygame.draw.rect(bg, PRESSED_PAD_COLOR, item)
                else:
                    pygame.draw.rect(bg, PAD_COLOR, item)    
            else:    
                pygame.draw.rect(bg, PAD_COLOR, item)


if __name__ == "__main__":
    main()
