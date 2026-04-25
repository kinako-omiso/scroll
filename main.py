import pyxel
#マジックナンバーはできる限り定数に置き換えるべき
SCREEN_WIDTH = 256
SCREEN_HEIGHT = 256
PLAYER_WIDTH = 16
PLAYER_HEIGHT = 16


class App:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, caption="Pyxel App")
        self.x = 0
        self.y = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        function.update
        

    def draw(self):
        pyxel.cls(0)