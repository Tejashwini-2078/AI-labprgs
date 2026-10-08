

# 8-Puzzle using DFS

initial = (1, 2, 3,
           4, 0, 6,
           7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


def print_board(state):
    for i in range(0, 9, 3):
        print(state[i], state[i + 1], state[i + 2])
    print()


def get_moves(state):
    moves = []
    blank = state.index(0)

    row = blank // 3
    col = blank % 3

    # Up
    if row > 0:
        new_state = list(state)
        new_state[blank], new_state[blank - 3] = \
            new_state[blank - 3], new_state[blank]
        moves.append(("UP", tuple(new_state)))

    # Down
    if row < 2:
        new_state = list(state)
        new_state[blank], new_state[blank + 3] = \
            new_state[blank + 3], new_state[blank]
        moves.append(("DOWN", tuple(new_state)))

    # Left
    if col > 0:
        new_state = list(state)
        new_state[blank], new_state[blank - 1] = \
            new_state[blank - 1], new_state[blank]
        moves.append(("LEFT", tuple(new_state)))

    # Right
    if col < 2:
        new_state = list(state)
        new_state[blank], new_state[blank + 1] = \
            new_state[blank + 1], new_state[blank]
        moves.append(("RIGHT", tuple(new_state)))

    return moves


def dfs():
    stack = [(initial, [])]
    visited = set()

    while stack:
        state, path = stack.pop()

        if state == goal:
            return path

        if state in visited:
            continue

        visited.add(state)

        for move, new_state in get_moves(state):
            if new_state not in visited:
                stack.append((new_state, path + [move]))

    return None


# Run DFS
solution = dfs()

print("Initial State:")
print_board(initial)

if solution:
    print("Solution using DFS:")
    for i, move in enumerate(solution, 1):
        print(i, ".", move)

    print("\nNumber of moves:", len(solution))
    print("\nGoal State:")
    print_board(goal)
else:
    print("No solution exists")
