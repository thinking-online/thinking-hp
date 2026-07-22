(function () {
  "use strict";

  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var opening = document.getElementById("opening");
  var openingSkip = document.getElementById("openingSkip");
  var progress = document.getElementById("progress");
  var pageIndex = document.getElementById("pageIndex");
  var indexToggle = document.getElementById("indexToggle");
  var stickyCta = document.getElementById("stickyCta");
  var indexLinks = Array.prototype.slice.call(document.querySelectorAll(".page-index__nav a"));
  var reveals = Array.prototype.slice.call(document.querySelectorAll(".reveal"));
  var counters = Array.prototype.slice.call(document.querySelectorAll("[data-count]"));
  var openingSeen = false;

  try {
    openingSeen = sessionStorage.getItem("core-english-opening-seen") === "1";
  } catch (error) {
    openingSeen = false;
  }

  function closeOpening() {
    if (!opening || opening.classList.contains("is-hidden")) return;
    opening.classList.add("is-hidden");
    document.body.classList.remove("is-locked");
    try {
      sessionStorage.setItem("core-english-opening-seen", "1");
    } catch (error) {
      // The animation still works when storage is unavailable.
    }
  }

  if (openingSeen || reduceMotion) {
    if (opening) opening.classList.add("is-hidden");
  } else if (opening) {
    document.body.classList.add("is-locked");
    window.setTimeout(closeOpening, 3900);
  }

  if (openingSkip) openingSkip.addEventListener("click", closeOpening);

  if (indexToggle && pageIndex) {
    indexToggle.addEventListener("click", function () {
      var isOpen = pageIndex.classList.toggle("is-open");
      indexToggle.setAttribute("aria-expanded", isOpen ? "true" : "false");
    });
  }

  indexLinks.forEach(function (link) {
    link.addEventListener("click", function () {
      if (!pageIndex || !indexToggle) return;
      pageIndex.classList.remove("is-open");
      indexToggle.setAttribute("aria-expanded", "false");
    });
  });

  /* ---- Reveal on scroll ---- */
  if ("IntersectionObserver" in window && !reduceMotion) {
    var revealObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("in");
        revealObserver.unobserve(entry.target);
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -5% 0px" });
    reveals.forEach(function (item) { revealObserver.observe(item); });
  } else {
    reveals.forEach(function (item) { item.classList.add("in"); });
  }

  /* ---- Count-up stats ---- */
  function animateCount(el) {
    var target = parseFloat(el.getAttribute("data-count"));
    if (isNaN(target)) return;
    var hasComma = target >= 1000;
    var duration = 1400;
    var start = null;
    function tick(ts) {
      if (start === null) start = ts;
      var p = Math.min((ts - start) / duration, 1);
      var eased = 1 - Math.pow(1 - p, 3);
      var val = Math.round(target * eased);
      el.textContent = hasComma ? val.toLocaleString("en-US") : String(val);
      if (p < 1) window.requestAnimationFrame(tick);
    }
    window.requestAnimationFrame(tick);
  }

  if ("IntersectionObserver" in window && !reduceMotion && counters.length) {
    var countObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        animateCount(entry.target);
        countObserver.unobserve(entry.target);
      });
    }, { threshold: 0.6 });
    counters.forEach(function (c) { countObserver.observe(c); });
  }

  /* ---- Scroll: progress bar, page index, sticky CTA ---- */
  var ticking = false;
  function updateScroll() {
    ticking = false;
    var y = window.scrollY || document.documentElement.scrollTop;
    var scrollable = document.documentElement.scrollHeight - window.innerHeight;
    if (progress) {
      progress.style.width = Math.min(100, y / Math.max(scrollable, 1) * 100) + "%";
    }
    if (pageIndex) {
      pageIndex.classList.toggle("show", y > window.innerHeight * 0.85);
    }
    if (stickyCta) {
      // Show after leaving the hero, hide near the very bottom (final CTA visible).
      var show = y > window.innerHeight * 0.9 && y < scrollable - 620;
      stickyCta.classList.toggle("show", show);
    }
  }
  function requestScrollUpdate() {
    if (ticking) return;
    ticking = true;
    window.requestAnimationFrame(updateScroll);
  }
  window.addEventListener("scroll", requestScrollUpdate, { passive: true });
  window.addEventListener("resize", requestScrollUpdate);
  updateScroll();

  /* ---- Active section in page index ---- */
  if ("IntersectionObserver" in window) {
    var sectionObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        indexLinks.forEach(function (link) {
          link.classList.toggle("is-active", link.getAttribute("href") === "#" + entry.target.id);
        });
      });
    }, { rootMargin: "-35% 0px -55% 0px", threshold: 0 });
    indexLinks.forEach(function (link) {
      var section = document.querySelector(link.getAttribute("href"));
      if (section) sectionObserver.observe(section);
    });
  }
})();
