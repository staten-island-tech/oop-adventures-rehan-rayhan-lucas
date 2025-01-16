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

    def use_clue(self, clue_description, suspect, inventory):
        if clue_description not in inventory.items:
            return "You don’t own this clue yet."
        if clue_description == "A blood-stained handkerchief found in the study." and suspect.role == "maid":
            return "The handkerchief matches Lucy's cleaning supplies! It’s incriminating."
        elif clue_description == "A torn piece of fabric found in the hallway." and suspect.role == "butler":
            return "The fabric matches the butler’s uniform. Could he have been in the hallway?"
        elif clue_description == "A letter in the victim’s desk about changing the will." and suspect.role == "son":
            return "The letter reveals James's motive! He was angry about losing his inheritance."
        return "This clue doesn’t seem relevant to this suspect."