document.addEventListener('DOMContentLoaded', function() {
  const myList = document.getElementById('my_list');

  document.getElementById('add_item').addEventListener('click', function() {
    const newLi = document.createElement('li');
    newLi.textContent = 'Item';
    myList.appendChild(newLi);
  });

  document.getElementById('remove_item').addEventListener('click', function() {
    if (myList.lastElementChild) {
        myList.removeChild(myList.lastElementChild);
    }
  });

  document.getElementById('clear_list').addEventListener('click', function() {
    myList.innerHTML = '';
  });
  });
  