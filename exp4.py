# ==============================
# BFS & DFS Graph Implementation
# ==============================

# Function to get index of node name
def get_index(name, nodes):
    for i in range(len(nodes)):
        if nodes[i] == name:
            return i
    return -1  # if not found


# Function to add edge in adjacency matrix
def add_edge(adj, nodes, src, dest):
    s = get_index(src, nodes)
    d = get_index(dest, nodes)

    # Since graph is undirected, mark both sides
    adj[s][d] = 1
    adj[d][s] = 1


# Function to print nodes nicely using names
def print_list(arr, nodes):
    print("[", end="")
    for i in range(len(arr)):
        print(nodes[arr[i]], end="")
        if i != len(arr) - 1:
            print(", ", end="")
    print("]", end="")


# ==============================
# BFS (Breadth First Search)
# ==============================
def bfs(start_name, end_name, nodes, adj):

    vertices = len(nodes)

    # Track visited nodes
    visited = [False] * vertices

    # Queue for BFS (FIFO)
    queue = []

    # CLOSED list (final traversal path)
    closed = []

    start = get_index(start_name, nodes)
    end = get_index(end_name, nodes)

    # Step 1: Add starting node
    queue.append(start)
    visited[start] = True  # mark visited when inserting

    print("\nBFS Traversal:")
    print(f"{'OPEN':<30}{'X':<10}CLOSED")
    print("-" * 60)

    # Loop until queue becomes empty
    while queue:

        # OPEN = current queue state
        open_list = queue.copy()

        # Remove first element (FIFO)
        x = queue.pop(0)

        # Add to CLOSED list
        closed.append(x)

        # Print current step
        print(f"{[nodes[i] for i in open_list]!s:<30}{nodes[x]:<10}", end="")
        print([nodes[i] for i in closed])

        # Stop if destination reached
        if x == end:
            break

        # Traverse all neighbors
        for i in range(vertices):

            # If edge exists and node not visited
            if adj[x][i] == 1 and not visited[i]:
                visited[i] = True  # mark visited immediately
                queue.append(i)    # add to queue

    print("\nFinal Path:", [nodes[i] for i in closed])


# ==============================
# DFS (Depth First Search)
# ==============================
def dfs(start_name, end_name, nodes, adj):

    vertices = len(nodes)

    # Track visited nodes
    visited = [False] * vertices

    # Stack for DFS (LIFO)
    stack = []

    # CLOSED list
    closed = []

    start = get_index(start_name, nodes)
    end = get_index(end_name, nodes)

    # Step 1: Push start node
    stack.append(start)

    print("\nDFS Traversal:")
    print(f"{'OPEN':<30}{'X':<10}CLOSED")
    print("-" * 60)

    # Loop until stack becomes empty
    while stack:

        # OPEN = current stack
        open_list = stack.copy()

        # Pop last element (LIFO)
        x = stack.pop()

        # Add to CLOSED
        closed.append(x)

        # Mark visited AFTER popping
        visited[x] = True

        # Print current step
        print(f"{[nodes[i] for i in open_list]!s:<30}{nodes[x]:<10}", end="")
        print([nodes[i] for i in closed])

        # Stop if destination reached
        if x == end:
            break

        # Traverse neighbors in reverse order
        # (to match expected output order)
        for i in range(vertices - 1, -1, -1):

            if adj[x][i] == 1 and not visited[i]:
                visited[i] = True  # mark when pushing
                stack.append(i)    # push to stack

    print("\nFinal Path:", [nodes[i] for i in closed])


# ==============================
# MAIN PROGRAM
# ==============================

# Input number of vertices
vertices = int(input("Enter number of vertices: "))

# Input node names
nodes = input("Enter node names (A B C or 0 1 2 etc): ").split()

# Create adjacency matrix initialized to 0
adj = [[0] * vertices for _ in range(vertices)]

# Input edges
e = int(input("Enter number of edges: "))
print("Enter edges (source destination):")

for _ in range(e):
    s, d = input().split()
    add_edge(adj, nodes, s, d)

# Menu-driven program
while True:
    print("\n--- MENU ---")
    print("1. BFS")
    print("2. DFS")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 3:
        print("Exiting...")
        break

    start = input("Enter starting node: ")
    end = input("Enter ending node: ")

    if choice == 1:
        bfs(start, end, nodes, adj)
    elif choice == 2:
        dfs(start, end, nodes, adj)
    else:
        print("Invalid choice!")