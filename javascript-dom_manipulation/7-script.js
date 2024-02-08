document.addEventListener("DOMContentLoaded", function () {
    const movieList = document.getElementById("list_movies");

    const apiUrl = "https://swapi-api.hbtn.io/api/films/?format=json";

    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        return response.json();
      })
      .then(data => {
        const movies = data.results;

        movies.forEach(movie => {
          const listItem = document.createElement("li");
          listItem.textContent = movie.title;
          movieList.appendChild(listItem);
        });
      })
      .catch(error => {
        console.error("Error:", error);
        movieList.textContent = "Error fetching data";
      });
});
