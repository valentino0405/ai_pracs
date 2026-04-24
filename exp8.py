def partial_order_planner(initial_state, goal_state):
    # Plan starts with "Start"
    plan = ["Start"]

    # Copy initial state so we don't modify original input
    current_state = initial_state.copy()

    print("\nInitial State:", current_state)
    print("Goal State:", goal_state)

    step = 1

    # Loop through each goal one by one
    for goal in goal_state:

        # If goal is already satisfied, skip it
        if goal not in current_state:

            print("\nStep", step, ": Achieving goal ->", goal)

            # Split goal into block and its position
            # Example: "A-B" → block = A, position = B
            block, position = goal.split("-")

            # Decide action based on position
            if position == "table":
                action = f"Put {block} on table"
            else:
                action = f"Stack {block} on {position}"

            # Add action to plan
            print("Action added to plan:", action)
            plan.append(action)

            # Update current state (goal achieved)
            current_state.append(goal)

            print("Current State:", current_state)

            step += 1

    # Add final step
    plan.append("Finish")

    # Print final plan
    print("\nFinal Plan:")
    for p in plan:
        print(p)


# ----------- USER INPUT -------------

initial_input = input("Enter initial state (comma separated, e.g. A-table,B-A): ")
goal_input = input("Enter goal state (comma separated, e.g. C-B,A-C): ")

# Convert input string → list
initial_state = [x.strip() for x in initial_input.split(",")]
goal_state = [x.strip() for x in goal_input.split(",")]

# Call planner
partial_order_planner(initial_state, goal_state)