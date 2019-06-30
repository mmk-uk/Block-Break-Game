
from math import radians
from math import degrees
from math import sin
from math import cos
from math import acos
import pyxel

#ボールとバーの接触判定に用いるバーの位置を保存するグローバル変数
bar_x = 0

#ボール管理のクラス
class BallList:
    def __init__(self):
        #ボールを保存するリスト
        self.balls = []

    #ボールを追加する関数
    def increase(self,ball):
        self.balls.append(ball)

    #管理しているボールを描画する関数
    def draw(self):
        #ボールがなかったら描画しない
        if len(self.balls) > 0:
            for ball in self.balls:
                ball.draw()
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
        self.vector = -90

    #ボールの位置を動かす関数
    def move(self):
        self.x = (self.x + self.speed*cos(radians(self.vector))) % pyxel.width
        self.y = (self.y + self.speed*sin(radians(self.vector))) % pyxel.height

    #ボールとバーとの接触判定を行う関数
    def bar_collision(self):
        if (self.y+2)>99 and (self.y+2)<104:
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
    def draw(self):
        #接触判定や動きの処理
        self.bar_collision()
        self.edge_collision()
        self.move()
        #描画
        pyxel.circ(self.x,self.y,2,10)

#バーのクラス
class Bar:
    def __init__(self):
        #バーの位置
        self.x = 72
        self.y = 100
        #バーの移動速度
        self.speed = 4

    #右方向への移動
    def right(self):
        #端に着いたら行かないようにする
        if self.x<144:
            self.x = (self.x + self.speed) % pyxel.width

    #左方向への移動
    def left(self):
        #端に着いたら行かないようにする
        if self.x>0:
            self.x = (self.x - self.speed) % pyxel.width

    #バーを描画する関数
    def draw(self):
        #バーのx座標の位置をグローバル変数に保存しておく(ボールとバーの接触判定に用いる)
        global bar_x
        bar_x = self.x
        #描画
        pyxel.rect(self.x, self.y, 16, 4, 9)


class App:
    def __init__(self):
        #ゲームの設定を行う
        pyxel.init(160,120,caption="ブロック崩し",fps=45)
        self.bar = Bar()
        self.balllist = BallList()
        self.balllist.increase(Ball(80,80))
        #フレーム毎にupdateとdrawを呼び出す
        pyxel.run(self.update, self.draw)

    def update(self):
        #ボタンを押した時の処理
        if pyxel.btn(pyxel.KEY_A):
            self.bar.left()
        if pyxel.btn(pyxel.KEY_D):
            self.bar.right()
        if pyxel.btn(pyxel.KEY_T):
            self.balllist.increase(Ball(80,80))

    def draw(self):
        #背景を真っ黒に
        pyxel.cls(0)
        #バーの描画
        self.bar.draw()
        #ボールの描画
        self.balllist.draw()


App()
