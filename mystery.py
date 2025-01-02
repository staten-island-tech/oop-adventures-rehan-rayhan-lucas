# Mystery storyline and clues
class Detective:
    def __init__(self, name):
        self.name = name  # The detective's name

    def interview_suspect(self, suspect):
        print(f"Interviewing {suspect.name}: {suspect.statement()}")

    def solve_case(self, suspects):
        
        for suspect in suspects:
            print(f"Analyzing {suspect.name}:")
            if suspect.is_guilty:
                print(f"Detective {self.name} concludes that {suspect.name} is the murderer!")
                return suspect
            else:
                print(f"{suspect.name} has an alibi or no clear motive.")
        print(f"{self.name} could not find the murderer based on the evidence.")
        return None


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
    def __init__(self, name, alibi, relationship_to_victim, motive=None, is_guilty=False):
        self.name = name
        self.alibi = alibi
        self.relationship_to_victim = relationship_to_victim
        self.motive = motive
        self.is_guilty = is_guilty  

    def statement(self):
        
        return f"My alibi is: {self.alibi}"

    def __str__(self):
        return f"{self.name}, who has a {self.relationship_to_victim} relationship with the victim."

    def reveal_motive(self):
        if self.motive:
            return f"Possible motive: {self.motive}"
        return "No clear motive identified."
class Case:
    def __init__(self, victim_name, detective):
        self.victim_name = victim_name
        self.detective = detective
        self.clues = []
        self.suspects = []

    def add_clue(self, clue):
        self.clues.append(clue)
        self.detective.investigate(clue)

    def add_suspect(self, suspect):
        self.suspects.append(suspect)

    def begin_investigation(self):
        print(f"\n{self.detective.name} is investigating the case of {self.victim_name}.\n")
        for suspect in self.suspects:
            self.detective.interview_suspect(suspect)

        self.detective.solve_case()
class Sheriff:
    def __init__(self, name):
        self.name = name 
    
    def introduce_case(self, detective, victim, suspects):
        print(f"\nSheriff {self.name}: Detective {detective.name}, we have a murder case.")
        print(f"Victim: {victim.name}, the crime happened last night.")
        print("The suspects are:")
        for suspect in suspects:
            print(f"- {suspect.name}, {suspect.relationship_to_victim}")
        
        print("The weapon used was a knife, and we need your help to solve it.")
        detective.receive_case(victim, suspects)
