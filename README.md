# Campus Navigator

A campus navigation web application that helps users find the shortest
paths between locations within a college using **Dijkstra's algorithm**.
It includes location aliases, input normalization, autocomplete
suggestions, and an interactive web interface built with Flask, HTML,
CSS, and JavaScript.

## Features

-   **Shortest-path navigation:** Finds a shortest route between two
    campus locations using Dijkstra's algorithm.
-   **Location aliases:** Recognizes alternative names and common terms
    for supported campus locations.
-   **Input normalization:** Helps map user-entered location names to
    the locations defined in the campus graph.
-   **Autocomplete suggestions:** Displays matching locations and
    aliases as the user types.
-   **Popular destinations:** Lets users select a destination from
    featured campus locations.
-   **Route display:** Shows the route as a sequence of locations and
    displays the total distance.

## Tech Stack

-   **Language:** Python
-   **Backend:** Flask
-   **Frontend:** HTML, CSS, JavaScript
-   **Algorithm:** Dijkstra's shortest-path algorithm

## Project Structure

``` text
Campus-Navigator/
├── app.py
├── graph.py
├── main.py
├── aliases.py
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── script.js
└── .gitignore
```

## Getting Started

### Prerequisites

-   Python 3 installed
-   Git (optional, for cloning the repository)

### 1. Clone the repository

``` bash
git clone https://github.com/Tejasri-630/Campus-Navigator.git
cd Campus-Navigator
```

### 2. (Optional) Create and activate a virtual environment

On Windows:

``` bash
python -m venv .venv
.venv\Scripts\activate
```

On macOS or Linux:

``` bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Flask

``` bash
python -m pip install Flask
```

### 4. Run the application

``` bash
python app.py
```

Open the local address shown in the terminal (usually
`http://127.0.0.1:5000/`) in your browser.

## How It Works

1.  The campus locations and weighted connections are represented as a
    graph.
2.  The user enters a starting location and a destination.
3.  Location normalization and aliases help identify the intended campus
    locations.
4.  Flask passes the validated locations to the shortest-path
    implementation.
5.  Dijkstra's algorithm calculates the route with the minimum total
    edge weight.
6.  The interface displays the sequence of locations and the total
    distance.

## Current Scope

The current version uses the campus graph and its configured edge
weights to calculate routes. GPS-based current-location detection is
**not yet implemented**.

## Future Improvements

-   Add GPS-based starting-location detection.
-   Improve the campus map and route visualization.
-   Add more campus locations and verify their distance data.
-   Add tests for graph traversal, location normalization, and route
    handling.

## Author

**Tejasri-630**

[View the GitHub
repository](https://github.com/Tejasri-630/Campus-Navigator)
