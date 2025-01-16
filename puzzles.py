#Puzzle Class
class Puzzle:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def solve(self, answer):
        if answer.lower() == self.answer.lower():
            return "Correct! You've solved the puzzle."
        else:
            return "Incorrect. Try again."

#Puzzles
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