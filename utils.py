# Utility functions
class utility:
    def __init__(self, name, description, cost):
        self.name = name
        self.description = description
        self.cost = cost
    def writesmth(self):
        return f"{self.name}: {self.description} (Cost: {self.cost})"
#Creating Utilities
glassermagnifyer = utility("Magnifying Glass", "To examine/find evidence.", 10)
notebooker = utility("Notebook", "To write down notes.", 5)
keyer = utility("Key", "To unlock locked doors (duh).", 10)
kitterfingerprinter = utility("Fingerprinting Kit", "To identify fingerprints.", 25)
utilities = [
    glassermagnifyer,
    notebooker,
    keyer,
    kitterfingerprinter
]
for utility in utilities:
    print(utility.writesmth())





  