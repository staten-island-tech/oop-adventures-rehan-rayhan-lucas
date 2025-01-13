import pygame
def switch_location(current_location, new_location):
    current_location = new_location
    return current_location

def draw_dialogue_box(screen, text, font, x, y):
    box = pygame.Rect(x, y, 600, 50)
    pygame.draw.rect(screen, (0, 0, 0), box)
    rendered_text = font.render(text, True, (255, 255, 255))
    screen.blit(rendered_text, (x + 10, y + 10))



