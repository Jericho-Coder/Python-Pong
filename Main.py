# Import packages
import turtle

# Set up window
win = turtle.Screen()
win.setup(width=600, height=800)
win.title("Tetris byy Jericho Bondi")
win.bgpic("Tetris.gif")
win.bgcolor("black")

# Set up colors
colors = ["black", "lightblue", "blue", "orange", "yellow", "green", "purple", "red"]

# Set up grid
grid = [
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
[1, 2, 3, 4, 5, 6, 7, 0, 0, 0, 0, 0, ],
]

pen = turtle.Turtle()
pen.penup()
pen.speed(0)
pen.shape("square")

def draw_grid(pen,grid):
    top = 170
    left = -110

    for y in range(len(grid)):
       for x in range(len(grid[0])):
         screen_x = left + (x * 20)
         screen_y = top - (y * 20)
         color_number = grid[y][x]
         color = colors[color_number]
         pen.color(color)
         pen.goto(screen_x, screen_y)
         pen.stamp()

draw_grid(pen,grid)

while True:
    win.update()
#win.mainloop()