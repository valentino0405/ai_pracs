# BFS and DFS using simple graph

# Graph stored as dictionary
graph = {}

# ---------------- BFS ----------------
def bfs(start, end):
    visited = []
    queue = [start]

    print("\nBFS Traversal:")

    while queue:
        node = queue.pop(0)   # remove first element

        if node not in visited:
            print(node, end=" ")
            visited.append(node)

            if node == end:
                break

            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

    print("\nFinal Path:", visited)


# ---------------- DFS ----------------
def dfs(start, end):
    visited = []
    stack = [start]

    print("\nDFS Traversal:")

    while stack:
        node = stack.pop()   # remove last element

        if node not in visited:
            print(node, end=" ")
            visited.append(node)

            if node == end:
                break

            # reverse so output stays proper
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

    print("\nFinal Path:", visited)


# ---------------- MAIN ----------------
n = int(input("Enter number of vertices: "))

nodes = input("Enter node names: ").split()

# create empty list for each node
for node in nodes:
    graph[node] = []

e = int(input("Enter number of edges: "))
print("Enter edges:")

for _ in range(e):
    u, v = input().split()
    graph[u].append(v)
    graph[v].append(u)   # undirected graph

while True:
    print("\n1. BFS")
    print("2. DFS")
    print("3. Exit")

    choice = int(input("Enter choice: "))

    if choice == 3:
        print("Exiting...")
        break

    start = input("Enter start node: ")
    end = input("Enter end node: ")

    if choice == 1:
        bfs(start, end)
    elif choice == 2:
        dfs(start, end)
    else:
        print("Invalid choice")