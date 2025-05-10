from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        # Try to read high score, create file if doesn't exist
        try:
            with open("high_score.txt", "r") as file:
                self.high_score = int(file.read())
        except (FileNotFoundError, ValueError):
            self.high_score = 0
            with open("high_score.txt", "w") as file:
                file.write("0")
                
        self.current_score = 0
        self.level = 1
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 320)
        self.update_score()
        
    def increase_score(self):
        """Increase player score"""
        self.current_score += 10
        # Update high score if needed
        if self.current_score > self.high_score:
            self.high_score = self.current_score
            self.save_high_score()
    
    def level_up(self):
        """Increase level when all aliens destroyed"""
        self.level += 1
        self.update_score()
    
    def update_score(self):
        """Refresh the score display"""
        self.clear()
        self.goto(-300, 320)
        self.write(f"Score: {self.current_score}", align="left", font=("Courier", 16, "normal"))
        self.goto(0, 320)
        self.write(f"Level: {self.level}", align="center", font=("Courier", 16, "normal"))
        self.goto(300, 320)
        self.write(f"High Score: {self.high_score}", align="right", font=("Courier", 16, "normal"))
    
    def game_over(self):
        """Display game over message"""
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 30, "normal"))
        self.goto(0, -50)
        self.write(f"Final Score: {self.current_score}", align="center", font=("Courier", 20, "normal"))
        self.save_high_score()
    
    def save_high_score(self):
        """Save high score to file"""
        with open("high_score.txt", "w") as file:
            file.write(str(self.high_score))