document.addEventListener('DOMContentLoaded', function() {
  fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json())
  .then(data => {
    const filmList = document.getElementById('list_movies');
    data.results.forEach(film => {
      const li = document.createElement('li');
      li.textContent = film.title;
      filmList.appendChild(li);
    });
  })
  .catch(error => console.error('Error:', error));
});
