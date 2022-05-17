from turtle import Turtle
import pygame as pg
import sys

key_delta = {pg.K_UP  : [0,-1],
            pg.K_DOWN : [0,+1],
            pg.K_RIGHT: [+1,0],
            pg.K_LEFT : [-1,0]}

def main():
    clock = pg.time.Clock()

    #練習1
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((1500, 900)) #画面用Surface
    sc_rect= screen.get_rect()               #画面用Rect
    bg_img = pg.image.load("fig/pg_bg.jpg")   #背景画像用のSurface
    bg_rect= bg_img.get_rect()               #背景画像用のRect
    #bg_rect.center = (1500, 500)
    screen.blit(bg_img, bg_rect)              #会計画像用Surfaceを画面用Surfaceに張り付ける
    
    #練習3
    tori_img = pg.image.load("fig/3.png")
    tori_img = pg.transform.rotozoom(tori_img, 0, 2)
    tori_rect= tori_img.get_rect()
    tori_rect.center = 900, 400             #こうかとん画像の中心座標
    screen.blit(tori_img, tori_rect)        #こうかとん画像surfaceを画面用surfaceに張り付ける




    while True:
        #練習2
        screen.blit(bg_img, bg_rect)
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        #練習4
        key_states = pg.key.get_pressed()
        for key, delta in key_delta.items():
            if key_states[key] == True:
                tori_rect.centerx += delta[0]
                tori_rect.centery += delta[1]
        screen.blit(tori_img, tori_rect)


        pg.display.update() #画面の更新
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()  
    main()
    pg.quit()
    sys.exit()
