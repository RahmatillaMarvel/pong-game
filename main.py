# Import necessary modules and classes
from turtle import Turtle, Screen
from modules.paddles import Paddle
from modules.ball import Ball
from modules.scoreboard import Scoreboard
from time import sleep

# Set up the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

# Create paddles, ball, and scoreboard
paddle1 = Paddle(screen, (350, 0), 'a')  # Create right paddle
paddle2 = Paddle(screen, (-350, 0), 'b')  # Create left paddle
ball = Ball()  # Create ball
scoreboard = Scoreboard()  # Create scoreboard

# Set the initial game state
game_is_on = True

# Main game loop
while game_is_on:
    # Slow down the ball movement
    sleep(ball.move_speed)
    screen.update()  # Update the screen
    ball.move()  # Move the ball

    # Check for collision with top or bottom wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Check for collision with paddles and bounce
    if (ball.distance(paddle1) < 50 and ball.xcor() > 320) or (ball.distance(paddle2) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # Check for scoring on the right side
    if ball.xcor() > 380:
        ball.reset_position()  # Reset ball position
        scoreboard.r_point()  # Increment right player's score

    # Check for scoring on the left side
    if ball.xcor() < -380:
        ball.reset_position()  # Reset ball position
        scoreboard.l_point()  # Increment left player's score

# Close the game window when clicked
screen.exitonclick()
