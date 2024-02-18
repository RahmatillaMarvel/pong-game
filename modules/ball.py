from turtle import Turtle

class Ball(Turtle):
    """A class to represent the ball in the Pong game."""

    def __init__(self) -> None:
        """Initialize the ball."""
        super().__init__(shape='circle')
        self.color('white')
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.goto(0, 0)
        self.x: int = 10
        self.y: int = 10
        self.move_speed: float = 0.1
    
    def move(self) -> None:
        """Move the ball."""
        self.new_x: int = self.xcor() + self.x
        self.new_y: int = self.ycor() + self.y
        self.goto(self.new_x, self.new_y)
        
    def bounce_y(self) -> None:
        """Change the y direction of the ball."""
        self.y *= -1
        
    def bounce_x(self) -> None:
        """Change the x direction of the ball and adjust move speed."""
        self.x *= -1
        self.move_speed *= 0.95

    def reset_position(self) -> None:
        """Reset the position of the ball and reset move speed."""
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
