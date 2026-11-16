# Vacuum Cleaner Problem - Two Rooms (A and B)

def vacuum_cleaner(room_A, room_B, start_room):

    rooms = {
        "A": room_A,
        "B": room_B
    }

    current_room = start_room

    print("\nInitial State:")
    print("Room A:", rooms["A"])
    print("Room B:", rooms["B"])
    print("Vacuum starts in Room:", current_room)

    while rooms["A"] == "Dirty" or rooms["B"] == "Dirty":

        print("\nVacuum is in Room", current_room)

        # If current room is dirty, clean it
        if rooms[current_room] == "Dirty":
            print("Room", current_room, "is Dirty")
            print("Action: SUCK")
            rooms[current_room] = "Clean"

        else:
            print("Room", current_room, "is Clean")

            # Move to the other room
            if current_room == "A":
                current_room = "B"
                print("Action: MOVE RIGHT")
            else:
                current_room = "A"
                print("Action: MOVE LEFT")

    print("\nFinal State:")
    print("Room A:", rooms["A"])
    print("Room B:", rooms["B"])
    print("Both rooms are Clean!")
    print("Goal State Reached.")


# Input
room_A = input("Enter status of Room A (Clean/Dirty): ").capitalize()
room_B = input("Enter status of Room B (Clean/Dirty): ").capitalize()
start_room = input("Enter starting room (A/B): ").upper()

# Run the vacuum cleaner
vacuum_cleaner(room_A, room_B, start_room)
