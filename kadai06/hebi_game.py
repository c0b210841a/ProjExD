import pygame as pg
from pygame.locals import *
import random

#ウィンドウサイズの設定
WIDTH  = 600
HEIGHT = 600

#スクリーン設定
SCREEN = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption('Snake Game')

#色の設定
RED    = (200, 50, 50)
BLUE   = (93, 216, 228)
GREEN  = (0, 255, 50)
PGREEN = (152,251,152)
LGREEN = (144,238,144)
YELLOW = (255, 255, 0)
BLACK  = (50, 50, 50)
WHITE  = (255, 255, 255)

#clockとfpsの設定
CLOCK = pg.time.Clock()
FPS = 10

#1マス辺りのサイズ設定
CHIP_SIZE = 30

#テキスト描画用の関数
def draw_text(text, size, x, y, color):
		font = pg.font.Font(None, size)
		text_surface = font.render(text, True, color)
		text_rect = text_surface.get_rect()
		text_rect.midtop = (x, y)
		SCREEN.blit(text_surface,text_rect)

    
#background class
class Background():
    def __init__(self):
        self.image = pg.Surface((CHIP_SIZE,CHIP_SIZE))
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)
        #画面全体のマスサイズを設定　600/30=20
        self.bg_row = int(WIDTH / CHIP_SIZE) 
        self.bg_col = int(HEIGHT / CHIP_SIZE)
 
    #描画メソッド
    def draw(self):
        #1マス飛ばしで色違いで描画していく
        for col in range(0, self.bg_col,2):
            for row in range(0, self.bg_row, 1):
                pg.draw.rect(SCREEN,LGREEN,(CHIP_SIZE * row,CHIP_SIZE * col,CHIP_SIZE,CHIP_SIZE))
            for row in range(1, self.bg_row, 2):
                pg.draw.rect(SCREEN,PGREEN,(CHIP_SIZE * row,CHIP_SIZE * col,CHIP_SIZE,CHIP_SIZE))
        #上記とは行違いで描画する
        for col in range(1, self.bg_col,2):
            for row in range(0, self.bg_row, 1):
                pg.draw.rect(SCREEN,PGREEN,(CHIP_SIZE * row,CHIP_SIZE * col,CHIP_SIZE,CHIP_SIZE))
            for row in range(1, self.bg_row, 2):
                pg.draw.rect(SCREEN,LGREEN,(CHIP_SIZE * row,CHIP_SIZE * col,CHIP_SIZE,CHIP_SIZE))


class Player:
    def __init__(self, x, y):
        #基本の設定
        self.image = pg.Surface((CHIP_SIZE,CHIP_SIZE))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        
        #移動幅の設定
        self.dx = CHIP_SIZE
        self.dy = CHIP_SIZE
        #長さの設定
        self.length = 1
        self.max_length = 50
        #動いたルートを記録用のリスト
        self.body_list = [(x, y)]

        #移動用の判定
        self.RIGHT = False
        self.LEFT  = False
        self.UP    = False
        self.DOWN  = False 

        #プレイ中かの判定
        self.PLAY = True 

    #自分自身に接触したかチェック用メソッド
    def check_collision_self(self):
        if len(self.body_list) > 3:
            pos = self.body_list[-1]
            if pos in self.body_list[:-3]:
                self.gameover()
                self.PLAY = False

    #ゲームオーバー時にテキスト描画するメソッド
    def gameover(self):
        draw_text('Game Over', 100, WIDTH / 2, int(HEIGHT * 0.45), WHITE)
        draw_text('SPACE_KEY to RESTART', 80, int(WIDTH / 2), int(HEIGHT / 1.5), WHITE)
        self.PLAY = False

    #動いたルートをリストに追加していくメソッド
    def log_append(self,x,y):
        if len(self.body_list) < self.length and len(self.body_list) < self.max_length:
            self.body_list.append((x , y))
        else:
            self.body_list.append((x,y))
            self.body_list.pop(0) 

    #キー操作用のメソッド
    def move(self):
        if self.PLAY:
            key = pg.key.get_pressed()
            #右に動いている時は左の入力は無効（以下3方向とも同じ処理）
            if key[K_LEFT]:
                if not self.RIGHT:
                    self.LEFT = True
                    self.RIGHT, self.UP, self.DOWN = False, False, False
            if key[K_RIGHT]:
                if not self.LEFT:
                    self.RIGHT = True
                    self.LEFT, self.UP, self.DOWN = False, False, False
            if key[K_UP]:
                if not self.DOWN:
                    self.UP = True
                    self.RIGHT, self.LEFT, self.DOWN = False, False, False
            if key[K_DOWN]:
                if not self.UP:
                    self.DOWN = True
                    self.RIGHT, self.UP, self.LEFT = False, False, False

            #それぞれがTRUEなら速度を足す
            if self.RIGHT:
                self.rect.x += self.dx
                #ルートのリストに動いた位置を追加
                self.log_append(self.rect.x,self.rect.y)
            if self.LEFT:
                self.rect.x -= self.dx
                self.log_append(self.rect.x,self.rect.y)
            if self.UP:
                self.rect.y -= self.dy
                self.log_append(self.rect.x,self.rect.y)
            if self.DOWN:
                self.rect.y += self.dy     
                self.log_append(self.rect.x,self.rect.y)

    #壁に当たったかの判定用メソッド
    def check_wall_collide(self):
        if self.rect.right > WIDTH or self.rect.left < 0 or self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.gameover()      
    
    #描画メソッド
    def draw(self):
        #リストをfor文で一つづつ描画
        for list in self.body_list:
            pg.draw.rect(SCREEN, BLUE, (list[0],list[1],self.width,self.height))
        
    #全ての処理をアップデートメソッドにまとめる    
    def update(self):
        self.move()
        self.draw()     
        #衝突判定のメソッドを実行
        self.check_wall_collide()
        self.check_collision_self()

    def respawn(self,x,y):
        self.length = 1
        self.body_list = [(x,y)]
#food class
class Food:
    def __init__(self, x, y):
        self.image = pg.Surface((CHIP_SIZE,CHIP_SIZE))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
    
    #foodの位置をランダムに決める為のメソッド
    #初期値はWIDTH,HEIGHT=800,CHIP_SIZE=20
    def lottery(self):
        self.rect.x,self.rect.y = random.randint(0,int(WIDTH / CHIP_SIZE) - 1) * CHIP_SIZE, random.randint(0,int(WIDTH / CHIP_SIZE) - 1) * CHIP_SIZE
        return self.rect.x, self.rect.y

    #描画メソッド
    def draw(self):
        pg.draw.rect(SCREEN, RED,(self.rect.x,self.rect.y,CHIP_SIZE,CHIP_SIZE))

#ゲームクラス
class Game:
    def __init__(self):
        #pygameとmixerの初期化
        pg.init()
        
        #スコア設定
        self.score = 0
        
        #速度設定
        self.speed = 0
        self.max_speed = 10

        #プレイヤーインスタンス化（初期位置は適当に決定、真ん中辺りに）
        self.player = Player(CHIP_SIZE * 10,CHIP_SIZE * 10)
        
        #メソッドでfoodの初期位置をランダムで決める
        #foodのインスタンス化
        self.food = Food(random.randrange(0,WIDTH,CHIP_SIZE),random.randrange(0,HEIGHT,CHIP_SIZE) )
        #バックグラウンドのインスタンス化
        self.bg = Background()

        
    #スコア描画用メソッド
    def draw_score(self):
        draw_text(f'SCORE: {self.score}', 80, int(WIDTH / 2), 20, WHITE)


    #メインループ処理メソッド
    def main(self):
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                if event.type == pg.KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                
                if self.player.PLAY == False:
                   
                    if event.type == pg.KEYDOWN:
                        if event.key == K_SPACE:
                            self.score = 0
                            self.player.rect.x,self.player.rect.y = CHIP_SIZE * 10,CHIP_SIZE * 10
                            self.player.respawn(CHIP_SIZE * 10,CHIP_SIZE * 10)
                            self.player.PLAY = True
                            self.speed = 0

            #背景描画
            SCREEN.fill(WHITE)

            #バックグラウンドの描画
            self.bg.draw()
            # #foodの描画
            self.food.draw()
            # #プレイヤーの描画と動き用のメソッド呼び出し     
            self.player.update()

            #スコア描画
            self.draw_score()

            # #playerとfoodの衝突判定
            if self.player.rect.colliderect(self.food.rect):
                self.food.lottery()
                self.player.length += 1
                self.score += 100
                if self.speed < self.max_speed:
                    self.speed += 1
                try:
                    self.get_food_sound.play()
                except:
                    pass
                
            #ゲーム全体の速度設定
            CLOCK.tick(FPS + self.speed)
            #全体をアップデート
            pg.display.update()
        pg.quit()

#ゲームクラスのインスタンス化
game = Game()
#ゲームクラスのメソッドを実行（これでゲームスタートする）
game.main()