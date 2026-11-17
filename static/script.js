// AUTOCOMPLETE
function setupAutocomplete(inputId, suggestionId) {
    const input = document.getElementById(inputId);
    const suggestionBox = document.getElementById(suggestionId);

    input.addEventListener("input", async function () {
        const query = input.value.trim();

        suggestionBox.innerHTML = "";

        if (query.length === 0) {
            suggestionBox.style.display = "none";
            return;
        }
        try {
            const response = await fetch(
                `/suggestions?q=${encodeURIComponent(query)}`
            );

            const suggestions = await response.json();

            suggestions.forEach(item => {
                const option = document.createElement("div");

                option.textContent = item.label;
                option.classList.add("suggestion-item");

                option.addEventListener("click", function () {
                    input.value = item.value;
                    suggestionBox.style.display = "none";
                });

                suggestionBox.appendChild(option);
            });

            suggestionBox.style.display =
                suggestions.length > 0 ? "block" : "none";

        } catch (error) {
            console.error("Suggestion error:", error);
        }
    });

    // Close suggestions when clicking outside
    document.addEventListener("click", function (event) {
        if (
            !input.contains(event.target) &&
            !suggestionBox.contains(event.target)
        ) {
            suggestionBox.style.display = "none";
        }
    });
}

setupAutocomplete("source", "source-suggestions");
setupAutocomplete("destination", "destination-suggestions");


// FIND ROUTE
document.getElementById("route-form").addEventListener(
    "submit",
    async function (event) {

        event.preventDefault();

        const source = document.getElementById("source").value.trim();
        const destination = document.getElementById("destination").value.trim();

        const resultBox = document.getElementById("result");

        resultBox.textContent = "Finding the shortest route...";

        try {
            const response = await fetch("/find-route", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    source: source,
                    destination: destination
                })
            });

            const data = await response.json();

            if (!response.ok) {
                resultBox.textContent = data.error;
                return;
            }

            resultBox.innerHTML = "";

const heading = document.createElement("h3");
heading.textContent = "Your Route";
resultBox.appendChild(heading);

const routeContainer = document.createElement("div");
routeContainer.classList.add("route-timeline");

data.route.forEach((location, index) => {

    const step = document.createElement("div");
    step.classList.add("route-step");

    const marker = document.createElement("div");
    marker.classList.add("route-marker");

    if (index === 0) {
        marker.textContent = "S";
        marker.classList.add("start-marker");
    } 
    else if (index === data.route.length - 1) {
        marker.textContent = "D";
        marker.classList.add("destination-marker");
    } 
    else {
        marker.textContent = index;
    }

    const name = document.createElement("span");
    name.textContent = location;

    step.appendChild(marker);
    step.appendChild(name);

    routeContainer.appendChild(step);
});

    resultBox.appendChild(routeContainer);

    const distance = document.createElement("p");
    distance.classList.add("total-distance");
    distance.textContent =
        `Total Distance: ${data.distance} metres`;

    resultBox.appendChild(distance);

        } catch (error) {
            resultBox.textContent =
                "Something went wrong. Please try again.";

            console.error("Route error:", error);
        }
    }
);
// POPULAR DESTINATION SELECTION


// POPULAR DESTINATION SELECTION
let selectedDestination = "";
const destinationCards = document.querySelectorAll(
    ".destination-card"
);

const modal = document.getElementById("location-modal");
const modalTitle = document.getElementById("modal-title");

destinationCards.forEach(card => {

    card.addEventListener("click", function () {

        // Get the selected destination
        const destination = card.dataset.destination;
        selectedDestination = destination;
        // Update popup heading
        modalTitle.textContent = `Navigate to ${destination}`;

        // Display the popup
        modal.style.display = "flex";

    });

});
// CLOSE POPUP

const closeModal = document.getElementById("close-modal");

// Close when clicking the X button
closeModal.addEventListener("click", function () {
    modal.style.display = "none";
});
// Close when clicking outside the popup

modal.addEventListener("click", function (event) {

    if (event.target === modal) {
        modal.style.display = "none";
    }

});

// MANUAL NAVIGATION

const chooseManually = document.getElementById("choose-manually");

chooseManually.addEventListener("click", function () {

    // Close the popup
    modal.style.display = "none";

    // Fill the selected destination
    const destinationInput = document.getElementById("destination");
    destinationInput.value = selectedDestination;

    // Scroll to the manual navigation section
    document.getElementById("manual-navigation-section")
        .scrollIntoView({ behavior: "smooth" });

});
