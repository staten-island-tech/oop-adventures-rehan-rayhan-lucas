#Location Class
class Location:
    def __init__(self, name, clues):
        self.name = name
        self.clues = clues

#Locations
class LocationManager:
    def __init__(self):
        self.locations = [
            Location("Study", ["A blood-stained handkerchief"]),
            Location("Hallway", ["A torn piece of fabric"]),
            Location("Victim's Room", ["A letter about the will"]),
        ]
    
    def get_locations(self):
        return self.locations
    
    def explore_location(self, location_name):
        for location in self.locations:
            if location.name.lower() == location_name.lower():
                return f"Exploring {location.name}. Clues found: {', '.join(location.clues)}"
        return "Location not found." 
