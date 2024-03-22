from appSettings import *

class Paddle:
    def __init__(self, canvas, center_x, center_y, width, height, board_height):
        self.canvas = canvas
        self.center_x = center_x
        self.center_y = center_y
        self.width = width
        self.height = height
        self.board_height = board_height

        self.paddle = self.canvas.create_rectangle(center_x - width / 2, center_y - height / 2, center_x + width / 2, center_y + height / 2, fill='white')

    def draw(self):
        self.canvas.coords(self.paddle, self.center_x - self.width / 2, self.center_y - self.height / 2, self.center_x + self.width / 2, self.center_y + self.height / 2)

    def top(self):
        # Move paddle up logic
        if self.center_y < self.height:
            self.center_y += VELOCITY
            self.draw
        return 0
    
    def down(self):
        # Move paddle down logic
        if self.center_y > 0:
            self.center_y -= VELOCITY
            self.draw
        return 0

    def collide_right(self):
        if self.center_x == 0:
            return 1
        else:
            return 0

    def collide_left(self):
        if self.center_x == self.height:
            return 1
        else:
            return 0