graph = {}

def bfs(start, end):
    visited = []
    queue = [start]
    closed = []

    print("\nBFS Traversal:")
    print(f"{'OPEN':<20}{'X':<10}CLOSED")
    print("-" * 45)

    while queue:
        open_list = queue.copy()
        x = queue.pop(0)

        if x not in visited:
            visited.append(x)
            closed.append(x)

            print(f"{str(open_list):<20}{x:<10}{closed}")

            if x == end:
                break

            for neighbor in graph[x]:
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)

    print("\nFinal Path:", closed)

def dfs(start, end):
    visited = []
    stack = [start]
    closed = []

    print("\nDFS Traversal:")
    print(f"{'OPEN':<20}{'X':<10}CLOSED")
    print("-" * 45)

    while stack:
        open_list = stack.copy()
        x = stack.pop()

        if x not in visited:
            visited.append(x)
            closed.append(x)

            print(f"{str(open_list):<20}{x:<10}{closed}")

            if x == end:
                break

            for neighbor in reversed(graph[x]):
                if neighbor not in visited and neighbor not in stack:
                    stack.append(neighbor)

    print("\nFinal Path:", closed)

n = int(input("Enter number of vertices: "))
nodes = input("Enter node names: ").split()

for node in nodes:
    graph[node] = []

e = int(input("Enter number of edges: "))
print("Enter edges:")

for _ in range(e):
    u, v = input().split()
    graph[u].append(v)
    graph[v].append(u)

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
        bfs(start, end)
    elif choice == 2:
        dfs(start, end)
    else:
        print("Invalid choice!")

"""
Sample Input:
Enter number of vertices: 7
Enter node names: A B C D E F G
Enter number of edges: 7
Enter edges:
A B
A D
B C
B E
D E
C F
E G

--- MENU ---
1. BFS
2. DFS
3. Exit
Enter your choice: 1
Enter starting node: A
Enter ending node: G

Sample Output (BFS):
BFS Traversal:
OPEN                X         CLOSED
---------------------------------------------
['A']               A         ['A']
['B', 'D']          B         ['A', 'B']
['D', 'C', 'E']     D         ['A', 'B', 'D']
['C', 'E']          C         ['A', 'B', 'D', 'C']
['E', 'F']          E         ['A', 'B', 'D', 'C', 'E']
['F', 'G']          F         ['A', 'B', 'D', 'C', 'E', 'F']
['G']               G         ['A', 'B', 'D', 'C', 'E', 'F', 'G']

Final Path: ['A', 'B', 'D', 'C', 'E', 'F', 'G']


--- MENU ---
1. BFS
2. DFS
3. Exit
Enter your choice: 2
Enter starting node: A
Enter ending node: G

Sample Output (DFS):
DFS Traversal:
OPEN                X         CLOSED
---------------------------------------------
['A']               A         ['A']
['D', 'B']          B         ['A', 'B']
['D', 'E', 'C']     C         ['A', 'B', 'C']
['D', 'E', 'F']     F         ['A', 'B', 'C', 'F']
['D', 'E']          E         ['A', 'B', 'C', 'F', 'E']
['D', 'G']          G         ['A', 'B', 'C', 'F', 'E', 'G']

Final Path: ['A', 'B', 'C', 'F', 'E', 'G']
"""