import pygame

# Define the Detective class
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

# Define the Sheriff class
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
            self.image.fill((255, 255, 255))  # Default appearance

    def update(self):
        self.animate()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

# Define the Suspect class
class Suspect(pygame.sprite.Sprite):
    def __init__(self, name, description, x, y, shirt_color, pants_color, hair_color, has_mustache=False):
        super().__init__()
        self.name = name
        self.description = description
        self.hair_color = hair_color
        self.shirt_color = shirt_color
        self.pants_color = pants_color
        self.has_mustache = has_mustache
        self.image = pygame.Surface((50, 100))  # Placeholder for suspect image
        self.image.fill((255, 255, 255))  # Color for testing
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.state = 'idle'

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
        self.animate()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

# Define each suspect with their details
suspect1 = Suspect("Suspect One", "Wears glasses, blue shirt, black pants", 100, 200, "blue", "black", "black")
suspect2 = Suspect("Suspect Two", "Has a mustache, red shirt, black pants", 200, 200, "red", "black", "brown", True)
suspect3 = Suspect("Suspect Three", "Has orange hair, red shirt, black pants", 300, 200, "red", "black", "orange")

# Adding them to a list to easily manage
suspects = [suspect1, suspect2, suspect3]
