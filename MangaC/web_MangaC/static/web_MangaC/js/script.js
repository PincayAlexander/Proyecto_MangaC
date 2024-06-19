function redirectToPDF(button, url, listItem) {
    if (url) {
        button.classList.add('button__clicked');
        vistoPDF(listItem);
        window.open(url, '_blank').focus();
    }
}

function vistoPDF(listItem) {
    let icon = listItem.querySelector('.fa-eye-slash');
    if (icon != null) {
        icon.classList.remove('fa-eye-slash');
        icon.classList.add('fa-eye');
        icon.style.color = 'blue';
    }
}