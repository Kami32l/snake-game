from turtle import Screen
import time
from snake_class import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()

user_name = screen.textinput("User Name", "Whats your name? ").lower()
while len(user_name) < 3:
    user_name = screen.textinput("Too short Try Again", "Whats your name? ").lower()
scoreboard = Scoreboard()


def read():
    res = {}
    with open("scoreboard.txt", "r") as text:
        for line in text:
            key, value = line.split(":")
            if int(value) > res.get(key, -1):
                res[key] = int(value)
    return res


def read_and_compare():
    users_score_dict = read()
    if user_name in users_score_dict:
        scoreboard.highest_score = users_score_dict[user_name]


read_and_compare()


def snake_game():
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard.reset_score()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    game_is_on = True

    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # Detect collision with food.
        print("snake:", snake.head.position())
        print("food", food.position())
        if snake.head.distance(food) <= 10:
            food.refresh()
            scoreboard.print_score()
            snake.extend()

        # Detect collision with wall.
        x_pos = round(snake.head.xcor())
        y_pos = round(snake.head.ycor())
        if abs(x_pos) >= 300 or abs(y_pos) >= 300:
            # print("Wall Mate")
            game_is_on = False

        # Detect collision with tail.
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                # print("łeror")

    if scoreboard.score > scoreboard.highest_score:
        # Append-adds at last
        with open("scoreboard.txt", mode="a") as file:
            file.write(f"{user_name}:{scoreboard.score} \n")

    names_scores = read()
    # print(names_scores)

    scoreboard.game_over()

    play_again = screen.textinput("Replay", "Do you want to play again? ").lower()

    if play_again == "no":
        screen.clear()
        scoreboard.print_scoreboard(names_scores)

    else:

        screen.clear()
        snake_game()


snake_game()

screen.exitonclick()
