const events = document.getElementsByClassName("events")[0]
const events_button = document.getElementById("events-choice-button");
const squads = document.getElementsByClassName("squads-section")[0]
const squads_button = document.getElementById("squads-choice-button");


function squadsButtonEvent() {
    if (! squads_button.classList.contains("active-button")) {
        squads.classList.remove("hidden");
        events.classList.add("hidden");
        squads_button.classList.add("active-button");
        events_button.classList.remove("active-button");
    }
}

function eventsButtonEvent() {
    if (! events_button.classList.contains("active-button")) {
        events.classList.remove("hidden");
        squads.classList.add("hidden");
        events_button.classList.add("active-button");
        squads_button.classList.remove("active-button");
    }
}


events_button.addEventListener("click", eventsButtonEvent);
squads_button.addEventListener("click", squadsButtonEvent);