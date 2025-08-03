// Cargar provincias desde tu API Django
fetch('/proyecto/api/provincias/')
    .then(response => response.json())
    .then(provincias => {
        const select = document.getElementById('provincia-select');
        provincias.forEach(p => {
            const option = document.createElement('option');
            option.value = p.id;
            option.textContent = p.name;
            select.appendChild(option);
        });
    });

const proyectosDB = {
    // Aquí simulo proyectos, en la práctica deberías traerlos desde tu backend Django
    1: [{id: 101, nombre: "Proyecto Azuay", lat: -2.90055, lng: -79.00472}],
    16: [{id: 102, nombre: "Proyecto Pichincha", lat: -0.18065, lng: -78.46783}],
    9: [{id: 103, nombre: "Proyecto Guayas", lat: -2.17099, lng: -79.92236}]
};

const proyectosList = document.getElementById('proyectos-list');
const map = L.map('map').setView([-1.831239, -78.183406], 6);  // Centro Ecuador

// Agregar capa base OpenStreetMap
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; OpenStreetMap contributors'
}).addTo(map);

let markers = [];

function clearMarkers() {
    markers.forEach(m => map.removeLayer(m));
    markers = [];
}

document.getElementById('provincia-select').addEventListener('change', function() {
    const provinciaId = this.value;
    proyectosList.innerHTML = '';
    clearMarkers();

    if (provinciaId && proyectosDB[provinciaId]) {
        proyectosDB[provinciaId].forEach(proyecto => {
            // Mostrar proyectos en la lista
            const div = document.createElement('div');
            div.textContent = proyecto.nombre;
            proyectosList.appendChild(div);

            // Añadir marcador en el mapa
            const marker = L.marker([proyecto.lat, proyecto.lng]).addTo(map)
                .bindPopup(proyecto.nombre);
            markers.push(marker);

            // Centrar mapa en el proyecto (podrías ajustar si hay varios)
            map.setView([proyecto.lat, proyecto.lng], 10);
        });
    }
});
