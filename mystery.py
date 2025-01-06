# Mystery storyline and clues
class Detective:
    def __init__(self, name):
        self.name = name
        self.clues_found = []
        self.suspects_interviewed = []

    def interview_suspect(self, suspect):
        print(f"Interviewing {suspect.name}: {suspect.statement()}")
        self.suspects_interviewed.append(suspect)

    def solve_case(self):
        if len(self.clues_found) > 0 and len(self.suspects_interviewed) > 0:
            print(f"\n{self.name} is analyzing the case based on the clues and suspects.")
            for clue in self.clues_found:
                print(clue)

            for suspect in self.suspects_interviewed:
                print(suspect.reveal_motive())
                if suspect.is_guilty:
                    print(f"Detective {self.name} concludes that {suspect.name} is the murderer!")
                    return suspect
            print(f"{self.name} could not definitively find the murderer based on the evidence.")
        else:
            print(f"{self.name} needs more clues or interviews to solve the case.")
        return None

    def receive_case(self, victim, suspects):
        print(f"\nDetective {self.name} has received the case of {victim.name}.")
        for suspect in suspects:
            self.interview_suspect(suspect)
        print("\nCase investigation is complete.")
        
    def investigate(self, clue):
        print(f"Investigating clue: {clue}")
        self.clues_found.append(clue)


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


victim = Suspect("John Doe", "No alibi", "victim")
suspect1 = Suspect("Alice Smith", "Was at home alone", "ex-girlfriend", "Jealousy over an affair", False)
suspect2 = Suspect("Bob Johnson", "Was working late", "business partner", "Financial gain - inheritance", True)
suspect3 = Suspect("Charlie Brown", "Was at the gym", "friend", "Revenge for being fired", False)

clue1 = Clue("Bloodied knife", "Near the victim's body")
clue2 = Clue("Suspicious phone call made to the victim", "Victim's phone records")
clue3 = Clue("A torn piece of clothing matching Alice's style", "Outside the house")

detective = Detective("Jane Doe")
sheriff = Sheriff("Joe Smith")

sheriff.introduce_case(detective, victim, [suspect1, suspect2, suspect3])

case = Case("John Doe's murder", detective)
case.add_clue(clue1)
case.add_clue(clue2)
case.add_clue(clue3)

case.add_suspect(suspect1)
case.add_suspect(suspect2)
case.add_suspect(suspect3)

case.begin_investigation()

