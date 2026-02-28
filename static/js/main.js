document.addEventListener('DOMContentLoaded', () => {
    // Nav Scroll
    const nav = document.querySelector('nav');
    window.addEventListener('scroll', () => {
        if (nav) {
            if (window.scrollY > 100) nav.classList.add('scrolled');
            else nav.classList.remove('scrolled');
        }
    });

    // Reveal on Scroll
    const reveals = document.querySelectorAll('.reveal-up');
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
            }
        });
    }, { threshold: 0.1 });

    reveals.forEach(el => observer.observe(el));

    // Modal Operations
    const modal = document.getElementById('booking-modal-overlay');
    const formContainer = document.getElementById('booking-form-container');
    const successCard = document.getElementById('confirmation-card');
    const closeModal = document.getElementById('close-modal');
    const doneBtn = document.getElementById('done-btn');
    const triggers = document.querySelectorAll('.booking-trigger');

    if (modal && formContainer && successCard) {
        triggers.forEach(btn => {
            btn.addEventListener('click', (e) => {
                const cat = e.currentTarget.dataset.category;
                const serv = e.currentTarget.dataset.service;
                
                const catInput = document.querySelector('input[name="category"]');
                const servInput = document.querySelector('input[name="service"]');
                if (catInput) catInput.value = cat;
                if (servInput) servInput.value = serv;
                
                const title = document.getElementById('modal-category-title');
                if (title) title.innerHTML = `${cat.split(' ')[0]} <span>${cat.split(' ')[1] || 'ACCESS'}</span>`;
                
                modal.classList.add('active');
                formContainer.style.display = 'block';
                successCard.style.display = 'none';
            });
        });

        const hideModal = () => modal.classList.remove('active');
        if (closeModal) closeModal.addEventListener('click', hideModal);
        if (doneBtn) doneBtn.addEventListener('click', hideModal);
    }

    // Form Submission
    const form = document.getElementById('contact-form');
    if (form) {
        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            const btn = form.querySelector('button');
            const originalText = btn.innerHTML;
            btn.innerHTML = 'VALIDATING...';
            btn.disabled = true;

            const data = new FormData(form);
            try {
                const response = await fetch('/contact/submit/', {
                    method: 'POST',
                    body: data,
                    headers: { 'X-Requested-With': 'XMLHttpRequest' }
                });
                const res = await response.json();
                if (response.ok) {
                    const dateDisplay = document.getElementById('booking-date-display');
                    if (dateDisplay) dateDisplay.innerText = res.booking_date;
                    formContainer.style.display = 'none';
                    successCard.style.display = 'flex';
                    form.reset();
                } else {
                    alert('Please check your input.');
                }
            } catch (err) {
                alert('SYSTEM ERROR. RETRY.');
            } finally {
                btn.innerHTML = originalText;
                btn.disabled = false;
            }
        });
    }

    // Smooth Scrolling
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });
});
