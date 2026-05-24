/* THINKING 家勉部 — scroll reveal, count-up, hero sequence, FAQ, sticky CTA */

(function () {
  'use strict';

  // ===== Nav scroll state =====
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
    if (sticky) sticky.classList.toggle('in', y > 600 && y < (document.documentElement.scrollHeight - window.innerHeight - 400));
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // ===== Hero sequence (intro stagger) =====
  document.addEventListener('DOMContentLoaded', () => {
    const seq = Array.from(document.querySelectorAll('[data-seq]')).sort((a, b) => +a.dataset.seq - +b.dataset.seq);
    seq.forEach((el, i) => {
      setTimeout(() => {
        el.classList.add('in');
      }, 300 + i * 480);
    });
    // Hero photo fade-in
    const hv = document.getElementById('heroVisual');
    if (hv) setTimeout(() => hv.classList.add('in'), 200);
  });

  // ===== Scroll reveal =====
  const io = new IntersectionObserver((entries) => {
    entries.forEach((e) => {
      if (e.isIntersecting) {
        e.target.classList.add('in');
        io.unobserve(e.target);
      }
    });
  }, { threshold: 0.14, rootMargin: '0px 0px -8% 0px' });

  document.querySelectorAll('.reveal, .reveal-up, .reveal-slow, .line-wipe').forEach((el) => {
    // skip hero items already controlled by data-seq stagger
    if (el.hasAttribute('data-seq')) return;
    io.observe(el);
  });

  // Stagger inside .pain__list and .after__grid and .testi__track and .manifesto__rows
  function staggerChildren(parentSel, childSel, base = 80) {
    document.querySelectorAll(parentSel).forEach((parent) => {
      parent.querySelectorAll(childSel).forEach((child, i) => {
        child.style.transitionDelay = (i * base) + 'ms';
      });
    });
  }
  staggerChildren('.pain__list', '.pain__item', 70);
  staggerChildren('.after__grid', '.after__cell', 60);
  staggerChildren('.testi__track', '.testi', 90);
  staggerChildren('.manifesto__rows', '.manifesto__row', 110);
  staggerChildren('.world__lines', '.world__line', 140);
  staggerChildren('.rank__tops', '.rank__top', 120);
  staggerChildren('.faq__list', '.faq__item', 0);
  staggerChildren('.fit__list', 'li', 80);

  // ===== Count-up =====
  const countIo = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      const el = entry.target;
      const target = parseFloat(el.dataset.target);
      const divisor = parseFloat(el.dataset.divisor || '1');
      const comma = el.dataset.comma === '1';
      const duration = 1600;
      const start = performance.now();
      function tick(now) {
        const t = Math.min(1, (now - start) / duration);
        const eased = 1 - Math.pow(1 - t, 3);
        const raw = target * eased / divisor;
        let v;
        if (divisor > 1) v = raw.toFixed(1);
        else v = Math.floor(raw);
        if (comma) v = Number(v).toLocaleString('en-US');
        el.textContent = v;
        if (t < 1) requestAnimationFrame(tick);
        else {
          // Final value (handle decimals/comma)
          let final = (divisor > 1) ? (target / divisor).toFixed(1) : target;
          if (comma) final = Number(final).toLocaleString('en-US');
          el.textContent = final;
        }
      }
      requestAnimationFrame(tick);
      countIo.unobserve(el);
    });
  }, { threshold: 0.4 });
  document.querySelectorAll('.count').forEach((el) => countIo.observe(el));

  // ===== Time chart bars =====
  const barIo = new IntersectionObserver((entries) => {
    entries.forEach((e) => {
      if (!e.isIntersecting) return;
      e.target.style.height = e.target.dataset.barHeight || '50%';
      barIo.unobserve(e.target);
    });
  }, { threshold: 0.3 });
  document.querySelectorAll('[data-bar-height]').forEach((el) => barIo.observe(el));

  // ===== FAQ accordion =====
  document.querySelectorAll('.faq__q').forEach((q) => {
    q.addEventListener('click', () => {
      const item = q.closest('.faq__item');
      item.classList.toggle('is-open');
    });
  });
  // Open first by default
  const first = document.querySelector('.faq__item');
  if (first) first.classList.add('is-open');

  // ===== Subtle parallax on hero photo =====
  const heroImg = document.querySelector('#heroVisual img');
  const worldBg = document.querySelector('.world__bg');
  const finalBg = document.querySelector('.final__bg');
  function parallax() {
    const y = window.scrollY;
    if (heroImg && y < window.innerHeight) {
      heroImg.style.transform = `scale(1.08) translateY(${y * 0.12}px)`;
    }
    if (worldBg) {
      const rect = worldBg.parentElement.getBoundingClientRect();
      const center = (rect.top + rect.height / 2) - (window.innerHeight / 2);
      worldBg.style.transform = `scale(1.1) translateY(${center * -0.08}px)`;
    }
    if (finalBg) {
      const rect = finalBg.parentElement.getBoundingClientRect();
      const center = (rect.top + rect.height / 2) - (window.innerHeight / 2);
      finalBg.style.transform = `translateY(${center * -0.06}px)`;
    }
  }
  let ticking = false;
  window.addEventListener('scroll', () => {
    if (!ticking) {
      requestAnimationFrame(() => { parallax(); ticking = false; });
      ticking = true;
    }
  }, { passive: true });

})();
