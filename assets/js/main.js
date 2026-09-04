/* ===================================================
   EspunyDesign — Main JavaScript
   Static per-language pages (/, /ca/, /en/) — no client-side
   i18n switching needed, just UI behaviour.
   - Header scroll state
   - Mobile nav toggle
   - Active section tracking
   - Scroll-reveal animations
   - Project modals
   - Secondary gallery lightbox
   - Smooth scroll
   - Contact form feedback
   =================================================== */

document.addEventListener('DOMContentLoaded', () => {

    // --- Header scroll effect ---
    const header = document.getElementById('header');

    function updateHeader() {
        if (!header) return;
        if (window.scrollY > 60) {
            header.classList.add('header--scrolled');
        } else {
            header.classList.remove('header--scrolled');
        }
    }

    window.addEventListener('scroll', updateHeader, { passive: true });
    updateHeader();

    // --- Mobile navigation toggle ---
    const navToggle = document.getElementById('nav-toggle');
    const navMenu = document.getElementById('nav-menu');
    const navLinks = document.querySelectorAll('.nav__link');

    if (navToggle && navMenu) {
        navToggle.addEventListener('click', () => {
            navToggle.classList.toggle('active');
            navMenu.classList.toggle('open');
            document.body.classList.toggle('modal-open');
        });

        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                navToggle.classList.remove('active');
                navMenu.classList.remove('open');
                document.body.classList.remove('modal-open');
            });
        });
    }

    // --- Active nav link on scroll ---
    const sections = document.querySelectorAll('.section');

    function updateActiveNav() {
        const scrollY = window.scrollY + window.innerHeight / 3;

        sections.forEach(section => {
            const top = section.offsetTop;
            const height = section.offsetHeight;
            const id = section.getAttribute('id');

            if (scrollY >= top && scrollY < top + height) {
                navLinks.forEach(link => {
                    link.classList.remove('active');
                    if (link.getAttribute('data-section') === id) {
                        link.classList.add('active');
                    }
                });
            }
        });
    }

    window.addEventListener('scroll', updateActiveNav, { passive: true });
    updateActiveNav();

    // --- Scroll reveal animations ---
    const revealElements = document.querySelectorAll(
        '.section__title, .section__subtitle, .project-card, .service-block, .about__content, .contact__info, .contact__form, .more-work__item'
    );

    revealElements.forEach(el => el.classList.add('reveal'));

    if ('IntersectionObserver' in window) {
        const revealObserver = new IntersectionObserver(
            (entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('revealed');
                        revealObserver.unobserve(entry.target);
                    }
                });
            },
            { threshold: 0.15, rootMargin: '0px 0px -40px 0px' }
        );

        revealElements.forEach(el => revealObserver.observe(el));
    } else {
        revealElements.forEach(el => el.classList.add('revealed'));
    }

    // --- Staggered reveal for grids ---
    const staggerContainers = document.querySelectorAll('.projects__grid, .services__grid, .more-work__grid');
    staggerContainers.forEach(container => {
        const children = container.querySelectorAll('.reveal');
        children.forEach((child, index) => {
            child.style.transitionDelay = `${index * 0.08}s`;
        });
    });

    // --- Generic modal open/close helpers ---
    function openModal(modal) {
        if (!modal) return;
        modal.classList.add('active');
        modal.setAttribute('aria-hidden', 'false');
        document.body.classList.add('modal-open');
        const closeBtn = modal.querySelector('.modal__close');
        if (closeBtn) setTimeout(() => closeBtn.focus(), 100);
    }

    function closeModal(modal) {
        if (!modal) return;
        modal.classList.remove('active');
        modal.setAttribute('aria-hidden', 'true');
        document.body.classList.remove('modal-open');
    }

    function closeAllModals() {
        document.querySelectorAll('.modal').forEach(m => closeModal(m));
    }

    function attachCardOpen(card, modal) {
        if (!card || !modal) return;
        card.addEventListener('click', () => openModal(modal));
        card.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                openModal(modal);
            }
        });
    }

    // --- Project cards & modals ---
    document.querySelectorAll('.project-card[data-modal]').forEach(card => {
        const modal = document.getElementById(card.getAttribute('data-modal'));
        attachCardOpen(card, modal);
    });

    document.querySelectorAll('[data-close-modal]').forEach(el => {
        el.addEventListener('click', closeAllModals);
    });

    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') closeAllModals();
    });

    // --- Secondary gallery lightbox ---
    const lightbox = document.getElementById('lightbox');
    const lightboxImg = lightbox ? lightbox.querySelector('.lightbox__img') : null;
    const lightboxCaption = lightbox ? lightbox.querySelector('.lightbox__caption') : null;

    document.querySelectorAll('.more-work__item').forEach(item => {
        item.addEventListener('click', () => {
            if (!lightbox || !lightboxImg) return;
            const fullSrc = item.getAttribute('data-full') || item.querySelector('img').src;
            const name = item.getAttribute('data-name') || '';
            lightboxImg.src = fullSrc;
            lightboxImg.alt = name;
            if (lightboxCaption) lightboxCaption.textContent = name;
            openModal(lightbox);
        });
        item.setAttribute('tabindex', '0');
        item.setAttribute('role', 'button');
        item.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                item.click();
            }
        });
    });

    // --- Smooth scroll for CTA button ---
    const ctaButton = document.getElementById('hero-cta-projects');
    if (ctaButton) {
        ctaButton.addEventListener('click', (e) => {
            const href = ctaButton.getAttribute('href');
            if (href && href.startsWith('#')) {
                e.preventDefault();
                const target = document.querySelector(href);
                if (target) target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    }

    // --- Smooth scroll for in-page anchor links ---
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const href = this.getAttribute('href');
            if (!href || href === '#') return;
            const target = document.querySelector(href);
            if (target) {
                e.preventDefault();
                const offset = parseInt(getComputedStyle(document.documentElement).getPropertyValue('--header-height')) || 72;
                const top = target.getBoundingClientRect().top + window.scrollY - offset;
                window.scrollTo({ top, behavior: 'smooth' });
            }
        });
    });

    // --- Contact form submit feedback ---
    const form = document.getElementById('contact-form');
    if (form) {
        form.addEventListener('submit', function () {
            const submitBtn = document.getElementById('form-submit');
            if (submitBtn) {
                const sendingText = submitBtn.getAttribute('data-sending-text');
                if (sendingText) submitBtn.textContent = sendingText;
                submitBtn.style.opacity = '0.6';
                submitBtn.style.pointerEvents = 'none';
            }
        });
    }

});
