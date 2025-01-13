def solve_mystery(detective, selected_suspect):
    if selected_suspect.name == "William Moriarty":
        print(f"\n{detective.name}: I've cracked the case. It's William Moriarty!")
        print("He was after the inheritance. Case closed.")
    else:
        print(f"\n{detective.name}: No, it’s not {selected_suspect.name}.")
        print("You lose! Try again.")




