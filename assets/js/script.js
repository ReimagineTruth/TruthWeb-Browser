const menuButton = document.getElementById('menuButton');
const closeButton = document.getElementById('closeButton');
const menuDrawer = document.getElementById('menuDrawer');
const themeToggleButton = document.getElementById('theme-toggle');
const body = document.body;

const openModalButton = document.getElementById('openModalButton');
const closeModalButton = document.getElementById('closeModalButton');
const infoModal = document.getElementById('infoModal');

// Apply Theme
function applyTheme(theme) {
    body.setAttribute('data-theme', theme);
    localStorage.setItem('theme', theme);
}
applyTheme(localStorage.getItem('theme') || 'dark');

themeToggleButton.addEventListener('click', () => {
    const newTheme = body.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
    applyTheme(newTheme);
});

// URL Navigation
const urlBar = document.getElementById('url-bar');
const browserFrame = document.getElementById('browser-frame');

urlBar.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        const url = urlBar.value;
        browserFrame.src = url.startsWith('http') ? url : `https://www.google.com/search?q=${encodeURIComponent(url)}`;
    }
});
