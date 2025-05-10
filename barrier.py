from turtle import Turtle

class Barriers:
    def __init__(self):
        self.bunch = []
        self.create_barriers()
        
    def create_barriers(self):
        """Create defensive barriers"""
        # Create 4 barriers
        for barrier_num in range(4):
            x_start = -300 + barrier_num * 200
            
            # Create a small barrier structure
            for row in range(3):
                for col in range(5):
                    new_block = Turtle()
                    new_block.color("white")
                    new_block.shape("square")
                    new_block.shapesize(0.75, 0.75)
                    new_block.penup()
                    # Position the barrier blocks
                    x_pos = x_start + col * 20
                    y_pos = -150 + row * 20
                    new_block.goto(x_pos, y_pos)
                    self.bunch.append(new_block)