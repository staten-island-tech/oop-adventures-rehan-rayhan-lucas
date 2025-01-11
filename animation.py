import pygame

class Detective(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 100))  # Placeholder for character image
        self.image.fill((255, 255, 255))  # Color for testing
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.state = 'idle'  # Default state

    def animate(self):
        if self.state == 'idle':
            self.image.fill((255, 255, 255))  # Idle state appearance
        elif self.state == 'walking':
            self.image.fill((0, 255, 0))  # Walking state appearance (Green)
        elif self.state == 'talking':
            self.image.fill((0, 0, 255))  # Talking state appearance (Blue)
        else:
            self.image.fill((255, 255, 255))  # Default appearance

    def update(self):
        self.animate()  # Update the animation every frame

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Sheriff(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 100))  # Placeholder for sheriff image
        self.image.fill((255, 255, 255))  # Color for testing
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.state = 'idle'

    def animate(self):
        if self.state == 'idle':
            self.image.fill((255, 255, 255))  # Idle state appearance
        elif self.state == 'walking':
            self.image.fill((0, 0, 255))  # Walking state appearance (Blue)
        elif self.state == 'talking':
            self.image.fill((255, 0, 0))  # Talking state appearance (Red)
        else:
            self.image.fill((255, 255, 255))

    def update(self):
        self.animate()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
