document.addEventListener('DOMContentLoaded', function () {
    const rootElement = document.documentElement;
    const themeToggleBtnHeader = document.getElementById('themeToggleHeader');
    const themeToggleBtnPost = document.getElementById('themeTogglePost');
    const sunIcon = document.getElementById('sunIcon');
    const moonIcon = document.getElementById('moonIcon');
    const avatarImg = document.getElementById('avatarImg');

    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'dark') {
        rootElement.classList.add('dark-mode');
    }

    function updateIconsAndAvatar() {
        const isDark = rootElement.classList.contains('dark-mode');
        sunIcon.style.display = isDark ? 'inline-block' : 'none';
        moonIcon.style.display = isDark ? 'none' : 'inline-block';

        // Check if avatarImg exists
        if (avatarImg) {
            avatarImg.src = isDark
                ? '/assets/images/avatar_dark.jpg'
                : '/assets/images/avatar.jpg';
        } else {
            console.log('Avatar image element not found!');
        }
    }

    updateIconsAndAvatar();

    function toggleTheme() {
        rootElement.classList.toggle('dark-mode');
        if (rootElement.classList.contains('dark-mode')) {
            localStorage.setItem('theme', 'dark');
        } else {
            localStorage.setItem('theme', 'light');
        }
        updateIconsAndAvatar();
    }

    if (themeToggleBtnHeader) {
        themeToggleBtnHeader.addEventListener('click', toggleTheme);
    }

    if (themeToggleBtnPost) {
        themeToggleBtnPost.addEventListener('click', toggleTheme);
    }
});
