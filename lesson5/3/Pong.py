# Pong.py
import tkinter as tk
import threading
from Ball import Ball
from Paddle import Paddle
import appSettings

class Pong:
    def __init__(self, root, WIDTH, HEIGHT, MARGIN):
        self.left_points = 0
        self.right_points = 0
        self.left_up = False
        self.left_down = False
        self.right_up = False
        self.right_down = False
        self.render = True

        self.root = root
        self.width = WIDTH
        self.height = HEIGHT
        self.margin = MARGIN

        self.root.title("Pong Game")
        self.root.geometry(f"{self.width}x{self.height}")

        self.canvas = tk.Canvas(self.root, bg='black', width=self.width, height=self.height)
        self.canvas.pack()

        # Initialize Paddle and Ball objects
        self.paddle_left = Paddle(self.canvas, MARGIN, HEIGHT / 2, WIDTH / 50, HEIGHT / 6, HEIGHT)
        self.paddle_right = Paddle(self.canvas, WIDTH - MARGIN, HEIGHT / 2, WIDTH / 50, HEIGHT / 6, HEIGHT)
        self.ball = Ball(self.canvas, WIDTH / 50, appSettings.VELOCITY, WIDTH, HEIGHT)

        self.draw_middle_lines()
        self.draw_board()
        self.move()

    def draw_middle_lines(self):
        # Draw middle lines logic
        return 0

    def draw_board(self):
        self.draw_points()
        self.paddle_left.draw()
        self.paddle_right.draw()
        self.ball.draw()

    def draw_points(self):
        # Draw po
        return 0

    def move(self):
        if self.render:
            self.timer = threading.Timer(0.05, self.move)
            self.timer.start()
            # Implement game logic here
            
    

if __name__ == "__main__":
    root = tk.Tk()
    pong_game = Pong(root, appSettings.WIDTH, appSettings.HEIGHT, appSettings.MARGIN)
    root.mainloop()