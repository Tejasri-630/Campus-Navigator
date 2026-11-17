
from graph import graph, locations, shortest_path
from aliases import location_aliases
from difflib import get_close_matches


def get_all_location_names():

    name_to_location = {}

    # Add actual location names
    for location in locations:
        name_to_location[location.lower()] = location

    # Add aliases
    for location, aliases in location_aliases.items():
        for alias in aliases:
            name_to_location[alias.lower()] = location

    return name_to_location


def suggest_location(user_input):

    name_to_location = get_all_location_names()

    possible_names = list(name_to_location.keys())

    suggestions = get_close_matches(
        user_input.lower(),
        possible_names,
        n=3,
        cutoff=0.6
    )

    results = []

    for suggestion in suggestions:

        location = name_to_location[suggestion]

        if location not in results:
            results.append(location)

    return results

def normalize_location(user_input):

    user_input = user_input.strip().lower()

    # 1. Exact location matching
    for location in locations:
        if user_input == location.lower():
            return location

    # 2. Exact alias matching
    for location, aliases in location_aliases.items():
        if user_input in aliases:
            return location

    
    
    # 3. Word-based partial matching
    matches = []

    for location in locations:

        words = user_input.split()

        if all(word in location.lower() for word in words):
            matches.append(location)

    for location, aliases in location_aliases.items():

        for alias in aliases:

            if all(word in alias for word in words):
                matches.append(location)

    matches = list(set(matches))
    if len(matches) == 1:
            return matches[0]

        # 4. Typo suggestions
    suggestions = suggest_location(user_input)

    if suggestions:

        print("\nDid you mean one of these locations?")

        for index, location in enumerate(suggestions, start=1):
            print(f"{index}. {location}")

        print("0. None of these")

        choice = input("Enter your choice: ").strip()

        if choice.isdigit():

            choice = int(choice)

            if 1 <= choice <= len(suggestions):
                return suggestions[choice - 1]

    # print("\nLocation not recognised.")
    # print("Please try again.")


    return None



# def get_location(message):

#     while True:

#         user_input = input(message).strip().lower()

#         # First check actual location names
#         for location in locations:

#             if user_input == location.lower():
#                 return location

#         # Then check alternative names
#         for location, aliases in location_aliases.items():

#             if user_input in aliases:
#                 return location

#         print("\nLocation not recognised!")
#         print("Please enter a valid campus location.")
def get_location(message):

    while True:

        user_input = input(message)

        location = normalize_location(user_input)

        if location is not None:
            return location

        print("Location not recognised or ambiguous.")
        print("Please enter a more specific location.")

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

