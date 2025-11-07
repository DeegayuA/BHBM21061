const themeToggleButton = document.getElementById('theme-toggle');
const bodyelement = document.body;

function toggleDarkMode() {
    bodyelement.classList.toggle('dark-mode');
    themeToggleButton.classList.toggle('active');
}

themeToggleButton.addEventListener('click', toggleDarkMode);
// --- IGNORE ---