/* SUMMER LOCK-ON — interactions */

(function () {
  'use strict';

  const LINE_URL = window.getSummerLineUrl ? window.getSummerLineUrl() : '#';

  document.querySelectorAll('[data-line-cta]').forEach((el) => {
    el.href = LINE_URL;
  });

  const nav = document.getElementById('nav');
  const progress = document.getElementById('progress');
  const sticky = document.getElementById('stickyCta');

  function onScroll() {
    const y = window.scrollY;
    if (nav) nav.classList.toggle('is-scrolled', y > 24);
    if (progress) {
      const h = document.documentElement.scrollHeight - window.innerHeight;
      progress.style.width = Math.min(100, (y / h) * 100) + '%';
    }
    if (sticky) {
      const nearBottom = y > document.documentElement.scrollHeight - window.innerHeight - 400;
      sticky.classList.toggle('in', y > 500 && !nearBottom);
    }
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  const io = new IntersectionObserver((entries) => {
    entries.forEach((e) => {
      if (e.isIntersecting) {
        e.target.classList.add('in');
        io.unobserve(e.target);
      }
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -6% 0px' });

  document.querySelectorAll('.reveal, .reveal-up, .reveal-left, .reveal-right').forEach((el) => {
    io.observe(el);
  });

  document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('[data-seq]').forEach((el, i) => {
      setTimeout(() => el.classList.add('in'), 200 + i * 200);
    });
  });

  // Calendar accordion
  document.querySelectorAll('.cal-phase__head').forEach((head) => {
    head.addEventListener('click', () => {
      const body = head.nextElementSibling;
      const isOpen = head.getAttribute('aria-expanded') === 'true';
      head.setAttribute('aria-expanded', isOpen ? 'false' : 'true');
      if (body) body.classList.toggle('is-open', !isOpen);
    });
  });

  // Table scroll hint
  document.querySelectorAll('[data-scroll-hint]').forEach((wrap) => {
    const table = wrap.querySelector('table');
    if (table && table.scrollWidth <= wrap.clientWidth) {
      wrap.classList.add('no-hint');
    }
    wrap.addEventListener('scroll', () => {
      wrap.classList.add('is-scrolled');
    }, { passive: true });
  });

  // FAQ
  document.querySelectorAll('.faq__q').forEach((q) => {
    q.addEventListener('click', () => {
      const item = q.closest('.faq__item');
      const wasOpen = item.classList.contains('is-open');
      document.querySelectorAll('.faq__item').forEach((i) => i.classList.remove('is-open'));
      if (!wasOpen) item.classList.add('is-open');
    });
  });

  // Count-up
  const countIo = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      const el = entry.target;
      const target = parseFloat(el.dataset.target);
      const suffix = el.dataset.suffix || '';
      const duration = 1400;
      const start = performance.now();
      function tick(now) {
        const t = Math.min(1, (now - start) / duration);
        const eased = 1 - Math.pow(1 - t, 3);
        el.textContent = Math.floor(target * eased) + suffix;
        if (t < 1) requestAnimationFrame(tick);
        else el.textContent = target + suffix;
      }
      requestAnimationFrame(tick);
      countIo.unobserve(el);
    });
  }, { threshold: 0.5 });
  document.querySelectorAll('.count').forEach((el) => countIo.observe(el));

})();
