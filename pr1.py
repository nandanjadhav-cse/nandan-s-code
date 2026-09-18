from collections import deque

# Goal state
GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

def print_puzzle(state):
    """Print the puzzle in 3x3 format."""
    for i in range(0, 9, 3):
        print(" ".join("_" if x == 0 else str(x)
                       for x in state[i:i + 3]))
    print()

def get_neighbors(state):
    """Generate all possible next states."""
    neighbors = []
    blank = state.index(0)
    row = blank // 3
    col = blank % 3

    moves = [
        ("Up", -1, 0),
        ("Down", 1, 0),
        ("Left", 0, -1),
        ("Right", 0, 1)
    ]

    for move, dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:

            new_blank = new_row * 3 + new_col

            new_state = list(state)
            # Swap blank and tile
            new_state[blank], new_state[new_blank] = \
                new_state[new_blank], new_state[blank]

            neighbors.append((tuple(new_state), move))
    return neighbors

def solve(initial):
    """Solve the puzzle using BFS."""

    queue = deque([initial])

    visited = {initial}

    parent = {initial: None}
    move_taken = {}

    while queue:
        current = queue.popleft()
        # Goal test
        if current == GOAL:
            path = []
            moves = []

            while current is not None:
                path.append(current)

                if parent[current] is not None:
                    moves.append(move_taken[current])

                current = parent[current]

            path.reverse()
            moves.reverse()

            return path, moves

        # Generate next states
        for next_state, move in get_neighbors(current):

            if next_state not in visited:

                visited.add(next_state)
                queue.append(next_state)

                parent[next_state] = current
                move_taken[next_state] = move

    return None
# MAIN PROGRAM 
print("8-PUZZLE")
print("Enter numbers from 0 to 8.")
print("Use 0 for the blank space.")
print()

print("Enter the puzzle row by row:")

numbers = []

for i in range(3):
    row = list(map(int, input(f"Row {i + 1}: ").split()))
    numbers.extend(row)

# Convert to tuple
initial_state = tuple(numbers)

# Check input
if len(initial_state) != 9 or set(initial_state) != set(range(9)):
    print("Invalid input!")
    print("You must enter numbers 0 to 8 exactly once.")
    exit()

print("\nInitial State:")
print_puzzle(initial_state)

print("Solving...")

result = solve(initial_state)

if result is None:

    print("No solution found.")

else:

    path, moves = result

    print("\nSolution Found!")
    print("Number of moves:", len(moves))

    print("\nMoves:")
    print(" -> ".join(moves))

    print("\nSolution Steps:")

    for i, state in enumerate(path):

        print("Step", i)
        print_puzzle(state)