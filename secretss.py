class SecretManager:
    def __init__(self):
        self.secrets = {
            "Study": "The study has a hidden compartment containing an old family heirloom.",
            "Hallway": "In the hallway, there’s a locked door that leads to the victim’s secret office.",
            "Victim's Room": "In the victim's room, a safe with a strange combination was discovered.",
        }

    def reveal_secret(self, location_name):
        return self.secrets.get(location_name, None) 


