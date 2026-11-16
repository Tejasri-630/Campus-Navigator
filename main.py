
from graph import graph, locations, shortest_path
from alias import location_aliases


def get_location(message):

    while True:

        user_input = input(message).strip().lower()

        # First check actual location names
        for location in locations:

            if user_input == location.lower():
                return location

        # Then check alternative names
        for location, aliases in location_aliases.items():

            if user_input in aliases:
                return location

        print("\nLocation not recognised!")
        print("Please enter a valid campus location.")


def display_route(route, total_distance):

    if route is None:
        print("\nNo route found between these locations.")
        return

    print("\n========== ROUTE DETAILS ==========")

    print("\nShortest Route:")

    for index, location in enumerate(route):
        print(f"{index + 1}. {location}")

    print("\nTotal Distance:", total_distance, "metres")

    print("Number of locations visited:", len(route))

    print("Number of road segments:", len(route) - 1)

    print("===================================")


def find_route(source, destination):

    if source == destination:
        print("\nYou are already at your destination!")
        return

    route, total_distance = shortest_path(
        graph, source, destination
    )

    display_route(route, total_distance)



def main():

    print("\n================================")
    print("       CAMPUS NAVIGATOR")
    print("  Shri Vishnu Engineering College")
    print("================================")

    while True:

        print("\n1. Find Shortest Route")
        print("2. View All Campus Locations")
        print("3. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":

            source = get_location("\nEnter starting location: ")
            destination = get_location("\nEnter destination: ")

            find_route(source, destination)

        elif choice == "2":

            print("\n====== CAMPUS LOCATIONS ======")

            for index, location in enumerate(locations, start=1):
                print(f"{index}. {location}")

            print("==============================")

        elif choice == "3":

            print("\nThank you for using Campus Navigator!")
            break

        else:
            print("\nInvalid choice! Please select 1, 2 or 3.")


if __name__ == "__main__":
    main()

