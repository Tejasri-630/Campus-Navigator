graph = {
    "Main Gate": {
        "Library": 100,
        "CSE Block": 150
    },
    "Library": {
        "Main Gate": 100,
        "Canteen": 80
    },
    "CSE Block": {
        "Main Gate": 150,
        "Canteen": 120
    },
    "Canteen": {
        "Library": 80,
        "CSE Block": 120
    }
}
graph["Sports"] = {}
def shortest_path(graph, source, destination):
    distance = {}
    parent = {}
    for location in graph:
        distance[location]  = float('inf')
        parent[location] = None
    distance[source] = 0
    visited = set()
    for _ in range(len(graph)):
        current = min((location for location in graph if location not in visited) , key = distance.get)
        visited.add(current)     
        if distance[current] == float('inf'):
                    break   
        for neighbor , dist in graph[current].items():
            if neighbor not in visited:
                new_distance = distance[current] + dist
                if new_distance < distance[neighbor]:
                    distance[neighbor] = new_distance
                    parent[neighbor] = current
    if distance[destination] == float('inf'):
        return (None , None)
    route = []
    current = destination
    while current is not None:
        route.append(current)
        current = parent[current]
    route.reverse()
    return (route , distance[destination])

locations = list(graph.keys())
print("Locations in the graph:")
for location in locations:
     print(location)
source = input("Enter the source location: ")
source = next(
    (loc for loc in locations if loc.lower() == source.lower()),
    None
)
if source is None:
    print("Invalid source location.")
    exit()
destination = input("Enter the destination location: ")
destination = next(
    (loc for loc in locations if loc.lower() == destination.lower()),
    None
)
if destination is None:
     print("Invalid destination location.")
     exit()
route , total_dist = shortest_path(graph, source, destination)
if route:
    print("Shortest path:", " -> ".join(route))
    print("Total distance:", total_dist, "meters")
else:
    print("No path found.")

