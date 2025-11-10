import random
import time


def roll_dice():
    """Simulē kauliņu metienu un atgriež rezultātu (1 līdz 6)."""
    return random.randint(1, 6)


def roll_multiple_dice(n):
    """Veic n kauliņu metienus un atgriež visus rezultātus."""
    results = []
    for _ in range(n):
        result = roll_dice()
        results.append(result)
        print(f"Kauliņš metiens: {result}")
        time.sleep(1)
    return results


number_of_rolls = 5
print(f"Metam {number_of_rolls} kauliņus:")
results = roll_multiple_dice(number_of_rolls)
print("Visi metieni:", results)
