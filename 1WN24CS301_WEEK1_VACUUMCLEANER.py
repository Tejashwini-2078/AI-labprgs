# Vacuum Cleaner Agent

def vacuum_agent(room_a, room_b, position):
    print("Initial State:")
    print("Room A:", room_a)
    print("Room B:", room_b)
    print("Vacuum Position:", position)
    print()

    while room_a == "Dirty" or room_b == "Dirty":

        if position == "A":
            if room_a == "Dirty":
                print("Room A is Dirty -> Sucking dirt...")
                room_a = "Clean"
                print("Room A is now Clean")
            else:
                print("Room A is Clean -> Moving to Room B")
                position = "B"

        elif position == "B":
            if room_b == "Dirty":
                print("Room B is Dirty -> Sucking dirt...")
                room_b = "Clean"
                print("Room B is now Clean")
            else:
                print("Room B is Clean -> Moving to Room A")
                position = "A"

        print()

    print("Goal State Reached!")
    print("Room A:", room_a)
    print("Room B:", room_b)
    print("Vacuum Position:", position)


# Initial state
room_a = "Dirty"
room_b = "Dirty"
position = "A"

# Run the vacuum cleaner agent
vacuum_agent(room_a, room_b, position)
