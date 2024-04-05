import math
import random
class PhysicsClass:
    def __init__(self, grid_spacing, particle_count, gravity_force, bounciness, fluid_force_distance, fluid_force, friction_value, particle_radius, x, y, random_placement=False):
        if random_placement:
            self.particles = []
            while len(self.particles) < particle_count:
                particle_x = random.randint(0, 1280)
                particle_y = random.randint(0, 720)
                self.particles.append({"velocity": [0.0, 0.0], "pos": [float(particle_x), float(particle_y)]})
        else:
            # Generate particles in a grid
            particle_grid_size = math.ceil(math.sqrt(particle_count))
            grid_y = 0
            self.particles = []
            while len(self.particles) < particle_count:
                grid_x = 0
                while grid_x < particle_grid_size and len(self.particles) < particle_count:
                    particle_x = (grid_x * grid_spacing - grid_spacing * (particle_grid_size / 2)) + 640 + particle_radius
                    particle_y = (grid_y * grid_spacing - grid_spacing * (particle_grid_size / 2)) + 360 + particle_radius
                    self.particles.append({"velocity": [0.0, 0.0], "pos": [float(particle_x), float(particle_y)]})
                    grid_x += 1
                grid_y += 1

        # Assign Variables
        self.gravityForce = gravity_force
        self.bounciness = bounciness
        self.particleRadius = particle_radius
        self.x = x
        self.y = y
        self.fluidForceDistance = fluid_force_distance
        self.fluidForce = fluid_force
        self.frictionValue = friction_value

    def gravity(self):
        # Increase velocity for all particles according to gravity
        for particle in self.particles:
            particle["velocity"][1] += self.gravityForce

    def velocity(self):
        # Move all particles according to their velocity
        for particle in self.particles:
            particle["pos"][0] += particle["velocity"][0]
            particle["pos"][1] += particle["velocity"][1]

    def bounce(self):
        # If particles go outside the bounds of the box make them teleport back and bounce
        for particle in self.particles:
            if particle["pos"][1] + self.particleRadius > self.y:
                particle["pos"][1] = self.y - self.particleRadius
                particle["velocity"][1] *= -1 * self.bounciness
            if particle["pos"][1] - self.particleRadius < 0:
                particle["pos"][1] = self.particleRadius
                particle["velocity"][1] *= -1 * self.bounciness
            if particle["pos"][0] + self.particleRadius > self.x:
                particle["pos"][0] = self.x - self.particleRadius
                particle["velocity"][0] *= -1 * self.bounciness
            if particle["pos"][0] - self.particleRadius < 0:
                particle["pos"][0] = self.particleRadius
                particle["velocity"][0] *= -1 * self.bounciness

    def fluid_physics(self):
        for particle1 in self.particles:
            for particle2 in self.particles:
                distance = math.dist(particle1["pos"], particle2["pos"])
                x = particle2["pos"][0] - particle1["pos"][0]
                y = particle2["pos"][1] - particle1["pos"][1]
                if y == 0:
                    if x > 0:
                        direction = math.radians(90)
                    else:
                        direction = math.radians(270)
                else:
                    direction = math.atan(x/y)

                if distance != 0:
                    # noinspection PyTypeChecker
                    force = max(0, self.fluidForceDistance-abs(distance))
                    force = force * force * force
                else:
                    force = 0.5
                force *= self.fluidForce

                force_x = math.sin(direction)*force
                force_y = math.cos(direction)*force
                particle2["velocity"][0] += force_x
                particle2["velocity"][1] += force_y

    def friction(self):
        for particle in self.particles:
            if particle["velocity"][0] > 0:
                particle["velocity"][0] -= self.frictionValue
            elif particle["velocity"][0] < 0:
                particle["velocity"][0] += self.frictionValue
            if particle["velocity"][1] > 0:
                particle["velocity"][1] -= self.frictionValue
            elif particle["velocity"][1] < 0:
                particle["velocity"][1] += self.frictionValue
