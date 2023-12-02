import pgzrun, random
from pgzhelper import *


# TODO: Replace the rectangles with Actor(image)
# TODO: Adds collision detection between the bird and the pipes
# TODO: Add a game over screen
# TODO: Add a background image
# TODO: Add a score counter
# TODO: Add sound effects


# Game constants
WIDTH = 700
HEIGHT = 500           
GRAVITY = 0.6
PIPE_WIDTH = 50
PIPE_GAP = 300      # The vertical gap between the top and bottom pipes
PIPE_SPACING = 200  # The horizontal space between each pipe

bird = Actor('birds/flp_bird2')
#bird = Rect((50, 250), (30, 30))
bird_speed = 0
bird.die = False
bird.score = 0


# The pipes are stored in two lists
top_pipes = []
bottom_pipes = []


def draw():
    screen.fill((0, 128, 255))  # Sky blue

    #screen.draw.filled_rect(bird, (255, 255, 0))
    
    bird.draw()

    for pipe in top_pipes:
        pipe.draw()

    for pipe in bottom_pipes:
        pipe.draw()


        screen.draw.text(f'Points: {bird.score}',(0,0), fontsize=30)

    if bird.die:
        screen.draw.text('< dead',(90, bird.y-80), fontsize=200, color='red')


def update():
    global bird_speed, pipes

    if bird.die: return

    # Apply gravity to the bird
    bird_speed += GRAVITY

    # Make the bird fall
    bird.y += bird_speed

    # Check for collision with the ground
    if bird.bottom > HEIGHT:
        # Put the bird back on the ground
        bird.bottom = HEIGHT

    # Check for collision with the ceiling
    if bird.top < 0:
        # Cap the bird at the ceiling
        bird.top = 0

    # Update top pipes and remove off-screen pipes
    for pipe in top_pipes:
        pipe.x -= 2
        if pipe.right < 0:
            top_pipes.remove(pipe)
            bird.score+=1
        else:
            if bird.collide_pixel(pipe):
                bird.die = True

    # Update bottom pipes and remove off-screen pipes
    for pipe in bottom_pipes:
        pipe.x -= 2
        if pipe.right < 0:
            bottom_pipes.remove(pipe)
        else:
            if bird.collide_pixel(pipe):
                bird.die = True

    # Generate new pipes
    has_pipe = len(top_pipes) > 0
    last_pipe = top_pipes[-1] if has_pipe else None
    last_pipe_far_enough = last_pipe.right < WIDTH - \
        PIPE_SPACING if has_pipe else True

    if not has_pipe or last_pipe_far_enough:
        MIN_HEIGHT = 50
        MAX_HEIGHT = HEIGHT - MIN_HEIGHT - PIPE_GAP
        pipe_height = random.randint(MIN_HEIGHT, MAX_HEIGHT)

        top_pipe = Rect((WIDTH, 0), (PIPE_WIDTH, pipe_height))
        top_pipe = Rect((WIDTH, pipe_height + PIPE_GAP),
                           (PIPE_WIDTH, HEIGHT - pipe_height - PIPE_GAP))
        
         
       
        top_pipe = Actor("environments/original/pipe1s")
        top_pipe.angle = 180
        top_pipe.pos = (WIDTH, 0)

        bottom_pipe = Actor("environments/original/pipe1s")
        bottom_pipe.pos=(WIDTH, pipe_height + PIPE_GAP)
        




        top_pipes.append(top_pipe)
        bottom_pipes.append(bottom_pipe)


def on_key_down(key):
    global bird_speed
    if key == keys.SPACE:
        bird_speed = -9


def on_mouse_down():
    global bird_speed
    bird_speed = -9



pgzrun.go()
