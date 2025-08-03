let provinciasData = {};
fetch('/proyecto/api/provincias/')
  .then(response => response.json())
  .then(provincias => {
    const select = document.getElementById('provincia-select');
    provincias.forEach(p => {
      provinciasData[p.id] = p;
      const option = document.createElement('option');
      option.value = p.id;
      option.textContent = p.name;
      select.appendChild(option);
    });
  });

const proyectosItems = document.getElementById('proyectos-items');
const detalleDiv = document.getElementById('detalle-proyecto');
const detalleContainer = document.getElementById('detalle-container');

const map = L.map('map').setView([-1.831239, -78.183406], 6);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; OpenStreetMap contributors'
}).addTo(map);

let markers = [];

function clearMarkers() {
  markers.forEach(m => map.removeLayer(m));
  markers = [];
}

document.getElementById('provincia-select').addEventListener('change', function () {
  const provinciaID = this.value;
  
  proyectosItems.innerHTML = '';
  detalleDiv.innerHTML = '';
  detalleContainer.classList.remove('show');
  detalleContainer.style.display = 'none';
  clearMarkers();

  if (!provinciaID) return;

  // 💡 CENTRAR EL MAPA EN LA PROVINCIA
  const provincia = provinciasData[provinciaID];
  if (provincia && provincia.lat && provincia.lng) {
    map.setView([provincia.lat, provincia.lng], 8);
  }

  fetch(`/proyecto/api/proyectos/${provinciaID}/`)
    .then(response => response.json())
    .then(proyectos => {
      if (proyectos.length === 0) {
        proyectosItems.innerHTML = '<p>No hay proyectos registrados en esta provincia.</p>';
      } else {
        proyectos.forEach(p => {
          const item = document.createElement('div');
          item.className = 'my-2';
          item.innerHTML = `<a href="#" class="text-primary fw-bold" data-id="${p.id}">${p.nombre}</a>`;
          item.querySelector('a').addEventListener('click', function (e) {
            e.preventDefault();
            mostrarDetalle(p);
          });
          proyectosItems.appendChild(item);

          if (p.lat && p.lon) {
            const marker = L.marker([p.lat, p.lon]).addTo(map).bindPopup(p.nombre);
            markers.push(marker);
          }
        });

        const primer = proyectos.find(p => p.lat && p.lon);
        if (primer) {
          map.setView([primer.lat, primer.lon], 8);
        }
      }
    });
});

function mostrarDetalle(p) {
  detalleDiv.innerHTML = `
    <h5>${p.nombre}</h5>
    <p><strong>Estado:</strong> ${p.estado}</p>
    <p><strong>País:</strong> ${p.pais}</p>
    <p><strong>Provincia:</strong> ${p.provincia}</p>
    <p><strong>Costo:</strong> $${p.costo}</p>
    <p><strong>Equipo:</strong> ${p.equipo}</p>
    <p><strong>Fecha de Aprobación:</strong> ${p.f_aprobacion}</p>
    <p><strong>Última Actualización:</strong> ${p.f_actualizacion}</p>
  `;
  detalleContainer.style.display = 'block';
  setTimeout(() => {
    detalleContainer.classList.add('show');
  }, 10);
}
