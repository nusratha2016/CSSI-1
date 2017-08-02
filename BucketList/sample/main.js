function addListItem(text){
  list = document.querySelector('ul');
  item = document.createElement('li');
  item.innerText = text;
  list.appendChild(item);
}
addListItem("Chocolate")
addListItem("Water")
addListItem("Pineapples")
addListItem("Blueberries")

// Now use the function to add elements to the list!
