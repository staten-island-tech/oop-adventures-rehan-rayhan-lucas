# Mystery storyline and clues
class Character:
    def __init__(self, name, role, alibi, description):
        self.name = name
        self.role = role  
        self.alibi = alibi
        self.description = description
        self.is_suspect = False
        self.clues = []

    def set_suspect_status(self, status):
        self.is_suspect = status
        
    def add_clue(self, clue):
        self.clues.append(clue)

    def __str__(self):
        return f"{self.name} ({self.role})"
