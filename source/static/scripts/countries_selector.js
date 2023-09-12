  var inputText = document.getElementsByClassName("input-text")[0];

  function getInputText() {
    return inputText.value;
  }

  function getCountries() {
    return document.querySelectorAll(".dropdown-content li");
  }

  function getCountryName(country) {
    return country.innerText;
  }

  function compareCountryNameWithInput(country, input) {
    return country.toLowerCase().startsWith(input.toLowerCase());
  }

  function filterOutCountries(countries, text) {
    let filtered_countries = [];
    for (let i = 0; i < countries.length; i++) {
      if (!compareCountryNameWithInput(getCountryName(countries[i]), text)) {
        filtered_countries.push(countries[i]);
      }
    }
    return filtered_countries;
  }

  function showCountries(countries) {
    countries.forEach((country) => {
      country.classList.remove("hidden");
    });
  }

  function hideCountries(countries) {
    countries.forEach((country) => {
      country.classList.add("hidden");
    });
  }

  function renderCountries() {
    // Firts, show all countries then hide these countries which don't match searched pattern
    let countries = getCountries();
    let input = getInputText();
    showCountries(countries);
    let filtered_countries = filterOutCountries(countries, input);
    hideCountries(filtered_countries);
  }

document.addEventListener("keyup", renderCountries);