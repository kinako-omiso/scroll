import pyxel

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.gravity = 0.5
        self.w, self.h = 16, 16

    def update(self):
        # 1. 入力処理（修正済み）
        self.vx = 0
        if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.KEY_A):   self.vx = -2
        if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_D):  self.vx = 2

        # X移動
        self.x += self.vx
        if self.check_collision(self.x, self.y):
            self.x -= self.vx

        # 2. Y移動と重力
        self.vy += self.gravity
        self.y += self.vy
        if self.check_collision(self.x, self.y):
            self.y -= self.vy
            self.vy = 0

        # 3. ジャンプ（重力方向によって向きを変える）
        if pyxel.btnp(pyxel.KEY_SPACE) and self.is_on_ground():
            # gravity > 0 なら上へ(-5)、gravity < 0 なら下へ(+5)
            jump_power = -5 if self.gravity > 0 else 5
            self.vy = jump_power

        # 重力反転
        if pyxel.btnp(pyxel.KEY_G):
            self.gravity *= -1
            # 反転した瞬間、少しだけ初速を与えると操作感が良くなる
            self.vy = 0 

    def is_on_ground(self):
        # 重力が下向きなら「1ピクセル下」に地面があるか
        # 重力が上向きなら「1ピクセル上」に地面があるか
        check_y = self.y + self.h + 1 if self.gravity > 0 else self.y - 1
        return self.check_collision(self.x, check_y)

    def check_collision(self, x, y):
        # 簡易的な画面端判定（後でタイルマップ判定に変えること）
        if x < 0 or x > 240 or y < 0 or y > 240:
            return True
        return False

    def draw(self):
        pyxel.rect(self.x, self.y, self.w, self.h, 9)