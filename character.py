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


