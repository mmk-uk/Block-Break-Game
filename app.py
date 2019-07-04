
from math import *
import pyxel

#ブロック、ボール、バーの読み込み
import block
import ball
import bar

class App:
    def __init__(self):
        #ゲームの設定を行う
        pyxel.init(160,120,caption="ブロック崩し",fps=45)
        self.bar = bar.Bar()
        self.balllist = ball.BallList()
        self.balllist.increase(ball.Ball(80,80))

        self.blockset = block.BlockSet()


        #フレーム毎にupdateとdrawを呼び出す
        pyxel.run(self.update, self.draw)

    def update(self):
        #ボタンを押した時の処理
        if pyxel.btn(pyxel.KEY_A):
            self.bar.left()
        if pyxel.btn(pyxel.KEY_D):
            self.bar.right()
        if pyxel.btn(pyxel.KEY_T):
            self.balllist.increase(ball.Ball(80,80))

    def draw(self):
        #背景を真っ黒に
        pyxel.cls(0)

        #バーの描画
        bar_x = self.bar.draw()

        #ボールの描画
        self.balllist.draw(bar_x)

        #ブロックの表示
        self.blockset.set(self.balllist.balls)


App()
