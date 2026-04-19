import random
import pyxel

CELL_SIZE = 8
GRID_W = 20
GRID_H = 15
SCREEN_W = GRID_W * CELL_SIZE
SCREEN_H = GRID_H * CELL_SIZE + 16

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)


class SnakeGame:
    def __init__(self):
        pyxel.init(SCREEN_W, SCREEN_H, title="Snake and Apple", fps=10)
        self.best_score = 0
        self.reset_game()
        pyxel.run(self.update, self.draw)

    def reset_game(self):
        self.snake = [(GRID_W // 2, GRID_H // 2)]
        self.direction = RIGHT
        self.next_direction = RIGHT
        self.apple = self.spawn_apple()
        self.score = 0
        self.game_over = False

    def spawn_apple(self):
        while True:
            pos = (random.randint(0, GRID_W - 1), random.randint(0, GRID_H - 1))
            if pos not in self.snake:
                return pos

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if self.game_over:
            if pyxel.btnp(pyxel.KEY_R):
                self.reset_game()
            return

        if pyxel.btnp(pyxel.KEY_UP) and self.direction != DOWN:
            self.next_direction = UP
        elif pyxel.btnp(pyxel.KEY_DOWN) and self.direction != UP:
            self.next_direction = DOWN
        elif pyxel.btnp(pyxel.KEY_LEFT) and self.direction != RIGHT:
            self.next_direction = LEFT
        elif pyxel.btnp(pyxel.KEY_RIGHT) and self.direction != LEFT:
            self.next_direction = RIGHT

        self.direction = self.next_direction
        head_x, head_y = self.snake[0]
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy)

        if (
            new_head[0] < 0
            or new_head[0] >= GRID_W
            or new_head[1] < 0
            or new_head[1] >= GRID_H
            or new_head in self.snake
        ):
            self.game_over = True
            self.best_score = max(self.best_score, self.score)
            return

        self.snake.insert(0, new_head)

        if new_head == self.apple:
            self.score += 1
            self.apple = self.spawn_apple()
        else:
            self.snake.pop()

    def draw_grid(self):
        for x in range(0, SCREEN_W, CELL_SIZE):
            pyxel.line(x, 0, x, GRID_H * CELL_SIZE - 1, 1)
        for y in range(0, GRID_H * CELL_SIZE, CELL_SIZE):
            pyxel.line(0, y, SCREEN_W - 1, y, 1)

    def draw(self):
        pyxel.cls(0)
        self.draw_grid()

        ax, ay = self.apple
        pyxel.rect(ax * CELL_SIZE, ay * CELL_SIZE, CELL_SIZE, CELL_SIZE, 8)
        pyxel.pset(ax * CELL_SIZE + 2, ay * CELL_SIZE + 2, 7)

        for i, (x, y) in enumerate(self.snake):
            color = 11 if i == 0 else 3
            pyxel.rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE, color)

        pyxel.rect(0, GRID_H * CELL_SIZE, SCREEN_W, 16, 13)
        pyxel.text(4, GRID_H * CELL_SIZE + 4, f"SCORE: {self.score}", 7)
        pyxel.text(60, GRID_H * CELL_SIZE + 4, f"BEST: {self.best_score}", 10)

        if self.game_over:
            pyxel.rect(12, 40, SCREEN_W - 24, 32, 0)
            pyxel.rectb(12, 40, SCREEN_W - 24, 32, 8)
            pyxel.text(24, 48, "GAME OVER", 8)
            pyxel.text(20, 58, "PRESS R TO RESTART", 7)
        else:
            pyxel.text(4, 2, "ARROWS TO MOVE", 5)
            pyxel.text(4, 10, "Q TO QUIT", 5)


SnakeGame()