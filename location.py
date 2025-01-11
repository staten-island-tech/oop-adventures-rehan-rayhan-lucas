<<<<<<< Updated upstream
 # Locations where the game takes place
#Suspect 3 people
# Detective
# Sheriff
# Sheriff's office
# Interrogation room with suspects
# Outside front of police station 2 roads to market one road to house
#Market for buying items
#Front of Home
#Inside First floor of home
#Inside Second floor of home
#Utilities
=======
import pygame

class Location:
    def __init__(self, name, description, drawing_func):
        self.name = name
        self.description = description
        self.drawing_func = drawing_func

    def display(self, screen):
        self.drawing_func(screen)  # Calls the location-specific drawing function

>>>>>>> Stashed changes
