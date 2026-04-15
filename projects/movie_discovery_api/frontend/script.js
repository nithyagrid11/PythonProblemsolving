//filter button click, genre and rating dropdowns showing
const btn = document.querySelector(".filter-btn");
const menu = document.querySelector(".filter-menu");

btn.addEventListener("click", () => {
    menu.style.display = menu.style.display === "block" ? "none" : "block";
});

function toggleMenu(id) {
    const el = document.getElementById(id);

    el.style.display =
        el.style.display === "block" ? "none" : "block";
}

//infinite automatic carousel
const movies = [
    {name: "Project Hail Mary", rating:5, img:"images/project hail mary.jpg"},
    {name: "Ready or Not 2", rating:4, img:"images/ready or not 2.jpg"},
    {name: "Sinners", rating:4.5, img:"images/sinners.jpg"},
    {name: "Dhurandhar", rating:4.5, img:"images/dhurandhar.jpg"},
    {name: "The Drama", rating:3.5, img:"images/the drama.jpg"},
    {name: "Thrash", rating:3.5, img:"images/thrash.jpg"},
    {name: "You.Me & Tuscany", rating: 3.5, img:"images/tuscany.jpg"},
    {name: "Vazha2", rating:4.5, img:"images/vazha2.jpg"},
    {name: "PizzaMovie", rating:3.5, img:"images/pizza movie.jpg"},
    {name: "MarioGalaxy", rating:3.5, img:"images/mario galaxy.jpg"},
    {name: "Hoppers", rating:3.5, img:"images/hoppers.webp"}
]
const slider = document.querySelector(".carousel-slider")
const newMovies = movies.concat(movies)
newMovies.forEach(element => {
    const card = document.createElement("div");
    card.className = "movie-card-mini";
    card.innerHTML = `
       <img src="${element.img}">
       <div class="card-info">
          <span class="rating">⭐ ${element.rating}</span>
          <h4>${element.name}</h4>
        </div>
    `;
    slider.appendChild(card);
});
let scrollAmount = 0
function autoScroll(){
    scrollAmount += 1;
    slider.scrollLeft = scrollAmount;
    if (scrollAmount >= slider.scrollWidth/2) {
        scrollAmount = scrollAmount - (slider.scrollWidth/2)
    }
}
setInterval(autoScroll,27)

//search
const forms = document.querySelector('.search-form')
forms.window.addEventListener("submit",formSubmitted)
function formSubmitted(event){
    event.preventDefault()
    const searchInput = document.querySelector('input[type="search"]').value;
    console.log(searchInput);
}
const selectedGenre = ''
const selectedRating = 0
const elements = document.querySelectorAll('p')