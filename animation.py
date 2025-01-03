#Animation-related functions 

import time
import sys
import random

class Animation:
    def __init__(self):
        pass

    # 1. Breathing Animation
    def breathing(self, character="@", cycles=3, speed=0.6):
        """Simulates a breathing animation where a character expands and contracts like breathing."""
        for _ in range(cycles):
            sys.stdout.write(f"{character}    ")  # Exhale (larger size)
            sys.stdout.flush()
            time.sleep(speed)
            sys.stdout.write("\r      ")  # Inhale (empty space)
            sys.stdout.flush()
            time.sleep(speed)
        print()  # Final newline after breathing cycle

    # 2. Kill Animation
    def kill_animation(self):
        """Simulate a kill with dramatic text and actions."""
        actions = [
            "The villain approaches...",
            "Suddenly, a swift movement...",
            "A knife flashes, and...",
            "The villain collapses with a final breath."
        ]
        for action in actions:
            self.typewriter_effect(action, speed=0.1)
            time.sleep(1)

    # 3. Typewriter Effect (for text animations)
    def typewriter_effect(self, text, speed=0.1):
        """Simulates a typewriter effect by printing each character with a delay."""
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(speed)
        print()

    # 4. Walking Animation
    def walking(self, character="~", steps=5, speed=0.2):
        """Simulate a walking animation with a character moving left to right."""
        for _ in range(steps):
            sys.stdout.write(f"{character}   ")
            sys.stdout.flush()
            time.sleep(speed)
            sys.stdout.write("\r     ")  # Clear previous character
            sys.stdout.flush()
            time.sleep(speed)
        print()  # End of walking animation

    # 5. Room Transition Animation
    def room_transition(self, old_room="Old Room", new_room="New Room", speed=1):
        """Simulate a room transition effect."""
        self.typewriter_effect(f"Leaving {old_room}...")
        time.sleep(speed)
        self.typewriter_effect(f"Entering {new_room}...")
        time.sleep(speed)
        sys.stdout.write("\r"*40)  # Clear screen effect
        sys.stdout.flush()

    # 6. Money Collection Animation
    def collect_money(self, amount):
        """Simulate the collection of money (e.g., +5, +10, +1, etc.)."""
        money_text = f"+{amount}"
        self.typewriter_effect(f"Collected {money_text}!", speed=0.3)
        time.sleep(0.5)

    # 7. Flashing Text Effect
    def flash_text(self, text, times=3, speed=0.5):
        """Flashes the text on and off a few times."""
        for _ in range(times):
            print(text, end="\r")
            time.sleep(speed)
            print(" " * len(text), end="\r")  # Clear the line
            time.sleep(speed)
        print(text)  # Final print to leave the text visible

    # Utility for pausing (e.g., when scene transition happens)
    def pause(self, duration=1):
        """Pause the game for a specified duration (in seconds)."""
        time.sleep(duration)
