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
            Puzzle("What is 2 + 2?", "4"),
            Puzzle("What color is the sky?", "blue"),
        ]

