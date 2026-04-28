import { fetchMovies } from "./api.js";

const recentSlider = document.querySelector(".carousel-slider");
const resultsSlider = document.getElementById("results-slider");
const resultsTitle = document.getElementById("results-title");

//filter button click, genre and rating dropdowns showing
const btn = document.querySelector(".filter-btn");
const menu = document.querySelector(".filter-menu");
btn.addEventListener("click", () => {
    menu.style.display = menu.style.display === "block" ? "none" : "block";
});
window.toggleMenu = function(id) {
    const el = document.getElementById(id);
    el.style.display =
        el.style.display === "block" ? "none" : "block";
}

const clearBtn = document.getElementById("clear-btn");
clearBtn.addEventListener("click", () => {
    // clear input
    document.querySelector('input[type="search"]').value = "";
    // reset filters
    selectedGenre = '';
    selectedRating = '';
    // hide results
    resultsTitle.style.display = "none";
    resultsSlider.innerHTML = "";
    // reset pagination
    currentPage = 1;
    // reload recent carousel
    loadMovies(`${recentUrl}&page=1`, recentSlider);
});
//infinite automatic carousel
/*const movies = [
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
]*/
/*const newMovies = movies.concat(movies)
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
});*/

//cards creating and pagination
let currentPage = 1;
const limit = 10;
let recentUrl = `http://127.0.0.1:8000/getall?limit=${limit}`;
let resultsUrl = "";
function loadMovies(url, targetSlider){
    fetchMovies(url).then(data => {
        targetSlider.innerHTML = "";
        if (!data || data.length === 0){
            targetSlider.innerHTML = "<p>No movies found</p>";
            return;
        }
        let moviesToRender = data;
        //only for carousel
        if (targetSlider === recentSlider) {
            moviesToRender = [...data, ...data]; // duplicate twice for infinite scroll
        }
        moviesToRender.forEach(element => {
            const card = document.createElement("div");
            card.className = "movie-card-mini";

            card.innerHTML = `
               <img src="assets/images/${element.image_url}">
               <div class="card-info">
                   <span class="rating">⭐ ${element.rating}</span>
                   <h4>${element.title}</h4>
               </div>
            `;
            targetSlider.appendChild(card);
        });
        if (targetSlider === recentSlider) {
            recentSlider.scrollLeft = 0;
        }
    });
}
loadMovies(`${recentUrl}&page=1`, recentSlider);
document.getElementById("next").addEventListener("click", () => {
    currentPage++;
    if (resultsTitle.style.display === "block") {
        loadMovies(`${resultsUrl}&page=${currentPage}`, resultsSlider);
    } else {
        loadMovies(`${recentUrl}&page=${currentPage}`, recentSlider);
    }
});
document.getElementById("prev").addEventListener("click", () => {
    if (currentPage > 1){
        currentPage--;
        if (resultsTitle.style.display === "block") {
            loadMovies(`${resultsUrl}&page=${currentPage}`, resultsSlider);
        } else {
            loadMovies(`${recentUrl}&page=${currentPage}`, recentSlider);
        }
    }
});

//infinte carousel
let scrollAmount = 0
function autoScroll() {
    if (!recentSlider) return;
    recentSlider.scrollLeft += 1;
    const cards = recentSlider.querySelectorAll(".movie-card-mini");
    if (cards.length === 0) return;
    const originalLength = Math.floor(cards.length / 2);
    const firstDuplicate = cards[originalLength];
    if (recentSlider.scrollLeft >= firstDuplicate.offsetLeft) {
        recentSlider.scrollLeft -= firstDuplicate.offsetLeft;
    }
}
setInterval(autoScroll,27)


function buildUrl() {
    let url = `http://127.0.0.1:8000/getall?limit=${limit}`;
    const searchInput = document.querySelector('input[type="search"]').value;
    if (searchInput) {
        url += `&name=${searchInput}`;
    }
    if (selectedGenre) {
        url += `&genre=${selectedGenre}`;
    }
    if (selectedRating) {
        url += `&rating=${selectedRating}`;
    }
    console.log("selectedRating:", selectedRating);
    console.log("final URL:", url);
    return url;
}

//capturing user input
const forms = document.querySelector('.search-form')
forms.addEventListener("submit",formSubmitted)
function formSubmitted(event){
    event.preventDefault()
    const searchInput = document.querySelector('input[type="search"]').value;
    currentPage = 1;
    resultsUrl = buildUrl();
    resultsTitle.style.display = "block";
    loadMovies(`${resultsUrl}&page=${currentPage}`, resultsSlider);
}
let selectedGenre = '';
let selectedRating = '';
let genrevar = document.querySelectorAll('#genre-menu p')
let ratingvar = document.querySelectorAll('#rating-menu p')
genrevar.forEach(e =>{
    e.addEventListener("click", ()=>{
        selectedGenre = e.textContent.trim();
        menu.style.display = "none";
        currentPage = 1;
        resultsUrl = buildUrl();
        resultsTitle.style.display = "block";
        loadMovies(`${resultsUrl}&page=${currentPage}`, resultsSlider);
    })
});
ratingvar.forEach(el =>{
    el.addEventListener('click',()=>{
        selectedRating = parseFloat(el.textContent.replace(/[^0-9.]/g, ""));
        menu.style.display = "none";
        currentPage = 1;
        resultsUrl = buildUrl();
        resultsTitle.style.display = "block";
        loadMovies(`${resultsUrl}&page=${currentPage}`, resultsSlider);
    })
});