# Utility functions
class utility:
    def __init__(self, name, description, cost):
        self.name = name
        self.description = description
        self.cost = cost

    def buy(self):
        print(f"Buying {self.name}: {self.description} for {self.cost}!")

    def writesmth(self):
        return f"{self.name}: {self.description} (Cost: {self.cost})"

glassermagnifyer = utility("Magnifying Glass", "idk", 1)
notebooker = utility("Notebook", "idk", 1)
lockerpicker = utility("Lockpick", "idk", 1)
lighterflasher = utility("Flashlight", "idk", 1)
cameraer = utility("Camera", "idk", 1)
kitterdisguiser = utility("Disguising Kit", "idk", 1)
mapper = utility("Map", "idk", 1)
keyer = utility("Key", "idk", 1)
packerbacker = utility("Backpack", "idk", 1)
kitterfingerprinter = utility("Fingerprinting Kit", "idk", 1)

utilities = [
    glassermagnifyer,
    notebooker,
    lockerpicker,
    lighterflasher,
    cameraer,
    kitterdisguiser,
    mapper,
    keyer,
    packerbacker,
    kitterfingerprinter
]
for utility in utilities:
    print(utility.writesmth())





  