# A* Algorithm for 8 Puzzle

# Global goal state
goal = [[0]*3 for _ in range(3)]

# To store visited states (avoid loops)
visited = []

# Convert 2D state to string (for easy comparison in visited)
def state_to_string(state):
    return ''.join(str(state[i][j]) for i in range(3) for j in range(3))


# Heuristic function h(n)
# Counts number of misplaced tiles (excluding blank 0)
def calculate_h(state):
    h = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal[i][j]:
                h += 1
    return h


# Print puzzle state nicely
def print_state(state):
    for row in state:
        print(*row)


# Deep copy of state (important for creating new states)
def copy_state(state):
    return [row[:] for row in state]


# Check if current state == goal state
def is_goal(state):
    return state == goal


# ----------- MAIN PROGRAM -----------

# Input
print("Note: For Blank Tile Enter 0")
print("Enter Initial State (3x3):")

current = []
for i in range(3):
    row = list(map(int, input().split()))
    current.append(row)

print("Enter Goal State (3x3):")
for i in range(3):
    goal[i] = list(map(int, input().split()))

g = 0  # Cost so far

# A* Loop
while not is_goal(current):
    
    visited.append(state_to_string(current))

    print(f"\nCurrent State (g={g}):")
    print_state(current)

    # Find blank tile position
    blank_row, blank_col = 0, 0
    for i in range(3):
        for j in range(3):
            if current[i][j] == 0:
                blank_row, blank_col = i, j

    min_f = float('inf')
    min_h = float('inf')
    best_state = None
    chosen_move = ""

    moves = ["Up", "Down", "Left", "Right"]

    for move in moves:
        new_row, new_col = blank_row, blank_col

        # Define movement
        if move == "Up":
            new_row -= 1
        elif move == "Down":
            new_row += 1
        elif move == "Left":
            new_col -= 1
        elif move == "Right":
            new_col += 1

        # Check valid move
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            temp = copy_state(current)

            # Swap blank with adjacent tile
            temp[blank_row][blank_col], temp[new_row][new_col] = temp[new_row][new_col], temp[blank_row][blank_col]

            # Avoid revisiting states
            if state_to_string(temp) not in visited:
                h = calculate_h(temp)
                new_g = g + 1
                f = new_g + h

                print(f"Move: {move} -> g(n)={new_g} h(n)={h} f(n)={f}")

                # Choose best state (lowest f, then lowest h)
                if f < min_f or (f == min_f and h < min_h):
                    min_f = f
                    min_h = h
                    best_state = temp
                    chosen_move = move

    # If no moves possible
    if best_state is None:
        print("\nStuck! No valid unvisited moves available.")
        break

    print(f"\nChosen Move: {chosen_move} with f(n) = {min_f} (h(n) = {min_h})")
    print("----------------------------------")

    current = best_state
    g += 1


# Final Output
if is_goal(current):
    print("\nGoal State Reached!")
    print_state(current)