import tkinter as tk
import random

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")

        self.canvas = tk.Canvas(root, width=400, height=400, bg="black")
        self.canvas.pack()

        self.snake = [(20, 20), (20, 30), (20, 40)]
        self.snake_dir = "Down"
        self.food = self.create_food()

        self.game_over = False

        self.root.bind("<KeyPress>", self.change_direction)
        self.run_game()

    def create_food(self):
        x = random.randint(0, 39) * 10
        y = random.randint(0, 39) * 10
        return (x, y)

    def change_direction(self, event):
        new_dir = event.keysym
        all_dirs = ["Up", "Down", "Left", "Right"]
        opposites = (("Up", "Down"), ("Left", "Right"))

        if new_dir in all_dirs:
            if (self.snake_dir, new_dir) not in opposites:
                self.snake_dir = new_dir

    def move_snake(self):
        head_x, head_y = self.snake[-1]

        if self.snake_dir == "Up":
            new_head = (head_x, head_y - 10)
        elif self.snake_dir == "Down":
            new_head = (head_x, head_y + 10)
        elif self.snake_dir == "Left":
            new_head = (head_x - 10, head_y)
        elif self.snake_dir == "Right":
            new_head = (head_x + 10, head_y)

        self.snake.append(new_head)
        if new_head == self.food:
            self.food = self.create_food()
        else:
            self.snake.pop(0)

    def check_collision(self):
        head_x, head_y = self.snake[-1]
        if not (0 <= head_x < 400 and 0 <= head_y < 400):
            return True
        if len(self.snake) != len(set(self.snake)):
            return True
        return False

    def update_canvas(self):
        self.canvas.delete(tk.ALL)
        self.canvas.create_rectangle(self.food[0], self.food[1], self.food[0] + 10, self.food[1] + 10, fill="red")
        for segment in self.snake:
            self.canvas.create_rectangle(segment[0], segment[1], segment[0] + 10, segment[1] + 10, fill="green")

    def run_game(self):
        if not self.game_over:
            self.move_snake()
            self.game_over = self.check_collision()
            self.update_canvas()
            self.root.after(100, self.run_game)
        else:
            self.canvas.create_text(200, 200, text="Game Over", fill="white", font=("Helvetica", 24))

root = tk.Tk()
game = SnakeGame(root)
root.mainloop()