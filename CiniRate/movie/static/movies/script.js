// Auto-hide alert messages after 3 seconds
document.addEventListener('DOMContentLoaded', function () {
    const alerts = document.querySelectorAll('.alert-dismissible');
    alerts.forEach(function (alert) {
        setTimeout(function () {
            alert.classList.remove('show');
            setTimeout(function () { alert.remove(); }, 300);
        }, 3000);
    });

    // Show stars next to the rating dropdown when the user picks a value
    const ratingSelect = document.querySelector('#id_rating');
    const preview = document.querySelector('#rating-preview');
    if (ratingSelect && preview) {
        const update = function () {
            const value = parseInt(ratingSelect.value) || 0;
            preview.textContent = '★'.repeat(value) + '☆'.repeat(5 - value);
        };
        ratingSelect.addEventListener('change', update);
        update();
    }
});