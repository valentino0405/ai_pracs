# A* for 8 Puzzle (Simple Version)

goal = []
visited = []

# Count misplaced tiles
def h(state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal[i][j]:
                count += 1
    return count

# Print puzzle
def show(state):
    for row in state:
        print(*row)

# Convert state into string for visited
def make_string(state):
    s = ""
    for row in state:
        for x in row:
            s += str(x)
    return s


print("Note: For Blank Tile Enter 0")
print("Enter Initial State:")
current = [list(map(int, input().split())) for _ in range(3)]

print("Enter Goal State:")
goal = [list(map(int, input().split())) for _ in range(3)]

g = 0

while current != goal:
    visited.append(make_string(current))

    print(f"\nCurrent State (g={g}):")
    show(current)

    # Find blank tile
    for i in range(3):
        for j in range(3):
            if current[i][j] == 0:
                r, c = i, j

    best = None
    best_f = 999
    best_h = 999
    best_move = ""

    moves = [("Up", -1, 0), ("Down", 1, 0), ("Left", 0, -1), ("Right", 0, 1)]

    for name, dr, dc in moves:
        nr, nc = r + dr, c + dc

        if 0 <= nr < 3 and 0 <= nc < 3:
            temp = [row[:] for row in current]
            temp[r][c], temp[nr][nc] = temp[nr][nc], temp[r][c]

            if make_string(temp) not in visited:
                new_h = h(temp)
                new_g = g + 1
                f = new_g + new_h

                print(f"Move: {name} -> g(n)={new_g} h(n)={new_h} f(n)={f}")

                if f < best_f or (f == best_f and new_h < best_h):
                    best = temp
                    best_f = f
                    best_h = new_h
                    best_move = name

    if best is None:
        print("\nStuck! No valid moves.")
        break

    print(f"\nChosen Move: {best_move} with f(n) = {best_f} (h(n) = {best_h})")
    print("----------------------------------")

    current = best
    g += 1

print("\nGoal State Reached!")
show(current)