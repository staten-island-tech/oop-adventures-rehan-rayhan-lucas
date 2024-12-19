# Mystery storyline and clues
class Detective:
    def __init__(self, name):
        self.name = name
        self.clues_found = []
        self.suspects_interviewed = []

    def investigate(self, clue):
        self.clues_found.append(clue)
        print(f"Clue found: {clue.description}")

    def interview_suspect(self, suspect):
        self.suspects_interviewed.append(suspect.name)
        print(f"Interviewing {suspect.name}: {suspect.statement()}")

    def solve_case(self):
        if len(self.clues_found) > 0 and len(self.suspects_interviewed) > 0:
            print(f"{self.name} is analyzing the case based on the clues and suspects.")
        else:
            print("The detective needs more clues or interviews.")
class Clue:
    def __init__(self, description, location):
        self.description = description
        self.location = location

    def __str__(self):
        return f"Clue: {self.description} found at {self.location}"
class Suspect:
    def __init__(self, name, alibi, relationship_to_victim):
        self.name = name
        self.alibi = alibi
        self.relationship_to_victim = relationship_to_victim



