goal = []
visited = []

def h(state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal[i][j]:
                count += 1
    return count

def show(state):
    for row in state:
        print(*row)

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

"""
INPUT:
2 8 3
1 6 4
7 0 5
1 2 3
8 0 4
7 6 5

OUTPUT:
Note: For Blank Tile Enter 0
Enter Initial State:
2 8 3
1 6 4
7 0 5
Enter Goal State:
1 2 3
8 0 4
7 6 5

Current State (g=0):
2 8 3
1 6 4
7 0 5
Move: Up -> g(n)=1 h(n)=3 f(n)=4
Move: Left -> g(n)=1 h(n)=5 f(n)=6
Move: Right -> g(n)=1 h(n)=5 f(n)=6

Chosen Move: Up with f(n) = 4 (h(n) = 3)
----------------------------------

Current State (g=1):
2 8 3
1 0 4
7 6 5
Move: Up -> g(n)=2 h(n)=3 f(n)=5
Move: Left -> g(n)=2 h(n)=3 f(n)=5
Move: Right -> g(n)=2 h(n)=4 f(n)=6

Chosen Move: Up with f(n) = 5 (h(n) = 3)
----------------------------------

Current State (g=2):
2 0 3
1 8 4
7 6 5
Move: Left -> g(n)=3 h(n)=2 f(n)=5
Move: Right -> g(n)=3 h(n)=4 f(n)=7

Chosen Move: Left with f(n) = 5 (h(n) = 2)
----------------------------------

Current State (g=3):
0 2 3
1 8 4
7 6 5
Move: Down -> g(n)=4 h(n)=1 f(n)=5

Chosen Move: Down with f(n) = 5 (h(n) = 1)
----------------------------------

Current State (g=4):
1 2 3
0 8 4
7 6 5
Move: Down -> g(n)=5 h(n)=2 f(n)=7
Move: Right -> g(n)=5 h(n)=0 f(n)=5

Chosen Move: Right with f(n) = 5 (h(n) = 0)
----------------------------------

Goal State Reached!
1 2 3
8 0 4
7 6 5
"""