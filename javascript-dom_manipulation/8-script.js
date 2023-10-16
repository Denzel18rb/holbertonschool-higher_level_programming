document.addEventListener('DOMContentLoaded', function () {

    const helloElement = document.getElementById('hello');

    const apiUrl = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        const translation = data.hello;

        helloElement.textContent = translation;
      })
      .catch(error => {
        console.error('Error:', error);
        helloElement.textContent = 'Error fetching translation';
      });
});
  