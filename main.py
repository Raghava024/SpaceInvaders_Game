import time
from turtle import Screen
from spaceship import Spaceship
from aliens import Aliens
from barrier import Barriers
from scorecard import Score

screen = Screen()
screen.setup(700, 700)
screen.bgcolor("black")
screen.title("Space Invaders")

# Enable animation buffering for smoother gameplay
screen.tracer(0)

barrier = Barriers()
scoreboard = Score()
spaceship = Spaceship()
aliens = Aliens()

screen.listen()
screen.onkey(spaceship.move_left, "a")
screen.onkey(spaceship.move_right, "d")
screen.onkey(spaceship.shoot, "c")

alien_move_direction = 1  # 1 for right, -1 for left
move_counter = 0
game_over = False

while not game_over:
    time.sleep(0.01)  # Control game speed
    screen.update()  # Update the screen
    
    # Move bullets from spaceship
    spaceship.move_bullets()
    
    # Move alien venoms
    aliens.move_venoms()
    
    # Move aliens sideways occasionally
    move_counter += 1
    if move_counter % 50 == 0:
        aliens.move_herd(alien_move_direction)
    
    # Change direction if aliens reach edge
    if move_counter % 200 == 0:
        alien_move_direction *= -1
    
    # Random alien shooting
    if move_counter % 30 == 0 and aliens.herd:  # Only shoot if aliens exist
        aliens.shoot()
    
    # Check collisions between spaceship bullets and aliens
    for bullet in spaceship.bullets[:]:  # Use a copy to avoid modification during iteration
        for alien in aliens.herd[:]:  # Use a copy to avoid modification during iteration
            if bullet.distance(alien) < 20:
                bullet.hideturtle()
                alien.hideturtle()
                if bullet in spaceship.bullets:
                    spaceship.bullets.remove(bullet)
                if alien in aliens.herd:
                    aliens.herd.remove(alien)
                scoreboard.increase_score()
                scoreboard.update_score()
    
    # Check collisions between alien venoms and spaceship
    for venom in aliens.poison[:]:
        if venom.distance(spaceship) < 20:
            game_over = True
            scoreboard.game_over()
    
    # Check collisions between alien venoms and barriers
    for venom in aliens.poison[:]:
        for barrier_block in barrier.bunch[:]:
            if venom.distance(barrier_block) < 15:
                venom.hideturtle()
                barrier_block.hideturtle()
                if venom in aliens.poison:
                    aliens.poison.remove(venom)
                if barrier_block in barrier.bunch:
                    barrier.bunch.remove(barrier_block)
    
    # Check collision between bullets and barriers
    for bullet in spaceship.bullets[:]:
        for barrier_block in barrier.bunch[:]:
            if bullet.distance(barrier_block) < 15:
                bullet.hideturtle()
                barrier_block.hideturtle()
                if bullet in spaceship.bullets:
                    spaceship.bullets.remove(bullet)
                if barrier_block in barrier.bunch:
                    barrier.bunch.remove(barrier_block)
    
    # Check if all aliens are destroyed
    if not aliens.herd:
        aliens.create_aliens()  # Create new wave of aliens
        scoreboard.level_up()
    
    # Check if spaceship is hit or if aliens reach bottom
    for alien in aliens.herd:
        if alien.ycor() < -100 or alien.distance(spaceship) < 20:
            game_over = True
            scoreboard.game_over()
    
    # Check if bullets are out of bounds
    for bullet in spaceship.bullets[:]:
        if bullet.ycor() > 350:
            bullet.hideturtle()
            spaceship.bullets.remove(bullet)
    
    # Check if venoms are out of bounds
    for venom in aliens.poison[:]:
        if venom.ycor() < -350:
            venom.hideturtle()
            aliens.poison.remove(venom)

screen.exitonclick()