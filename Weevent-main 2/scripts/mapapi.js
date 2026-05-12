"use strict";

document.addEventListener("DOMContentLoaded", function() {
    var map = L.map('map').setView([55.8642, -4.2518], 13);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);
});
