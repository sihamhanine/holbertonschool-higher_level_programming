document.addEventListener("DOMContentLoaded", function () {
    const btnTranslate = document.getElementById('btn_translate');
    
    btnTranslate.addEventListener('click', function () {
      const langCode = document.getElementById('language_code').value;
      const url = `https://hellosalut.stefanbohacek.dev/?lang=${langCode}`;
      
      fetch(url)
        .then(response => response.json())
        .then(data => {
          document.getElementById('hello').textContent = data.hello;
        })
        .catch(error => console.error('Error:', error));
    });
  });
