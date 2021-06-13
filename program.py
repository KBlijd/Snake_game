from ipy_lib import SnakeUserInterface

interface = SnakeUserInterface(32, 24, 1)
direction = 'r'
food = []
direction_list = ['u', 'd', 'l', 'r']

def generate_apple():
    global food
    food = [interface.random(32), interface.random(24)]

class Snake:
    def __init__(self):
        self.figure = [[0, 0], [0, 1]]

    def move(self, mov):
        if mov == 'r' and mov != 'l':
            self.figure.insert(0, [self.figure[0][0] + 1, self.figure[0][1]])
            if self.figure[0][0] > 31:
                self.figure[0][0] = 0
        elif mov == 'l' and mov != 'r':
            self.figure.insert(0, [self.figure[0][0] - 1, self.figure[0][1]])
            if self.figure[0][0] < 0:
                self.figure[0][0] = 31
        elif mov == 'u' and mov != 'd':
            self.figure.insert(0, [self.figure[0][0], self.figure[0][1] - 1])
            if self.figure[0][1] < 0:
                self.figure[0][1] = 23
        elif mov == 'd' and mov != 'u':
            self.figure.insert(0, [self.figure[0][0], self.figure[0][1] + 1])
            if self.figure[0][1] > 23:
                self.figure[0][1] = 0

    def eat(self, apple):
        if self.figure[0][0] == apple[0] and self.figure[0][1] == apple[1]:
            self.figure.append([apple[0], apple[1]])
            generate_apple()
            
    def collision_check(self):
        for j in self.figure[1:]:
            if self.figure[0][0] == j[0] and self.figure[0][1] == j[1]:
                interface.set_animation_speed(0)
                interface.clear_text()
                interface.print_('Game over')


snake = Snake()
generate_apple()
interface.set_animation_speed(10)
interface.print_('Good luck!')
for i in snake.figure:
    interface.place(i[0], i[1], 2)

while True:
    interface.show()
    interface.clear()
    event = interface.get_event()
    if event.data in direction_list:
        direction = event.data
    snake.move(direction)
    snake.figure.pop()
    snake.collision_check()
    snake.eat(food)
    interface.place(food[0], food[1], 1)
    for i in snake.figure:
        interface.place(i[0], i[1], 2)