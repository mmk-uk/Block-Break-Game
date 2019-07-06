from math import *
import pyxel

#ブロックの横の数
block_num_x = 10
#ブロックの縦の数
block_num_y = 6


#ブロック管理のクラス
class BlockSet:
    def __init__(self):
        #ブロックの座標間隔の計算
        self.dis_x = (pyxel.width-10)//block_num_x
        self.dis_y = (pyxel.height-50)//block_num_y

        #ブロックの大きさの計算
        self.block_w = self.dis_x - 2
        self.block_h = self.dis_y - 2

        #ブロックの描画開始x座標の計算
        self.start_x = (pyxel.width-(self.block_w*block_num_x)-(2*(block_num_x-1)))//2

        #ブロックの管理するリスト
        self.blocklist = []

        #接触判定の使用する角度
        self.corner1 = degrees(atan2(-self.block_h/2,self.block_w/2))
        self.corner2 = degrees(atan2(self.block_h/2,self.block_w/2))
        self.corner3 = degrees(atan2(-self.block_h/2,-self.block_w/2))
        self.corner4 = degrees(atan2(self.block_h/2,-self.block_w/2))

    def block_reset(self):
        del self.blocklist[:]
        #ブロックを生成
        for i in range(block_num_y):
            for j in range(block_num_x):
                self.blocklist.append(Block(j*self.dis_x+self.start_x,i*self.dis_y+2,self.block_w,self.block_h))

    #ブロックを表示する関数
    def set(self,balls):
        for block in self.blocklist:
            if len(balls) == 0:
                block.draw()
            else:
                for ball in balls:
                    #ボールとの接触判定
                    if block.ball_collision(ball):
                        if ball.flag == False:
                            #ボールが当たって位置によって、ボールの角度を変える
                            if ball.x >= block.x and ball.x <= block.x+self.block_w:
                                ball.vector = -ball.vector
                            elif ball.y >= block.y and ball.y <= block.y+self.block_h:
                                ball.vector = 180-ball.vector
                            elif self.corner3 <= block.ball_direction and block.ball_direction <= self.corner1:
                                ball.vector = -ball.vector
                            elif self.corner1 < block.ball_direction and block.ball_direction < self.corner2:
                                ball.vector = 180-ball.vector
                            elif self.corner2 <= block.ball_direction and block.ball_direction <= self.corner4:
                                ball.vector = -ball.vector
                            else:
                                ball.vector = 180-ball.vector
                            ball.flag = True
                            #ボールが当たったのでブロックを消す
                            self.blocklist.remove(block)
                        else:
                            block.draw()
                    else:
                        block.draw()


#ブロックのクラス
class Block:
    def __init__(self,x,y,w,h):
        #ブロックの位置
        self.x = x
        self.y = y
        #ブロックの大きさ
        self.w = w
        self.h = h

        self.ball_direction = 0

    #ブロックを表示する関数
    def draw(self):
        pyxel.rect(self.x, self.y, self.w, self.h, 8)

    #ブロックがボールに接触しているかを判定する関数
    def ball_collision(self,ball):
        if ball.y-3 < self.y + self.h and ball.y+3 > self.y and ball.x-3 < self.x + self.w and ball.x+3 > self.x:
            #ブロックの中心地点
            block_center_x = self.x + self.w/2
            block_center_y = self.y + self.h/2
            #ブロックの中心から見たボールの角度を計算
            self.ball_direction = degrees(atan2(ball.y-block_center_y,ball.x-block_center_x))
            return True
