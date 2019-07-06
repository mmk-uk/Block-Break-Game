
from math import *
import pyxel

#ブロック、ボール、バーの読み込み
import block
import ball
import bar

class Game:
    def __init__(self):
        #ゲームの設定を行う
        pyxel.init(160,120,caption="ブロック崩し",fps=45)

        self.playing = False

        # 作成したドット絵やタイルマップの情報を読み込む
        pyxel.load('BB_graphic.pyxres')


        self.bar = bar.Bar()
        self.balllist = ball.BallList()


        self.blockset = block.BlockSet()


        #フレーム毎にupdateとdrawを呼び出す
        pyxel.run(self.update, self.draw)

    def update(self):
        if self.playing == True:
            #ボタンを押した時の処理
            if pyxel.btn(pyxel.KEY_A):
                self.bar.left()
            if pyxel.btn(pyxel.KEY_D):
                self.bar.right()
            if pyxel.btn(pyxel.KEY_T):
                self.balllist.increase(ball.Ball(80,80))
            if len(self.balllist.balls)==0:
                self.playing = False
        else:
            if pyxel.btnp(pyxel.KEY_S):
                self.playing = True
                self.bar.center()
                self.blockset.block_reset()
                self.balllist.increase(ball.Ball(80,80))

    def draw(self):

        if self.playing == True:
            #背景を真っ黒に
            pyxel.cls(0)
            #バーの描画
            bar_x = self.bar.draw()
            #ボールの描画
            self.balllist.draw(bar_x)
            #ブロックの表示
            self.blockset.set(self.balllist.balls)
        else:
            pyxel.cls(0)
            pyxel.bltm(13,2,0,0,0,16,16)



Game()
