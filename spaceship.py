from turtle import Turtle

class Spaceship(Turtle):
    def __init__(self):
        super().__init__()
        self.color("blue")
        self.shape("turtle")
        self.penup()
        self.shapesize(1, 1)
        self.goto(0, -250)  # Start at bottom center
        self.setheading(90)
        self.bullets = []  # List to store active bullets
        self.speed = 20  # Movement speed
        self.bullet_speed = 10  # Bullet speed
        # Set boundary limits
        self.left_boundary = -320
        self.right_boundary = 320

    def move_left(self):
        """Move spaceship left while respecting boundary"""
        new_x = self.xcor() - self.speed
        if new_x > self.left_boundary:
            self.goto(new_x, self.ycor())

    def move_right(self):
        """Move spaceship right while respecting boundary"""
        new_x = self.xcor() + self.speed
        if new_x < self.right_boundary:
            self.goto(new_x, self.ycor())

    def shoot(self):
        """Create a new bullet at spaceship position"""
        # Limit number of bullets to avoid overwhelming
        if len(self.bullets) < 5:
            bullet = Turtle()
            bullet.penup()
            bullet.shape("square")
            bullet.shapesize(0.2, 0.2)
            bullet.color("yellow")
            bullet.setheading(90)
            bullet.goto(self.xcor(), self.ycor() + 20)  # Start from spaceship's position
            self.bullets.append(bullet)

    def move_bullets(self):
        """Move all active bullets upward"""
        for bullet in self.bullets:
            bullet.forward(self.bullet_speed)