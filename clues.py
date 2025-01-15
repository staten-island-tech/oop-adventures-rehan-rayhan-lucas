class Clue:
    def __init__(self, description, cost):
        self.description = description
        self.cost = cost


class ClueManager:
    def __init__(self):
        self.clues = [
            Clue("A blood-stained handkerchief found in the study.", 5),
            Clue("A torn piece of fabric found in the hallway.", 3),
            Clue("A letter in the victim’s desk about changing the will.", 8),
        ]

    def get_clues(self):
        return self.clues

    def buy_clue(self, index, inventory):
        if 0 <= index < len(self.clues):
            clue = self.clues[index]
            if clue.description not in inventory.items:
                return inventory.buy_clue(clue.description, clue.cost)
            else:
                return "You already own this clue."
        return "Invalid clue selection."
