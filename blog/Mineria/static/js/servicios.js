document.addEventListener('DOMContentLoaded', function () {
  const modal = new bootstrap.Modal(document.getElementById('servicioModal'));
  const modalTitle = document.getElementById('servicioModalLabel');
  const modalDescription = document.getElementById('modal-description');

  const descripciones = {
    'GEOLOGÍA Y EVALUACION DE RECURSOS': `
      <h1>Tenemos para Ofrecerte</h1>
      <ul>
        <li><i class="bi bi-tools text-warning me-2"></i>Procesamiento de bases de datos geológicas / mineras</li>
        <li><i class="bi bi-diagram-3 text-primary me-2"></i>Interpretación, modelización geológica en 3D</li>
        <li><i class="bi bi-graph-up-arrow text-success me-2"></i>Estimación de recursos</li>
        <li><i class="bi bi-check-circle text-info me-2"></i>Control y Garantía de Calidad (QA-QC)</li>
        <li><i class="bi bi-binoculars text-danger me-2"></i>Exploración Minera: Planificación, supervisión & control</li>
        <li><i class="bi bi-bar-chart-line text-secondary me-2"></i>Análisis estadístico / geoestadístico</li>
        <li>⛏️ Desarrollo y control de Operaciones mineras (cielo abierto / subterráneas)</li>
        <li>💰 Evaluación económica de proyectos mineros</li>
        <li>📝 Informes de Exploración, Producción</li>
        <li>📂 Gestión de administración y cumplimiento de concesiones Mineras</li>
      </ul>
    `,
    'INGENIERÍA DE MINAS': `
      <ul>
        <li>Diseño, optimización y operación de minas a cielo abierto / subterráneas</li>
        <li>Evaluación de costos de capital y de operación (Capex/Opex)</li>
        <li>Optimización de producción de mina y planta de beneficio</li>
      </ul>  
    `,
    'DISEÑO': 'Creamos diseños atractivos y funcionales para tus proyectos.',
    'CREATIVIDAD': 'Innovamos con creatividad para soluciones únicas y efectivas.'
  };

  document.querySelectorAll('.servicio-card').forEach(card => {
    card.addEventListener('click', function () {
      const servicio = this.getAttribute('data-servicio')?.trim();
      console.log("Servicio clickeado:", servicio);  // para debug
      modalTitle.textContent = servicio;

      if (descripciones[servicio]) {
        modalDescription.innerHTML = descripciones[servicio];
      } else {
        modalDescription.textContent = 'Descripción no disponible.';
      }

      modal.show();
    });
  });
});

