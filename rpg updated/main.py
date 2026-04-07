import sys
import time
from models.character import Character
from models.generator import RandomGenerator
from engine.analyzer import StatisticalAnalyzer
from engine.visualizer import DataVisualization

characters = []

def print_slow(text):
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.01)
    print()

def main_menu():
    gen = RandomGenerator()
    while True:
        print("\n=== RPG CHARACTER MANAGER ===")
        print("[1] Create Random Character (Faker)")
        print("[2] View Character Radar (Matplotlib)")
        print("[3] Statistical Analysis (Pandas)")
        print("[4] Export Database (CSV)")
        print("[Q] Quit")
        
        choice = input("Choice: ").upper()
        
        if choice == "1":
            new_char = gen.generate_random_character()
            characters.append(new_char)
            print_slow(f"Created: {new_char.name} ({new_char.race} {new_char.char_class})")
            print(f"Backstory: {new_char.backstory}")
            
        elif choice == "2":
            if not characters: print("No characters yet!")
            else:
                for i, c in enumerate(characters): print(f"{i}: {c.name}")
                idx = int(input("Select Index: "))
                DataVisualization.plot_radar(characters[idx])
                
        elif choice == "3":
            analyzer = StatisticalAnalyzer(characters)
            print("\n--- Roster Stats ---")
            print(analyzer.get_summary())
            
        elif choice == "4":
            analyzer = StatisticalAnalyzer(characters)
            if analyzer.save_to_csv():
                print("Data exported to data/characters.csv")
                
        elif choice == "Q":
            break

if __name__ == "__main__":
    main_menu()
