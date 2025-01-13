import pygame

def draw_money_counter(screen, font, money_counter):
    text = font.render(f"Money: ${money_counter}", True, (255, 255, 255))
    screen.blit(text, (650, 10))  # Top right of the screen

def update_money_counter(money_counter, amount):
    return money_counter + amount

def draw_dialogue_box(screen, text, font, x, y):
    box = pygame.Rect(x, y, 600, 50)
    pygame.draw.rect(screen, (0, 0, 0), box)
    rendered_text = font.render(text, True, (255, 255, 255))
    screen.blit(rendered_text, (x + 10, y + 10))

def switch_location(current_location, new_location):
    return new_location








  