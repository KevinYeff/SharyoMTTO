//icono hamburguesa

document.addEventListener('DOMContentLoaded', function () {
    const toggleButton = document.querySelector('.toggle');
    const navMenu = document.querySelector('nav ul');

    toggleButton.addEventListener('click', function () {
        navMenu.classList.toggle('show');
    });
});
