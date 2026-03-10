// ERRM — Main JavaScript

document.addEventListener('DOMContentLoaded', () => {

  // ========================
  // NAVBAR : Scroll effect
  // ========================
  const navbar = document.querySelector('.navbar');
  if (navbar) {
    window.addEventListener('scroll', () => {
      navbar.classList.toggle('scrolled', window.scrollY > 50);
    });
  }

  // ========================
  // BURGER MENU
  // ========================
  const burger = document.querySelector('.burger');
  const mobileMenu = document.querySelector('.mobile-menu');
  if (burger && mobileMenu) {
    burger.addEventListener('click', () => {
      burger.classList.toggle('open');
      mobileMenu.classList.toggle('open');
    });
    // Close on link click
    mobileMenu.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        burger.classList.remove('open');
        mobileMenu.classList.remove('open');
      });
    });
  }

  // ========================
  // ACTIVE NAV LINK
  // ========================
  const currentPath = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.navbar-links a, .mobile-menu a').forEach(link => {
    const linkPath = link.getAttribute('href');
    if (linkPath === currentPath) {
      link.classList.add('active');
    }
  });

  // ========================
  // REVEAL ON SCROLL
  // ========================
  const revealElements = document.querySelectorAll('.reveal');
  if (revealElements.length > 0) {
    const revealObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          revealObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });

    revealElements.forEach(el => revealObserver.observe(el));
  }

  // ========================
  // COUNTER ANIMATION (hero stats)
  // ========================
  const counters = document.querySelectorAll('[data-count]');
  if (counters.length > 0) {
    const counterObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const el = entry.target;
          const target = parseInt(el.getAttribute('data-count'));
          const suffix = el.getAttribute('data-suffix') || '';
          const duration = 1800;
          const start = performance.now();

          function animate(now) {
            const elapsed = now - start;
            const progress = Math.min(elapsed / duration, 1);
            const eased = 1 - Math.pow(1 - progress, 3);
            el.textContent = Math.round(eased * target) + suffix;
            if (progress < 1) requestAnimationFrame(animate);
          }

          requestAnimationFrame(animate);
          counterObserver.unobserve(el);
        }
      });
    }, { threshold: 0.5 });

    counters.forEach(el => counterObserver.observe(el));
  }

  // ========================
  // LIGHTBOX (réalisations)
  // ========================
  const lightbox = document.querySelector('.lightbox');
  const lightboxImg = document.querySelector('.lightbox-img');
  const lightboxClose = document.querySelector('.lightbox-close');

  if (lightbox && lightboxImg) {
    document.querySelectorAll('[data-lightbox]').forEach(item => {
      item.addEventListener('click', () => {
        const src = item.getAttribute('data-lightbox');
        lightboxImg.src = src;
        lightbox.classList.add('active');
        document.body.style.overflow = 'hidden';
      });
    });

    function closeLightbox() {
      lightbox.classList.remove('active');
      document.body.style.overflow = '';
      lightboxImg.src = '';
    }

    if (lightboxClose) lightboxClose.addEventListener('click', closeLightbox);
    lightbox.addEventListener('click', (e) => {
      if (e.target === lightbox) closeLightbox();
    });
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') closeLightbox();
    });
  }

  // ========================
  // CONTACT FORM (AJAX Formspree)
  // ========================
  const contactForm = document.querySelector('#contact-form');
  if (contactForm) {
    contactForm.addEventListener('submit', async (e) => {
      e.preventDefault();

      const btn = contactForm.querySelector('button[type="submit"]');
      const originalHTML = btn.innerHTML;

      // État de chargement
      btn.textContent = 'Envoi en cours...';
      btn.disabled = true;

      const formData = new FormData(contactForm);

      try {
        const response = await fetch(contactForm.action, {
          method: contactForm.method,
          body: formData,
          headers: {
            'Accept': 'application/json'
          }
        });

        if (response.ok) {
          // Succès
          btn.textContent = 'Message envoyé ✓';
          btn.style.background = '#1E6B1E';
          contactForm.reset();
        } else {
          // Erreur Formspree
          const data = await response.json();
          if (Object.hasOwn(data, 'errors')) {
            btn.textContent = data.errors.map(error => error.message).join(", ");
          } else {
            btn.textContent = 'Erreur lors de l\'envoi';
          }
          btn.style.background = 'var(--rouge)';
        }
      } catch (error) {
        // Erreur réseau
        btn.textContent = 'Erreur de connexion';
        btn.style.background = 'var(--rouge)';
      }

      // Restauration du bouton après 4 secondes
      setTimeout(() => {
        btn.innerHTML = originalHTML;
        btn.disabled = false;
        btn.style.background = '';
      }, 4000);
    });
  }

  // ========================
  // FILTER GALLERY BY URL
  // ========================
  const urlParams = new URLSearchParams(window.location.search);
  const filterCat = urlParams.get('filter');
  if (filterCat) {
    const galleryItems = document.querySelectorAll('.gallery-page-item');
    if (galleryItems.length > 0) {
      // Modifier le label et le titre principal
      const tempLabel = document.querySelector('.section-label.reveal');
      if (tempLabel) tempLabel.textContent = `Portfolio filtré : ${filterCat}`;

      const pageTitle = document.querySelector('.page-hero h1');
      if (pageTitle) pageTitle.textContent = filterCat;

      // Filtrer les éléments
      galleryItems.forEach(item => {
        const catSpan = item.querySelector('.gallery-page-overlay span');
        if (catSpan && !catSpan.textContent.toLowerCase().includes(filterCat.toLowerCase())) {
          item.style.display = 'none';
        }
      });
      // Scroll vers la galerie
      const gallerySection = document.querySelector('.gallery-page-grid');
      if (gallerySection) {
        setTimeout(() => {
          gallerySection.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }, 300);
      }
    }
  }

});
