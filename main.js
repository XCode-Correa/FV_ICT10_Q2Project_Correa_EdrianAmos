// Q2 Project - GLOBAL JS //

// Copied for mass use in Projects //

const loader = document.getElementById('page-loader');
    // 1. Slide OUT when the page finishes loading
    window.addEventListener('load', () => {
        // Small delay so the user sees the logo briefly
        setTimeout(() => {
            loader.classList.add('slide-out');
        }, 500); 
});

// Fix for Safari/Firefox "Back" button showing a stuck screen
window.addEventListener('pageshow', (event) => {
    if (event.persisted) {
        loader.classList.add('slide-out');
    }
});

// 2. Slide IN when clicking internal links
document.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', (e) => {
        const href = link.getAttribute('href');
        // Ignore empty links, anchor jumps (#), external links, or new tabs
        if (
        !href ||
        href.startsWith('#') ||
        href.startsWith('mailto:') ||
        href.startsWith('tel:') ||
        link.target === '_blank' ||
        link.hostname !== window.location.hostname
        ) {
            return;
        }

        // Stop immediate navigation so the slide-in animation can play
        e.preventDefault();
        loader.classList.remove('slide-out');

        // Wait for the 1s CSS transition to finish, then change page
        setTimeout(() => {
            window.location.href = href;
        }, 1000);
    });
});