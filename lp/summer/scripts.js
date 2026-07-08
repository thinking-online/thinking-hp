/* SUMMER LOCK-ON — interactions */

(function () {
  'use strict';

  const LINE_URL = window.getSummerLineUrl ? window.getSummerLineUrl() : '#';

  document.querySelectorAll('[data-line-cta]').forEach((el) => {
    el.href = LINE_URL;
  });

  // Nav scroll
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

  // Reveal
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

  // Hero sequence
  document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('[data-seq]').forEach((el, i) => {
      setTimeout(() => el.classList.add('in'), 200 + i * 200);
    });
  });

  // 300 hours bars
  const barIo = new IntersectionObserver((entries) => {
    entries.forEach((e) => {
      if (!e.isIntersecting) return;
      e.target.querySelectorAll('.hours-viz__bar').forEach((bar, i) => {
        setTimeout(() => {
          bar.style.height = (60 + Math.random() * 40) + '%';
        }, i * 30);
      });
      barIo.unobserve(e.target);
    });
  }, { threshold: 0.3 });
  document.querySelectorAll('.hours-viz').forEach((el) => barIo.observe(el));

  // Subject tabs
  document.querySelectorAll('.subjects__tab').forEach((tab) => {
    tab.addEventListener('click', () => {
      const group = tab.closest('.subjects');
      const target = tab.dataset.tab;
      group.querySelectorAll('.subjects__tab').forEach((t) => t.classList.remove('is-active'));
      group.querySelectorAll('.subjects__panel').forEach((p) => p.classList.remove('is-active'));
      tab.classList.add('is-active');
      const panel = group.querySelector('[data-panel="' + target + '"]');
      if (panel) panel.classList.add('is-active');
    });
  });

  // Subject accordion
  document.querySelectorAll('.subject-card__head').forEach((head) => {
    head.addEventListener('click', () => {
      const card = head.closest('.subject-card');
      const wasOpen = card.classList.contains('is-open');
      card.closest('.subjects__panel').querySelectorAll('.subject-card').forEach((c) => {
        c.classList.remove('is-open');
      });
      if (!wasOpen) card.classList.add('is-open');
    });
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

  // Checklist animation
  const checkIo = new IntersectionObserver((entries) => {
    entries.forEach((e) => {
      if (!e.isIntersecting) return;
      const items = e.target.querySelectorAll('.checklist__item');
      items.forEach((item, i) => {
        setTimeout(() => item.classList.add('is-checked'), 300 + i * 180);
      });
      checkIo.unobserve(e.target);
    });
  }, { threshold: 0.2 });
  document.querySelectorAll('.checklist').forEach((el) => checkIo.observe(el));

  // Pricing mode from URL ?plan=standard | ?plan=dual (default: dual)
  const pricing = document.getElementById('pricing');
  if (pricing) {
    const params = new URLSearchParams(window.location.search);
    const mode = params.get('plan') === 'standard' ? 'standard' : 'dual';
    pricing.dataset.pricingMode = mode;
  }

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
