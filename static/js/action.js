//useless for now
console.log("Hello, world!");

window.onload = function() {
  console.log("Hello, world!");

  const loaders = document.querySelectorAll('.container .loader');
  const image = document.querySelector('.container #Pic');

  console.log("Hello, world again!");

  image.addEventListener('load', function() {
    loaders.forEach(function(loader) {
      console.log("beep");
      loader.remove();
    });
  });
}




