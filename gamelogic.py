from character import CharacterManager
from clues import ClueManager
from location import LocationManager
from inventory import Inventory
from secretss import SecretManager
from puzzles import PuzzleManager






class MysteryGame:
    def __init__(self):
        self.character_manager = CharacterManager()
        self.clue_manager = ClueManager()
        self.location_manager = LocationManager()
        self.secret_manager = SecretManager()
        self.puzzle_manager = PuzzleManager()
        self.inventory = Inventory()
        self.discovered_secrets = []


    def introduce_suspects(self):
        print("\nIntroducing the suspects:")
        for character in self.character_manager.get_characters():
            print(f"\n--- {character.name.capitalize()} ---")
            print(character.introduction())


    def investigate_clue(self):
        available_clues = self.clue_manager.get_clues()
        print("\nAvailable clues:")
        for i, clue in enumerate(available_clues):
            if clue.description not in self.inventory.items:
                print(f"{i + 1}. {clue.description} (Cost: {clue.cost} coins)")
        try:
            choice = int(input("Choose a clue to investigate (number): ").strip()) - 1
            if 0 <= choice < len(available_clues):
                clue = available_clues[choice]
                print(self.clue_manager.buy_clue(choice, self.inventory))
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input. Please enter a number.")


    def question_suspect(self):
        suspects = self.character_manager.get_characters()
        print("\nAvailable suspects:")
        for i, suspect in enumerate(suspects):
            print(f"{i + 1}. {suspect.name.capitalize()}")
        try:
            choice = int(input("Choose a suspect to question (number): ").strip()) - 1
            if 0 <= choice < len(suspects):
                suspect = suspects[choice]
                print(f"\n{suspect.question(self.inventory)}")
                clue_choice = input("Do you want to use a clue on this suspect? (yes/no): ").strip().lower()
                if clue_choice == "yes":
                    print(self.use_clue_on_suspect(suspect))
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input. Please enter a number.")


    def use_clue_on_suspect(self, suspect):
        print("\nYour inventory:")
        for i, item in enumerate(self.inventory.items):
            print(f"{i + 1}. {item}")
        try:
            choice = int(input("Choose a clue to use (number): ").strip()) - 1
            if 0 <= choice < len(self.inventory.items):
                clue_description = self.inventory.items[choice]
                return self.clue_manager.use_clue(clue_description, suspect, self.inventory)
            else:
                return "Invalid choice."
        except ValueError:
            return "Invalid input. Please enter a number."


    def explore_location(self):
        locations = self.location_manager.get_locations()
        print("\nAvailable locations:")
        for i, location in enumerate(locations):
            print(f"{i + 1}. {location.name.capitalize()}")
        try:
            choice = int(input("Choose a location to explore (number): ").strip()) - 1
            if 0 <= choice < len(locations):
                location = locations[choice]
                print(f"\n{self.location_manager.explore_location(location.name)}")
                for clue in location.clues:
                    if clue not in self.inventory.items:
                        print(self.inventory.add_item(clue))
                secret = self.secret_manager.reveal_secret(location.name)
                if secret and secret not in self.discovered_secrets:
                    self.discovered_secrets.append(secret)
                    print(f"Secret discovered: {secret}")
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input. Please enter a number.")


    def solve_puzzle(self):
        puzzles = self.puzzle_manager.puzzles
        print("\nAvailable puzzles:")
        for i, puzzle in enumerate(puzzles):
            print(f"{i + 1}. {puzzle.question}")
        try:
            choice = int(input("Choose a puzzle to solve (number): ").strip()) - 1
            if 0 <= choice < len(puzzles):
                puzzle = puzzles[choice]
                answer = input(f"\n{puzzle.question}\nYour answer: ").strip()
                if puzzle.solve(answer).startswith("Correct"):
                    print(puzzle.solve(answer))
                    print(self.inventory.earn_coins(5))  # Earn 5 coins for solving a puzzle
                else:
                    print("Incorrect. Try again.")
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input. Please enter a number.")


    def view_inventory(self):
        print("\n" + self.inventory.view_inventory())


    def solve_mystery(self):
        print("\nYou are solving the mystery!")
        solution = input("Who is the murderer? (Enter their name): ").strip().lower()
        if self.character_manager.check_solution(solution):
            print("\nCongratulations! You solved the case!")
            print("\n--- The Truth ---")
            print(self.character_manager.get_motive())
            return True
        else:
            print("\nThat’s incorrect. Keep investigating!")
            return False


    def play(self):
        print("Welcome to the Mystery Mansion!")
        print("There’s been a murder. You are the detective on the case.")
        print("The suspects are: the maid, the son, the butler, and the two cousins.")
        print("\nWould you like to meet the suspects first? (yes/no)")
        if input().strip().lower() == "yes":
            self.introduce_suspects()


        while True:
            print("\nWhat would you like to do?")
            print("1. Investigate a clue (buy clues with coins)")
            print("2. Solve a puzzle (earn coins)")
            print("3. Question a suspect")
            print("4. Explore a location")
            print("5. View inventory")
            print("6. Solve the mystery")
            print("7. Exit game")
            print(f"Your current coins: {self.inventory.coins}")


            choice = input("Enter your choice (1-7): ").strip()


            if choice == "1":
                self.investigate_clue()
            elif choice == "2":
                self.solve_puzzle()
            elif choice == "3":
                self.question_suspect()
            elif choice == "4":
                self.explore_location()
            elif choice == "5":
                self.view_inventory()
            elif choice == "6":
                if self.solve_mystery():
                    break
            elif choice == "7":
                print("Exiting the game. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    game = MysteryGame()
    game.play()



