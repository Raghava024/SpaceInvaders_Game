import random
from turtle import Turtle

class Aliens:
    def __init__(self):
        self.herd = []
        self.poison = []  # List for alien projectiles
        self.venom_speed = 5
        self.move_speed = 10
        self.create_aliens()

    def create_aliens(self):
        """Create a grid of alien enemies"""
        # Clear any remaining aliens
        for alien in self.herd:
            alien.hideturtle()
        self.herd = []
        
        # Create new grid of aliens
        for row in range(3):  # 3 rows
            for col in range(10):  # 10 columns
                new_alien = Turtle()
                new_alien.color("green")
                new_alien.shape("triangle")
                new_alien.shapesize(0.75, 0.75)
                new_alien.setheading(270)
                new_alien.penup()
                # Position in grid formation
                x_pos = -270 + col * 60
                y_pos = 250 - row * 40
                new_alien.goto(x_pos, y_pos)
                self.herd.append(new_alien)

    def move_herd(self, direction):
        """Move all aliens sideways and occasionally down"""
        for alien in self.herd:
            alien.goto(alien.xcor() + (self.move_speed * direction), alien.ycor())
            
        # Check if any alien is at screen edge
        for alien in self.herd:
            if alien.xcor() > 320 or alien.xcor() < -320:
                # Move all aliens down
                for a in self.herd:
                    a.goto(a.xcor(), a.ycor() - 20)
                return True  # Signal to change direction
        return False

    def shoot(self):
        """Random alien shoots venom"""
        if self.herd:  # Only shoot if there are aliens
            # Select random alien to shoot
            shooting_alien = random.choice(self.herd)
            
            venom = Turtle()
            venom.penup()
            venom.shape("square")
            venom.shapesize(0.2, 0.2)
            venom.color("red")
            venom.setheading(270)  # Head downward
            venom.goto(shooting_alien.xcor(), shooting_alien.ycor() - 10)
            self.poison.append(venom)

    def move_venoms(self):
        """Move all venoms downward"""
        for venom in self.poison:
            venom.forward(self.venom_speed)