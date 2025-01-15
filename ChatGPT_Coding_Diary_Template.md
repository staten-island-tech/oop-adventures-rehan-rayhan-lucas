# ChatGPT Coding Diary
## Project Name: OOP Adevntures
### Date: 1/14/25
---
## 1. **Task/Problem Description**
What functions can I make to allow the player to explore a specific location to get clues?
---
## 2. **Initial Approach/Code**
```python
    def __init__(self, name, clues):
        self.name = name
        self.clues = clues

class LocationManager:
    def __init__(self):
        self.locations = [
            Location("Study", ["A blood-stained handkerchief"]),
            Location("Hallway", ["A torn piece of fabric"]),
            Location("Victim's Room", ["A letter about the will"]),
        ]
    
    def get_locations(self):
        return self.locations
```
My plan was to create a function where the player explores a chosen location to get clues, and that if it doesn't work, it will return that it doesn't work.
---
## 3. **Interaction with ChatGPT**
### Questions/Requests to ChatGPT
From this code (insert my code here), how can a function that allows the player to explore a location for clues be made?
## 4. **ChatGPT's Suggestions/Code Changes**
```python
    def explore_location(self, location_name):
        for location in self.locations:
            if location.name.lower() == location_name.lower():
                return f"Exploring {location.name}. Clues found: {', '.join(location.clues)}"
        return "Location not found."
```
I had the right idea, I just couldn't put my thoughts into code.
---
## 5. **Reflection on Changes**
After putting in the `explore_location` function, I realized that the logic was straightforward and required careful handling of letter capitalization when comparing location names. The use of `lower()` made sure that the comparison is case-insensitive, which is important for user input flexibility.
---
## 6. **Testing and Results**
After making the changes, I tested the `explore_location` function with various inputs to ensure it worked correctly.
- **Tests Conducted**:
Tested with exact location names (e.g., "Study").
Tested with different cases (e.g., "study", "STUDY").
Tested with invalid location names (e.g., "Kitchen").
- **Results**:
The function returned the correct clues for valid locations.
The function correctly handled case-insensitive inputs.
The function returned "Location not found." for invalid locations.
```python
print(location_manager.explore_location("Study"))  # expected output: exploring Study. clues found: a blood-stained handkerchief
print(location_manager.explore_location("study"))  # expected output: exploring Study. clues found: a blood-stained handkerchief
print(location_manager.explore_location("Kitchen"))  # expected output: location not found.
```
# ChatGPT Coding Diary
## Project Name: OOP Adevntures
### Date: 1/13/25
---
## 1. **Task/Problem Description**
What can I do to allow the user to check for each item in their inventory?
---
## 2. **Initial Approach/Code**
```python
class Inventory:
    def __init__(self):
        self.items = []
        self.coins = 10  #the player starts with 10 coins by default

    def add_item(self, item):
        if item not in self.items:
            self.items.append(item)
            return f"{item} has been added to your inventory."
        return f"{item} is already in your inventory."

    def view_inventory(self):
        if not self.items:
            return f"Your inventory is empty. You have {self.coins} coins."
        return f"Your inventory contains: {self.items} You have {self.coins} coins."
```
My plan was to create a for loop or to create true or false functions, but I knew there was way easier and shorter ways to do this.
---
## 3. **Interaction with ChatGPT**
### Questions/Requests to ChatGPT
From this code (insert my code here), how can a function that allows the player to check for their inventory for existing items?
## 4. **ChatGPT's Suggestions/Code Changes**
```python
        return f"Your inventory contains:\n" + "\n".join(self.items) + f"\n\nYou have {self.coins} coins."
```
This was not what I had expected. what is a .join, and what does it do?
---
## 5. **Reflection on Changes**
After implementing the suggested change using `join`, I realized that it simplifies the process of formatting the inventory list. The `join` method is very useful for combining list elements into a single string with a specified separator, making the output more readable.
---
## 6. **Testing and Results**
- **Tests Conducted**:
Tested with an empty inventory.
Tested with a single item in the inventory.
Tested with multiple items in the inventory.
- **Results**:
When the inventory is empty, it correctly displays "Your inventory is empty. You have 10 coins."
When the inventory has one item, it correctly displays the item and the number of coins.
When the inventory has multiple items, it correctly lists all items, each on a new line, and the number of coins.
```python
# Example: Testing the view_inventory function
inventory = Inventory()
# Test with empty inventory
print(inventory.view_inventory())  # Expected output: Your inventory is empty. You have 10 coins.
# Test with one item
inventory.add_item("Sword")
print(inventory.view_inventory())  # Expected output: Your inventory contains: Sword\nYou have 10 coins.
# Test with multiple items
inventory.add_item("Shield")
inventory.add_item("Potion")
print(inventory.view_inventory())  # Expected output: Your inventory contains:\nSword\nShield\nPotion\nYou have 10 coins.
```
# ChatGPT Coding Diary
## Project Name: OOP Adevntures
### Date: 1/13/25
---
## 1. **Task/Problem Description**
chatgpt im really lazy so make me questions please
---
## 2. **Initial Approach/Code**
```python
class Puzzle:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def solve(self, answer):
        if answer.lower() == self.answer.lower():
            return "Correct! You've solved the puzzle."
        else:
            return "Incorrect. Try again."


class PuzzleManager:
    def __init__(self):
        self.puzzles = [
            Puzzle("Who is the greatest and most glorious computer science teacher in all of existence?", "Mr. Whalen"),
            Puzzle("Who is giving us a 100 on this project?", "Mr. Whalen"),
        ]
```
I knew that writing each question individually would take really long, so I just asked ChatGPT to generate questions for me to speed up the process.
---
## 3. **Interaction with ChatGPT**
### Questions/Requests to ChatGPT
From this code (insert my code here), make me some trivia questions.
## 4. **ChatGPT's Suggestions/Code Changes**
```python
class PuzzleManager:
    def __init__(self):
        self.puzzles = [
            Puzzle("Who is the greatest and most glorious computer science teacher in all of existence?", "Mr. Whalen"),
            Puzzle("Who is giving us a 100 on this project?", "Mr. Whalen"),
            Puzzle("What is the capital of France?", "Paris"),
            Puzzle("What is 28172 + 13213?", "41385"),
            Puzzle("What is the largest planet in our solar system?", "Jupiter"),
            Puzzle("Who wrote 'To Kill a Mockingbird'?", "Harper Lee"),
            Puzzle("What is the boiling point of water?", "100°C"),
            Puzzle("Who painted the Mona Lisa?", "Leonardo da Vinci"),
            Puzzle("What is the smallest prime number?", "2"),
            Puzzle("What is the chemical symbol for gold?", "Au"),
            Puzzle("Who is known as the father of computers?", "Charles Babbage"),
            Puzzle("What is the speed of light?", "299,792,458 m/s"),
            Puzzle("Who discovered penicillin?", "Alexander Fleming"),
            Puzzle("What is the tallest mountain in the world?", "Mount Everest"),
            Puzzle("What is the hardest natural substance on Earth?", "Diamond"),
            Puzzle("Who wrote '1984'?", "George Orwell"),
            Puzzle("What is the largest ocean on Earth?", "Pacific Ocean"),
            Puzzle("What is the main ingredient in guacamole?", "Avocado"),
            Puzzle("Who developed the theory of relativity?", "Albert Einstein"),
            Puzzle("What is the currency of Japan?", "Yen"),
            Puzzle("What is the capital of Italy?", "Rome"),
            Puzzle("What is the square root of 64?", "8"),
            Puzzle("Who was the first president of the United States?", "George Washington"),
            Puzzle("What is the chemical symbol for water?", "H2O"),
            Puzzle("What is the largest mammal?", "Blue Whale"),
            Puzzle("Who wrote 'Pride and Prejudice'?", "Jane Austen"),
            Puzzle("What is the capital of Canada?", "Ottawa"),
            Puzzle("What is the smallest country in the world?", "Vatican City"),
            Puzzle("Who painted the Starry Night?", "Vincent van Gogh"),
            Puzzle("What is the capital of Australia?", "Canberra"),
            Puzzle("What is the chemical symbol for sodium?", "Na"),
            Puzzle("Who discovered gravity?", "Isaac Newton"),
            Puzzle("What is the largest desert in the world?", "Sahara Desert"),
            Puzzle("Who wrote 'The Great Gatsby'?", "F. Scott Fitzgerald"),
            Puzzle("What is the capital of Germany?", "Berlin"),
            Puzzle("What is the main gas found in the air we breathe?", "Nitrogen"),
            Puzzle("Who was the first man to walk on the moon?", "Neil Armstrong"),
            Puzzle("What is the capital of Russia?", "Moscow"),
            Puzzle("What is the largest bone in the human body?", "Femur"),
            Puzzle("Who wrote 'Moby-Dick'?", "Herman Melville"),
            Puzzle("What is 15 * 15?", "225"),
            Puzzle("What is the area of a circle with radius 7?", "153.94"),
            Puzzle("What is the perimeter of a rectangle with length 8 and width 5?", "26"),
            Puzzle("What is the volume of a cube with side length 4?", "64"),
            Puzzle("What is the Pythagorean theorem?", "a^2 + b^2 = c^2"),
            Puzzle("What is the sum of the angles in a triangle?", "180 degrees"),
            Puzzle("What is the derivative of x^2?", "2x"),
            Puzzle("What is the integral of 1/x?", "ln(x)"),
            Puzzle("What is the value of pi to 3 decimal places?", "3.142"),
            Puzzle("What is the circumference of a circle with diameter 10?", "31.42"),
            Puzzle("What is the area of a triangle with base 6 and height 3?", "9"),
            Puzzle("What is the slope of the line y = 2x + 3?", "2"),
            Puzzle("What is the quadratic formula?", "(-b ± √(b^2 - 4ac)) / 2a"),
            Puzzle("What is the distance formula?", "√((x2 - x1)^2 + (y2 - y1)^2)"),
            Puzzle("What is the midpoint formula?", "((x1 + x2) / 2, (y1 + y2) / 2)"),
            Puzzle("What is the volume of a sphere with radius 3?", "113.1"),
            Puzzle("What is the surface area of a cylinder with radius 3 and height 5?", "150.8"),
            Puzzle("What is the sum of the first 10 natural numbers?", "55"),
            Puzzle("What is the factorial of 5?", "120"),
            Puzzle("What is the value of the golden ratio?", "1.618")
        ]
```

