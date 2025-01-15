class Character:
    def __init__(self, name, role, alibi, motive=None):
        self.name = name
        self.role = role
        self.alibi = alibi
        self.motive = motive

    def introduction(self):
        return f"{self.name} is the {self.role}. {self.alibi}"

    def question(self):
        return f"{self.name} answers: 'I didn't do it! My alibi is solid!'"

    def get_motive(self):
        return self.motive if self.motive else "No known motive."


class CharacterManager:
    def __init__(self):
        self.characters = [
            Character("Lucy", "maid", "I was cleaning the kitchen all evening.", "She was fired recently and wanted revenge."),
            Character("James", "son", "I was in my room all night studying.", "He was angry about his inheritance."),
            Character("Reginald", "butler", "I was serving drinks in the study.", "He had a secret affair with the victim's spouse."),
            Character("Eleanor", "cousin", "I was at the bar down the road.", "She was jealous of the family fortune."),
            Character("Victor", "cousin", "I was with Eleanor the whole time.", "Victor has financial troubles and needed money.")
        ]
    
    def get_characters(self):
        return self.characters

    def check_solution(self, solution):
        return solution == "lucy"  # Lucy is the murderer
    
    def get_motive(self):
        return "Lucy had been fired recently and held a grudge. She planned to kill the victim for revenge."


 

