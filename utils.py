# Utility functions
class utility:
    def __init__(self, name, description, cost):
        self.name = name
        self.description = description
        self.cost = cost
    def writesmth(self):
        return f"{self.name}: {self.description} (Cost: {self.cost})"
#Creating Utilities
glassermagnifyer = utility("Magnifying Glass", "To examine/find evidence. 25 percent chance of breaking", 5)
notebooker = utility("Notebook", "To write down notes.", 5)
lockerpicker = utility("Lockpick", "To open locked doors or compartments. Has a 25 percent of breaking.", 3)
cameraer = utility("Camera", "To keep memories! One time usage. Photos can be put into notebook.", 3)
mapper = utility("Map", "For recording the surroundings.", 1)
packerbacker = utility("Backpack", "To increase your inventory space.", 25)
kitterfingerprinter = utility("Fingerprinting Kit", "To identify fingerprints.", 15)
utilities = [
    glassermagnifyer,
    notebooker,
    lockerpicker,
    cameraer,
    mapper,
    packerbacker,
    kitterfingerprinter
]
for utility in utilities:
    print(utility.writesmth())




  