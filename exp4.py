def get_index(name, nodes):
    for i in range(len(nodes)):
        if nodes[i] == name:
            return i
    return -1

def add_edge(adj, nodes, src, dest):
    s = get_index(src, nodes)
    d = get_index(dest, nodes)
    adj[s][d] = 1
    adj[d][s] = 1

def print_list(arr, nodes):
    print("[", end="")
    for i in range(len(arr)):
        print(nodes[arr[i]], end="")
        if i != len(arr) - 1:
            print(", ", end="")
    print("]", end="")

def bfs(start_name, end_name, nodes, adj):
    vertices = len(nodes)
    visited = [False] * vertices
    queue = []
    closed = []

    start = get_index(start_name, nodes)
    end = get_index(end_name, nodes)

    queue.append(start)
    visited[start] = True

    print("\nBFS Traversal:")
    print(f"{'OPEN':<30}{'X':<10}CLOSED")
    print("-" * 60)

    while queue:
        open_list = queue.copy()
        x = queue.pop(0)
        closed.append(x)

        print(f"{[nodes[i] for i in open_list]!s:<30}{nodes[x]:<10}", end="")
        print([nodes[i] for i in closed])

        if x == end:
            break

        for i in range(vertices):
            if adj[x][i] == 1 and not visited[i]:
                visited[i] = True
                queue.append(i)

    print("\nFinal Path:", [nodes[i] for i in closed])

def dfs(start_name, end_name, nodes, adj):
    vertices = len(nodes)
    visited = [False] * vertices
    stack = []
    closed = []

    start = get_index(start_name, nodes)
    end = get_index(end_name, nodes)

    stack.append(start)

    print("\nDFS Traversal:")
    print(f"{'OPEN':<30}{'X':<10}CLOSED")
    print("-" * 60)

    while stack:
        open_list = stack.copy()
        x = stack.pop()
        closed.append(x)
        visited[x] = True

        print(f"{[nodes[i] for i in open_list]!s:<30}{nodes[x]:<10}", end="")
        print([nodes[i] for i in closed])

        if x == end:
            break

        for i in range(vertices - 1, -1, -1):
            if adj[x][i] == 1 and not visited[i]:
                visited[i] = True
                stack.append(i)

    print("\nFinal Path:", [nodes[i] for i in closed])

vertices = int(input("Enter number of vertices: "))
nodes = input("Enter node names (A B C or 0 1 2 etc): ").split()

adj = [[0] * vertices for _ in range(vertices)]

e = int(input("Enter number of edges: "))
print("Enter edges (source destination):")

for _ in range(e):
    s, d = input().split()
    add_edge(adj, nodes, s, d)

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

"""
Sample Input:
Enter number of vertices: 7
Enter node names (A B C or 0 1 2 etc): A B C D E F G
Enter number of edges: 7
Enter edges (source destination):
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
OPEN                          X         CLOSED
------------------------------------------------------------
['A']                         A         ['A']
['B', 'D']                    B         ['A', 'B']
['D', 'C', 'E']               D         ['A', 'B', 'D']
['C', 'E']                    C         ['A', 'B', 'D', 'C']
['E', 'F']                    E         ['A', 'B', 'D', 'C', 'E']
['F', 'G']                    F         ['A', 'B', 'D', 'C', 'E', 'F']
['G']                         G         ['A', 'B', 'D', 'C', 'E', 'F', 'G']

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
OPEN                          X         CLOSED
------------------------------------------------------------
['A']                         A         ['A']
['D', 'B']                    B         ['A', 'B']
['D', 'E', 'C']               C         ['A', 'B', 'C']
['D', 'E', 'F']               F         ['A', 'B', 'C', 'F']
['D', 'E']                    E         ['A', 'B', 'C', 'F', 'E']
['D', 'G']                    G         ['A', 'B', 'C', 'F', 'E', 'G']

Final Path: ['A', 'B', 'C', 'F', 'E', 'G']
"""