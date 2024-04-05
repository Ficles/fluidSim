import pygame
class RenderClass:
    def __init__(self, x_size, y_size, background_colour):
        pygame.init()
        self.x = x_size
        self.y = y_size
        self.screen = pygame.display.set_mode((self.x, self.y), pygame.SCALED)
        self.background = background_colour

    def update(self):
        pygame.display.flip()
        self.screen.fill(self.background)

    def draw_dots(self, colour, pos_list, radius):
        for pos in pos_list:
            pygame.draw.circle(self.screen, colour, pos, radius)

    def blur(self, blur_radius):
        if blur_radius > 0:
            self.screen.blit(pygame.transform.gaussian_blur(self.screen, blur_radius), (0, 0))
