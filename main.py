from render import RenderClass
from physics import PhysicsClass
import pygame

# Assigning variables
frameRate = 60
blur = 0
running = True

# Initialize classes
render = RenderClass(1280, 720, (0, 0, 0))
physics = PhysicsClass(
    30,
    100,
    0.0,
    0.5,
    100,
    0.000001,
    0.1,
    10,
    render.x,
    render.y,
    True)
clock = pygame.time.Clock()

# Simulation Loop
while running:
    # Quit when X button pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Generate dot position list for drawing
    dots = []
    for particle in physics.particles:
        dots.append(particle["pos"])

    # Apply Physics
    physics.gravity()
    physics.velocity()
    physics.bounce()
    physics.friction()
    physics.fluid_physics()

    # Render
    render.draw_dots((0, 128, 255), dots, physics.particleRadius)
    render.blur(blur)
    render.update()

    clock.tick(frameRate)  # Limit frame rate
