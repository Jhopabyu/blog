document.addEventListener('DOMContentLoaded', function () {
    const btnSubir = document.getElementById('btnSubir');

    if (btnSubir) {
      window.addEventListener('scroll', function () {
        if (window.scrollY > 200) {
          btnSubir.style.display = 'block';
        } else {
          btnSubir.style.display = 'none';
        }
      });

      btnSubir.addEventListener('click', function () {
        window.scrollTo({
          top: 0,
          behavior: 'smooth'
        });
      });
    }
  });