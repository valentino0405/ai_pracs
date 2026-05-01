status = ["", ""]

status[0] = input("Enter status of Location A (Dirty/Clean): ")
status[1] = input("Enter status of Location B (Dirty/Clean): ")

currentPos = input("Enter initial position of Vacuum (A/B): ")

totalCost = 0

COST_MOVE = 1
COST_CLEAN = 10

print("\nStarting Vacuum Cleaner Reflex Agent Simulation")

while True:
    posIndex = 0 if currentPos == "A" else 1
    otherIndex = 1 if posIndex == 0 else 0
    otherLocationName = "A" if otherIndex == 0 else "B"

    print("\n--- Current State ---")
    print(f"Location: {currentPos} | Status: {status[posIndex]}")
    print(f"Overall Status: A ({status[0]}), B ({status[1]})")
    print(f"Current Total Cost: {totalCost}")

    if status[posIndex] == "Dirty":
        print(f"Action: SUCK (Cost: {COST_CLEAN})")
        status[posIndex] = "Clean"
        totalCost += COST_CLEAN

    elif status[0] == "Clean" and status[1] == "Clean":
        print("Goal Reached: Both locations are clean. Action: EXIT.")
        break

    else:
        print(f"Action: MOVE to {otherLocationName} (Cost: {COST_MOVE})")
        currentPos = otherLocationName
        totalCost += COST_MOVE

print("\nSimulation complete.")
print(f"Final Total Cost of operations: {totalCost}")

"""
INPUT
Enter status of Location A (Dirty/Clean): Dirty
Enter status of Location B (Dirty/Clean): Dirty
Enter initial position of Vacuum (A/B): A

OUTPUT
Starting Vacuum Cleaner Reflex Agent Simulation

--- Current State ---
Location: A | Status: Dirty
Overall Status: A (Dirty), B (Dirty)
Current Total Cost: 0
Action: SUCK (Cost: 10)

--- Current State ---
Location: A | Status: Clean
Overall Status: A (Clean), B (Dirty)
Current Total Cost: 10
Action: MOVE to B (Cost: 1)

--- Current State ---
Location: B | Status: Dirty
Overall Status: A (Clean), B (Dirty)
Current Total Cost: 11
Action: SUCK (Cost: 10)

--- Current State ---
Location: B | Status: Clean
Overall Status: A (Clean), B (Clean)
Current Total Cost: 21
Goal Reached: Both locations are clean. Action: EXIT.

Simulation complete.
Final Total Cost of operations: 21
"""