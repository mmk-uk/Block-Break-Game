import pyxel

#バーのクラス
class Bar:
    def __init__(self):
        #バーの位置
        self.x = 72
        self.y = 110
        #バーの移動速度
        self.speed = 2

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

    def center(self):
        self.x = 72

    #バーを描画する関数
    def draw(self):
        #描画
        pyxel.rect(self.x, self.y, 16, 4, 9)
        #バーのx座標の位置を返す
        return self.x
