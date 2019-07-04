from math import *
import pyxel

#ボール管理のクラス
class BallList:
    def __init__(self):
        #ボールを保存するリスト
        self.balls = []

    #ボールを追加する関数
    def increase(self,ball):
        self.balls.append(ball)

    #管理しているボールを描画する関数
    def draw(self,bar_x):
        #ボールがなかったら描画しない
        if len(self.balls) > 0:
            for ball in self.balls:
                ball.draw(bar_x)
                #ボールが下端に接触したらボールを消す
                if (ball.y+2)>117:
                    self.balls.remove(ball)

#ボールのクラス
class Ball:
    def __init__(self,x,y):
        #ボールの位置
        self.x = x
        self.y = y
        #ボールのスピード
        self.speed = 2
        #ボールの進む角度
        self.vector = 90

    #ボールの位置を動かす関数
    def move(self):
        self.x = (self.x + self.speed*cos(radians(self.vector))) % pyxel.width
        self.y = (self.y + self.speed*sin(radians(self.vector))) % pyxel.height

    #ボールとバーとの接触判定を行う関数
    def bar_collision(self,bar_x):
        if (self.y+2)>109 and (self.y+2)<114:
            if self.x>=bar_x-1 and self.x<=bar_x+17:
                #ボールがバーと接触した部分によって角度を変える
                dis = (self.x-(bar_x+9))/10
                self.vector = int(degrees(-acos(dis)))

    #ボールと端との接触判定を行う関数
    def edge_collision(self):
        if (self.x+2)>158:
            self.vector = 180 - self.vector
        if (self.x-2)<2:
            self.vector = 180 - self.vector
        if (self.y+2)>120:
            pass
        if (self.y-2)<2:
            self.vector = -self.vector

    #ボールを描画する関数
    def draw(self,bar_x):
        #接触判定や動きの処理
        self.bar_collision(bar_x)
        self.edge_collision()
        self.move()
        #描画
        pyxel.circ(self.x,self.y,2,10)
