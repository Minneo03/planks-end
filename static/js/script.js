let slides = [
  "static/images/amusements/Krakens Curse.png",
  "static/images/amusements/Swash Buckler.png",
  "static/images/amusements/Pirate's Plunder.png",
  "static/images/amusements/Buccaneer's Blitz.png",
  "static/images/amusements/Cannonball Express.png"
];

let currentSlide = 0;

function nextSlide() {
  currentSlide = (currentSlide + 1) % slides.length;
  document.getElementById('slideshowImg').src = slides[currentSlide];
}

function prevSlide() {
  currentSlide = (currentSlide - 1 + slides.length) % slides.length;
  document.getElementById('slideshowImg').src = slides[currentSlide];
}
