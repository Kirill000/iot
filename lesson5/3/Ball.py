import random

class Ball:
    def __init__(self, canvas, side, velocity, width, height):
        self.canvas = canvas
        self.side = side
        self.velocity = velocity
        self.width = width
        self.height = height

        self.x = width / 2
        self.y = height / 2
        self.dx = velocity
        self.dy = velocity

        self.ball = self.canvas.create_rectangle(self.x - side / 2, self.y - side / 2, self.x + side / 2, self.y + side / 2, fill='white')

    def draw(self):
        self.canvas.coords(self.ball, self.x - self.side / 2, self.y - self.side / 2, self.x + self.side / 2, self.y + self.side / 2)

    def restart(self):
        self.x = self.width / 2
        self.y = self.height / 2
        self.dx = random.choice([-1, 1]) * self.velocity
        self.dy = random.choice([-1, 1]) * self.velocity

    def move(self, pong, paddle):
        # Implement ball movement logic here
        # if self.x == 
        pass