import pyxel

class Bar:
    def __init__(self):
        self.x = 72
        self.y = 100

    def right(self):
        if self.x<144:
            self.x = (self.x + 2) % pyxel.width

    def left(self):
        if self.x>0:
            self.x = (self.x - 2) % pyxel.width

    def draw(self):
        pyxel.rect(self.x, self.y, 16, 4, 10)


class App:
    def __init__(self):
        pyxel.init(160,120)
        self.bar = Bar()
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btn(pyxel.KEY_A):
            self.bar.left()
        if pyxel.btn(pyxel.KEY_D):
            self.bar.right()

    def draw(self):
        #背景を真っ黒に
        pyxel.cls(0)
        self.bar.draw()


App()
