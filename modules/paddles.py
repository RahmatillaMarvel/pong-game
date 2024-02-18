from turtle import Turtle, Screen

class Paddle(Turtle):
    """A class to represent a paddle in the Pong game."""

    def __init__(self, screen: Screen, coordinates: tuple, control: str) -> None:
        """Initialize the paddle."""
        super().__init__(shape='square')
        self.color('white')
        self.penup()    
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(coordinates)
        self.screen: Screen = screen
        self.screen.listen()
        if control == 'a':
            self.screen.onkey(self.go_up, 'Up')
            self.screen.onkey(self.go_down, 'Down')
        else:
            self.screen.onkey(self.go_up, 'w')
            self.screen.onkey(self.go_down, 's')

    def go_up(self) -> None:
        """Move the paddle up."""
        new_y = self.ycor() + 100
        self.goto(self.xcor(), new_y)
    
    def go_down(self) -> None:
        """Move the paddle down."""
        new_y = self.ycor() - 100
        self.goto(self.xcor(), new_y)
