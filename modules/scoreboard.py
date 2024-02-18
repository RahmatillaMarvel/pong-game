from turtle import Turtle

class Scoreboard(Turtle):
    """A class to represent the scoreboard in the Pong game."""

    def __init__(self) -> None:
        """Initialize the scoreboard."""
        super().__init__(visible=False)
        self.color('green')
        self.penup()
        self.right_player: int = 0
        self.left_player: int = 0
        self.goto(0, 200)
        self.update_scoreboard()

    def update_scoreboard(self) -> None:
        """Update the scoreboard display."""
        self.clear()
        self.write(f'{self.right_player} : {self.left_player}', align='center', font=("Arial", 50, "normal"))

    def l_point(self) -> None:
        """Add a point to the left player's score."""
        self.left_player += 1
        self.update_scoreboard()

    def r_point(self) -> None:
        """Add a point to the right player's score."""
        self.right_player += 1
        self.update_scoreboard()
