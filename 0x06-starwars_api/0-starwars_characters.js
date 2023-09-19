#!/usr/bin/node
// This is the url we want to request data from 
let request = "https://swapi-api.alx-tools.com/api/"

// the function call to retrieve the data and display the page
fetch(request.then(response) => {
  return response.json();
}).then((data) => {
  let p = document.getElementById("text");
  console.log(data)
  p.innerHTML = JSON.stringify(data);
})
