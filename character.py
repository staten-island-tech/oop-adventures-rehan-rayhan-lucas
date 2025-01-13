import pygame

class Detective:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.state = 'idle'
        self.inventory = [None, None, None, None]  # Inventory with 4 spaces
        self.money = 0  # Starting money

    def update(self):
        # Update detective position, state, etc.
        pass

    def draw(self, screen):
        # Load and draw the detective's image (First-Person POV, no detective image)
        pass

    def add_to_inventory(self, item):
        for i in range(4):
            if self.inventory[i] is None:
                self.inventory[i] = item
                return True
        return False  # No space in inventory

    def remove_from_inventory(self, index):
        if 0 <= index < 4:
            self.inventory[index] = None
            return True
        return False

    def add_money(self, amount):
        self.money += amount

    def show_inventory(self):
        print(f"Inventory: {self.inventory}")

    def show_money(self):
        return f"Money: ${self.money}"

class Sheriff:
    def __init__(self, name):
        self.name = name
        self.image = pygame.image.load('Images/Sheriff.png')  # Sheriff's image

    def introduce_case(self, detective, victim, suspects):
        print(f"\nSheriff {self.name}: Detective {detective.name}, we have a murder case.")
        print(f"Victim: {victim.name}, the crime happened last night.")
        print("The suspects are:")
        for suspect in suspects:
            print(f"- {suspect.name}, {suspect.relationship_to_victim}")
        
        print("The weapon used was a knife, and we need your help to solve it.")
        detective.receive_case(victim, suspects)

class Suspect:
    def __init__(self, name, alibi, relationship_to_victim, motive, image_path):
        self.name = name
        self.alibi = alibi
        self.relationship_to_victim = relationship_to_victim
        self.motive = motive
        self.image = pygame.image.load(image_path)

    def statement(self):
        return f"My alibi is: {self.alibi}"

    def reveal_motive(self):
        return f"Possible motive: {self.motive}"

class Suspect1(Suspect):
    def __init__(self):
        super().__init__("Alice Smith", "Was at home alone", "Ex-girlfriend", "Jealousy over an affair", "Images/Suspect 1.png")

class Suspect2(Suspect):
    def __init__(self):
        super().__init__("William Moriarty", "Was working late", "Business partner", "Financial gain - inheritance", "Images/Suspect 2.png")

class Suspect3(Suspect):
    def __init__(self):
        super().__init__("Charlie Brown", "Was at the gym", "Friend", "Revenge for being fired", "Images/Suspect 3.png")
