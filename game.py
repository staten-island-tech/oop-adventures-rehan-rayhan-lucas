import pygame
from character import Detective, Sheriff, Suspect1, Suspect2, Suspect3
from location import switch_location, draw_dialogue_box
from mystery import solve_mystery
from utils import draw_dialogue_box, switch_location

# Set up Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))

# Initialize detective and sheriff
detective = Detective("Sherlock Holmes", 400, 250)
sheriff = Sheriff("Joe Smith")

# Define suspects
suspect1 = Suspect1()
suspect2 = Suspect2()
suspect3 = Suspect3()
suspects = [suspect1, suspect2, suspect3]

# Define money tracker
money_counter = 0

# Define font for text rendering
font = pygame.font.SysFont("Arial", 24)

# Define environment functions
def draw_first_floor(screen, font):
    global money_counter
    screen.fill((200, 200, 255))  # Light blue background
    first_floor_image = pygame.image.load("Images/First Floor.png")
    screen.blit(first_floor_image, (0, 0))  # Display first floor

    # Interactable box: Leave House
    leave_house_box = pygame.Rect(100, 400, 150, 50)  # Adjust these coordinates
    pygame.draw.rect(screen, (0, 0, 0), leave_house_box)
    text = font.render("Leave House", True, (255, 255, 255))
    screen.blit(text, (110, 410))  # Position of text

    # Interactable arrow: To Second Floor
    second_floor_arrow = pygame.Rect(600, 250, 50, 50)  # Adjust these coordinates
    pygame.draw.polygon(screen, (0, 0, 0), [(600, 250), (650, 230), (650, 270)])
    pygame.draw.rect(screen, (0, 0, 0), second_floor_arrow)
    text = font.render("To Second Floor", True, (255, 255, 255))
    screen.blit(text, (620, 270))  # Position of text

    # Money scattered around
    money_icon = pygame.image.load("Images/Money.png")
    money_rect = money_icon.get_rect()
    money_rect.topleft = (150, 150)  # Random position for money
    screen.blit(money_icon, money_rect)

    # Money collection (simple click detection for now)
    if money_rect.collidepoint(pygame.mouse.get_pos()):
        if pygame.mouse.get_pressed()[0]:  # Left click
            money_counter += 5  # Add $5 for money click

def draw_front_of_house(screen, font):
    screen.fill((255, 255, 200))  # Light yellow background
    front_of_house_image = pygame.image.load("Images/Front of House.png")
    screen.blit(front_of_house_image, (0, 0))  # Display front of house

    # Interactable box: Enter House
    enter_house_box = pygame.Rect(100, 400, 150, 50)
    pygame.draw.rect(screen, (0, 0, 0), enter_house_box)
    text = font.render("Enter House", True, (255, 255, 255))
    screen.blit(text, (110, 410))

    # Interactable arrow: To Front of Police Station
    police_station_arrow = pygame.Rect(600, 250, 50, 50)
    pygame.draw.polygon(screen, (0, 0, 0), [(600, 250), (650, 230), (650, 270)])
    pygame.draw.rect(screen, (0, 0, 0), police_station_arrow)
    text = font.render("To Front of Police Station", True, (255, 255, 255))
    screen.blit(text, (620, 270))

def draw_front_of_police_station(screen, font):
    screen.fill((200, 255, 255))  # Light green background
    front_of_police_station_image = pygame.image.load("Images/Front of Police Station.png")
    screen.blit(front_of_police_station_image, (0, 0))  # Display front of police station

    # Interactable arrow: To The House
    to_house_arrow = pygame.Rect(600, 250, 50, 50)
    pygame.draw.polygon(screen, (0, 0, 0), [(600, 250), (650, 230), (650, 270)])
    pygame.draw.rect(screen, (0, 0, 0), to_house_arrow)
    text = font.render("To The House", True, (255, 255, 255))
    screen.blit(text, (620, 270))

    # Interactable arrow: To The Market
    to_market_arrow = pygame.Rect(50, 250, 50, 50)
    pygame.draw.polygon(screen, (0, 0, 0), [(50, 250), (100, 230), (100, 270)])
    pygame.draw.rect(screen, (0, 0, 0), to_market_arrow)
    text = font.render("To The Market", True, (255, 255, 255))
    screen.blit(text, (70, 270))

    # Interactable box: Enter Police Station
    enter_police_station_box = pygame.Rect(100, 400, 150, 50)
    pygame.draw.rect(screen, (0, 0, 0), enter_police_station_box)
    text = font.render("Enter Police Station", True, (255, 255, 255))
    screen.blit(text, (110, 410))

def draw_interrogation_room(screen, font):
    global money_counter
    screen.fill((255, 0, 0))  # Red background
    interrogation_room_image = pygame.image.load("Images/Interrogation Room.png")
    screen.blit(interrogation_room_image, (0, 0))  # Display interrogation room

    # Money scattered around
    money_icon = pygame.image.load("Images/Money.png")
    money_rect = money_icon.get_rect()
    money_rect.topleft = (150, 150)  # Random position for money
    screen.blit(money_icon, money_rect)

    # Money collection (simple click detection for now)
    if money_rect.collidepoint(pygame.mouse.get_pos()):
        if pygame.mouse.get_pressed()[0]:  # Left click
            money_counter += 5  # Add $5 for money click

    # Suspects' statements
    suspect1_image = pygame.image.load("Images/Suspect 1.png")
    screen.blit(suspect1_image, (100, 100))
    text = font.render(suspect1.statement(), True, (255, 255, 255))
    screen.blit(text, (100, 180))

    suspect2_image = pygame.image.load("Images/Suspect 2.png")
    screen.blit(suspect2_image, (300, 100))
    text = font.render(suspect2.statement(), True, (255, 255, 255))
    screen.blit(text, (300, 180))

    suspect3_image = pygame.image.load("Images/Suspect 3.png")
    screen.blit(suspect3_image, (500, 100))
    text = font.render(suspect3.statement(), True, (255, 255, 255))
    screen.blit(text, (500, 180))

def draw_market(screen, font):
    screen.fill((255, 255, 255))  # White background
    market_image = pygame.image.load("Images/Market.png")
    screen.blit(market_image, (0, 0))  # Display market

    # Interactive items and their purchase options
    # Example: Notebook (5 bucks)
    notebook_rect = pygame.Rect(100, 150, 100, 50)
    pygame.draw.rect(screen, (0, 0, 0), notebook_rect)
    text = font.render("Buy Notebook - $5", True, (255, 255, 255))
    screen.blit(text, (110, 160))

def game_loop():
    global money_counter
    running = True
    current_location = 'First Floor'

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Draw current environment
        if current_location == 'First Floor':
            draw_first_floor(screen, font)
        elif current_location == 'Front of House':
            draw_front_of_house(screen, font)
        elif current_location == 'Front of Police Station':
            draw_front_of_police_station(screen, font)
        elif current_location == 'Interrogation Room':
            draw_interrogation_room(screen, font)
        elif current_location == 'Market':
            draw_market(screen, font)

        pygame.display.flip()  # Update the screen

game_loop()
