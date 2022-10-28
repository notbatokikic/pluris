
const toggleButton = document.getElementsByClassName('toggle-button')[0]
const navbarLinks = document.getElementsByClassName('navbar-links-mobile')[0]
const arrowButton = document.getElementsByClassName('arrow-container')[0]

toggleButton.addEventListener('click', () => {
navbarLinks.classList.toggle('active');
})

toggleButton.addEventListener('click', () => {
    toggleButton.classList.toggle('is-active');
})

toggleButton.addEventListener('click', () => {
    arrowButton.classList.toggle('active');
})


