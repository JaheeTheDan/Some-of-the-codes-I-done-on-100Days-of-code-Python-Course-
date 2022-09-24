'''Main game code'''
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

#1 being slow and anything lower gradually get faster
GAME_SPEED = 0.08

def collisions():
    '''To detect the different kind of collisions'''
    head = snake.head
    body = snake.segments[1:]

    def wall_collision():
        x, y = head.pos()
        if x > 290 or x < -300 or y > 300 or y < -290:
            return True
        return False

    def body_collision():
        if True in [head.distance(segment)<10 for segment in body]:
            return True
        return False

    if wall_collision() or body_collision():
        return True
    return False


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()

screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')


while True:
    screen.update()
    time.sleep(GAME_SPEED)
    snake.move()

    # Detect collisions with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score_board.add_score()
        score_board.show_score()
        snake.extend_snake()

    # Detect collisions with wall and itself.
    if collisions():
        score_board.game_over()
        time.sleep(1)
        score_board.reset()
        snake.reset()
        food.refresh()
