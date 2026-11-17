
# Campus Navigator - SVECW

locations = [
    "Main Gate",
    "Temple Square",
    "Temple",
    "Annapurna Canteen",
    "Xerox Center",
    "Telugu Talli Statue",
    "D Block",
    "Hostel Entrance",
    "A Block",
    "B Block",
    "C Block",
    "Seetha Indoor Auditorium",
    "Library",
    "Central Square",
    "Sports Complex",
    "Sports Complex - ATM Entrance",
    "Sports Complex - Fresh Choice Entrance",
    "Fresh Choice",
    "Snacks Area",
    "Medical Shop",
    "SBI ATM",
    "ICICI Bank ATM",
    "Medha Hostel",
    "Administration Hub",
    "AR/VR Studio",
    "Brewista",
    "Radio Vishnu 90.4",
    "Smruthi Vanam",
    "Jewel Labs"
]
# Format:
# (Location 1, Location 2, estimated distance in metres)

connections = [

    # 1. Main Gate and Temple area
    ("Main Gate", "Temple Square", 120),
    ("Temple Square", "Temple", 40),
    ("Temple Square", "Snacks Area", 20),
    ("Temple", "Annapurna Canteen", 70),
    ("Annapurna Canteen", "Telugu Talli Statue", 40),
    ("Annapurna Canteen", "Xerox Center", 0),
    ("Seetha Indoor Auditorium", "Jewel Labs", 10),

    # 2. Snacks and shops
    ("Snacks Area", "Fresh Choice", 300),
    ("Medical Shop", "SBI ATM", 25),
    ("Medical Shop", "ICICI Bank ATM", 0),

    # 3. Sports Complex and its two entrances
    ("SBI ATM", "Sports Complex - ATM Entrance", 15),
    ("Medical Shop", "Sports Complex - ATM Entrance", 35),

    ("Fresh Choice", "Sports Complex - Fresh Choice Entrance", 100),

    ("Sports Complex - ATM Entrance", "Sports Complex", 0),
    ("Sports Complex - Fresh Choice Entrance", "Sports Complex", 0),


    # 4. Academic blocks and Hostel Entrance
    ("Telugu Talli Statue", "D Block", 70),
    ("D Block", "Hostel Entrance", 100),
    ("Hostel Entrance", "A Block", 80),
    ("A Block", "B Block", 30),
    ("B Block", "C Block", 30),
    # 5. C Block, Library, Auditorium and Radio
    ("C Block", "Library", 35),
    ("Library", "Seetha Indoor Auditorium", 100),
    ("Seetha Indoor Auditorium", "Radio Vishnu 90.4", 10),

    # Additional direct walking connections
    ("C Block", "Seetha Indoor Auditorium", 75),
    ("Telugu Talli Statue", "Seetha Indoor Auditorium", 350),
    ("Radio Vishnu 90.4", "Telugu Talli Statue", 340),

    # 6. Central Square connections
    ("Central Square", "Hostel Entrance", 80),
    ("Administration Hub", "Brewista", 0),
    ("Brewista", "Medha Hostel", 40),  # provisional
    ("Medha Hostel", "Central Square", 150),     # provisional
    ("Medha Hostel", "ICICI Bank ATM", 150),  # provisional # 
    ("ICICI Bank ATM", "Central Square", 100),  # provisional

    # 7. Medha Hostel and Administration Hub
    ("Sports Complex - Fresh Choice Entrance", "Medical Shop", 120),
    ("Medha Hostel", "Administration Hub", 40),
    ("Administration Hub", "C Block", 90),
    ("Administration Hub", "Brewista", 0),
    ("Administration Hub", "AR/VR Studio", 0),

    # 8. Smruthi Vanam - access from surrounding locations
    ("Smruthi Vanam", "Telugu Talli Statue", 35),
    ("Smruthi Vanam", "D Block", 45),
    ("Smruthi Vanam", "Hostel Entrance", 55),
    ("Smruthi Vanam", "A Block", 50),
    ("Smruthi Vanam", "B Block", 60),
    ("Smruthi Vanam", "C Block", 65),
    ("Smruthi Vanam", "Seetha Indoor Auditorium", 40),
    ("Smruthi Vanam", "Radio Vishnu 90.4", 30),

    # 9. Jewel Labs - upward slope from C Block
    ("C Block", "Jewel Labs", 80)
]


# Initialize weighted adjacency list
graph = {location: {} for location in locations}


# Add undirected connections
def add_connection(location1, location2, distance):

    if location1 not in graph or location2 not in graph:
        raise ValueError("Location not found")

    if distance < 0:
        raise ValueError("Distance cannot be negative")

    graph[location1][location2] = distance
    graph[location2][location1] = distance


# Build the graph
for location1, location2, distance in connections:
    add_connection(location1, location2, distance)


# Display the weighted graph

def shortest_path(graph, source, destination):

    if source not in graph or destination not in graph:
        return None, None

    distance = {location: float('inf') for location in graph}
    parent = {location: None for location in graph}

    distance[source] = 0
    visited = set()

    restricted_intermediate = {
        "Smruthi Vanam",
        "Sports Complex"
    }

    for _ in range(len(graph)):

        unvisited = [
            location for location in graph
            if location not in visited
        ]

        if not unvisited:
            break

        current = min(unvisited, key=lambda x: distance[x])

        if distance[current] == float('inf'):
            break

        visited.add(current)

        # Destination reached: no need to explore further
        if current == destination:
            break

        # Don't expand restricted locations unless they are the source
        if current in restricted_intermediate and current != source:
            continue

        for neighbor, dist in graph[current].items():

            if neighbor not in visited:

                new_distance = distance[current] + dist

                if new_distance < distance[neighbor]:
                    distance[neighbor] = new_distance
                    parent[neighbor] = current

    if distance[destination] == float('inf'):
        return None, None

    route = []
    current = destination

    while current is not None:
        route.append(current)
        current = parent[current]

    route.reverse()

    return route, distance[destination]