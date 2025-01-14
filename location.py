class Location:
    def __init__(self, name, clues):
        self.name = name
        self.clues = clues


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
#You also got the inventory.py: 
class Inventory:
    def __init__(self):
        self.items = []
        self.coins = 10  # Start with 10 coins by default

    def add_item(self, item):
        if item not in self.items:
            self.items.append(item)
            return f"{item} has been added to your inventory."
        return f"{item} is already in your inventory."

    def view_inventory(self):
        if not self.items:
            return f"Your inventory is empty. You have {self.coins} coins."
        return f"Your inventory contains:\n" + "\n".join(self.items) + f"\n\nYou have {self.coins} coins."

    def earn_coins(self, amount):
        self.coins += amount
        return f"You earned {amount} coins! You now have {self.coins} coins."

    def spend_coins(self, amount):
        if self.coins >= amount:
            self.coins -= amount
            return True
        return False

    def buy_clue(self, clue, cost):
        if self.spend_coins(cost):
            self.add_item(clue)
            return f"You purchased the clue: {clue} for {cost} coins."
        return f"You don’t have enough coins to buy this clue. It costs {cost} coins."
#And puzzles.py:
class Puzzle:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def solve(self, answer):
        if answer.lower() == self.answer.lower():
            return "Correct! You've solved the puzzle."
        else:
            return "Incorrect. Try again."


class PuzzleManager:
    def __init__(self):
        self.puzzles = [
            Puzzle("What is 2 + 2?", "4"),
            Puzzle("What color is the sky?", "blue"),
        ]



