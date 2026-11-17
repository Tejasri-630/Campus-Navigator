from flask import Flask, render_template, request, jsonify
from graph import locations, graph, shortest_path
from main import normalize_location
from aliases import location_aliases
app = Flask(__name__)

@app.route("/")
def home():
    return render_template(
        "index.html",
        locations = locations)
@app.route("/find-route", methods=["POST"])
def find_route():

    data = request.get_json()

    source_input = data.get("source", "")
    destination_input = data.get("destination", "")

    source = normalize_location(source_input)
    destination = normalize_location(destination_input)

    if source is None:
        return jsonify({"error": "Invalid or ambiguous starting location."}), 400

    if destination is None:
        return jsonify({"error": "Invalid or ambiguous destination."}), 400

    if source == destination:
        return jsonify({"error": "Source and destination cannot be the same."}), 400

    route, total_distance = shortest_path(graph, source, destination)

    if route is None:
        return jsonify({"error": "No route found."}), 404

    return jsonify({
        "route": route,
        "distance": total_distance
    })
@app.route("/suggestions")
def get_suggestions():
    query = request.args.get("q", "").strip().lower()

    if not query:
        return jsonify([])

    results = []

    # Search official campus location names
    for location in locations:
        if query in location.lower():
            results.append({
                "label": location,
                "value": location
            })

    # Search alternative names (aliases)
    for location, aliases in location_aliases.items():
        for alias in aliases:
            if query in alias.lower():
                results.append({
                    "label": f"{alias} — {location}",
                    "value": location
                })

    # Remove duplicate locations
    unique_results = []
    seen = set()

    for item in results:
        if item["value"] not in seen:
            seen.add(item["value"])
            unique_results.append(item)

    return jsonify(unique_results)
if __name__ == "__main__":
    app.run(debug = True)