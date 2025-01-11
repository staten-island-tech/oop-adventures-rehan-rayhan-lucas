import pygame

# Utility function for dialogue boxes
def draw_dialogue_box(screen, dialogue):
    pygame.draw.rect(screen, (0, 0, 0), (50, 400, 700, 100))  # Dark box for dialogue
    pygame.draw.rect(screen, (255, 255, 255), (50, 400, 700, 100), 3)  # White border
    font = pygame.font.Font(None, 36)
    text = font.render(dialogue, True, (255, 255, 255))
    screen.blit(text, (60, 430))  # Display text inside the box

# Function to switch between locations
def switch_location(current_location, new_location):
    print(f"Moving to {new_location.name}...")
    current_location = new_location
    return current_location

# Utility function to display text
def display_text(screen, text, x, y):
    font = pygame.font.Font(None, 36)
    rendered_text = font.render(text, True, (255, 255, 255))
    screen.blit(rendered_text, (x, y))

# Class for utilities (items to buy and use)
class Utility:
    def __init__(self, name, description, cost):
        self.name = name
        self.description = description
        self.cost = cost

    def buy(self):
        print(f"Buying {self.name}: {self.description} for {self.cost}! This will help with your investigation.")

    def writesmth(self):
        return f"{self.name}: {self.description} (Cost: {self.cost})"

# Creating Utilities
<<<<<<< Updated upstream
glassermagnifyer = utility("Magnifying Glass", "To examine/find evidence. 25 percent chance of breaking", 5)
notebooker = utility("Notebook", "To write down notes.", 5)
cameraer = utility("Camera", "To keep memories! One time usage. Photos can be put into notebook.", 3)
mapper = utility("Map", "For recording the surroundings.", 1)
keyer = utility("Key", "To unlock locked doors (duh).", 10)
packerbacker = utility("Backpack", "To increase your inventory space.", 25)
kitterfingerprinter = utility("Fingerprinting Kit", "To identify fingerprints.", 15)

packerbacker = utility("Backpack", "To increase your inventory space.", 20)
kitterfingerprinter = utility("Fingerprinting Kit", "To identify fingerprints.", 10)
=======
glassermagnifyer = Utility("Magnifying Glass", "To examine/find evidence. 25 percent chance of breaking", 5)
notebooker = Utility("Notebook", "To write down notes.", 5)
lockerpicker = Utility("Lockpick", "To open locked doors or compartments. Has a 25 percent of breaking.", 3)
lighterflasher = Utility("Flashlight", "You light up my world! A light source.", 20)
cameraer = Utility("Camera", "To keep memories! One time usage. Photos can be put into notebook.", 3)
kitterdisguiser = Utility("Disguising Kit", "For camouflage purposes.", 15)
mapper = Utility("Map", "For recording the surroundings.", 1)
keyer = Utility("Key", "To unlock locked doors (duh).", 10)
packerbacker = Utility("Backpack", "To increase your inventory space.", 25)
kitterfingerprinter = Utility("Fingerprinting Kit", "To identify fingerprints.", 15)

# List of utilities
>>>>>>> Stashed changes
utilities = [
    glassermagnifyer,
    notebooker,
    cameraer,
    mapper,
    keyer,
    packerbacker,
    kitterfingerprinter
]

# Print descriptions of all utilities
for utility in utilities:
    print(utility.writesmth())

# Function to display available utilities (items) at the market
def display_market_items(screen, utilities):
    font = pygame.font.SysFont(None, 30)
    y_offset = 100  # Starting Y position for the list

    # Display title for the items list
    title_text = font.render("Items Available at the Market", True, (0, 0, 0))
    screen.blit(title_text, (20, y_offset))
    y_offset += 40  # Move down after title

    # Loop through utilities and display each one
    for utility in utilities:
        item_text = font.render(f"- {utility.name}: {utility.description} (Cost: ${utility.cost})", True, (0, 0, 0))
        screen.blit(item_text, (20, y_offset))
        y_offset += 30  # Move down for the next item

