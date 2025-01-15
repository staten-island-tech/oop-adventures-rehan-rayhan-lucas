class Detective:
    def __init__(self, name, age, experience):
        self.name = name
        self.age = age
        self.experience = experience
        self.inventory = []
        # Add any other detective-specific attributes or methods

    def investigate(self):
        return f"{self.name} is investigating the crime scene."

    def add_to_inventory(self, item):
        if len(self.inventory) < 4:
            self.inventory.append(item)
        else:
            return "Inventory is full."

    def show_inventory(self):
        return f"{self.name}'s inventory: {', '.join(self.inventory) if self.inventory else 'Empty'}"

class Sheriff:
    def __init__(self, name, age, rank):
        self.name = name
        self.age = age
        self.rank = rank
        self.knowledge = "Has information about the market and game lore."

    def provide_info(self):
        return f"The sheriff provides information: {self.knowledge}"

class Suspect1:
    def __init__(self, name, age, alibi):
        self.name = name
        self.age = age
        self.alibi = alibi
        self.story = "I was at home during the crime."

    def tell_story(self):
        return f"{self.name}: {self.story}"

    def give_alibi(self):
        return f"{self.name}'s alibi: {self.alibi}"

class Suspect2:
    def __init__(self, name, age, alibi):
        self.name = name
        self.age = age
        self.alibi = alibi
        self.story = "I was at the store when the crime happened."

    def tell_story(self):
        return f"{self.name}: {self.story}"

    def give_alibi(self):
        return f"{self.name}'s alibi: {self.alibi}"

class Suspect3:
    def __init__(self, name, age, alibi):
        self.name = name
        self.age = age
        self.alibi = alibi
        self.story = "I was out of town during the incident."

    def tell_story(self):
        return f"{self.name}: {self.story}"

    def give_alibi(self):
        return f"{self.name}'s alibi: {self.alibi}"


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


 

