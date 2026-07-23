(function () {
  "use strict";

  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var opening = document.getElementById("opening");
  var openingSkip = document.getElementById("openingSkip");
  var progress = document.getElementById("progress");
  var pageIndex = document.getElementById("pageIndex");
  var indexToggle = document.getElementById("indexToggle");
  var indexLinks = Array.prototype.slice.call(document.querySelectorAll(".page-index__nav a"));
  var reveals = Array.prototype.slice.call(document.querySelectorAll(".reveal"));
  var openingSeen = false;

  try {
    openingSeen = sessionStorage.getItem("coreenglish-sl-opening") === "1";
  } catch (e) {
    openingSeen = false;
  }

  function closeOpening() {
    if (!opening || opening.classList.contains("is-hidden")) return;
    opening.classList.add("is-hidden");
    document.body.classList.remove("is-locked");
    try {
      sessionStorage.setItem("coreenglish-sl-opening", "1");
    } catch (e) {}
  }

  if (opening) {
    if (openingSeen || reduceMotion) {
      opening.classList.add("is-hidden");
    } else {
      document.body.classList.add("is-locked");
      window.setTimeout(closeOpening, 3800);
    }
  }
  if (openingSkip) openingSkip.addEventListener("click", closeOpening);

  if (indexToggle && pageIndex) {
    indexToggle.addEventListener("click", function () {
      var open = pageIndex.classList.toggle("is-open");
      indexToggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }

  indexLinks.forEach(function (link) {
    link.addEventListener("click", function () {
      if (!pageIndex || !indexToggle) return;
      pageIndex.classList.remove("is-open");
      indexToggle.setAttribute("aria-expanded", "false");
    });
  });

  if ("IntersectionObserver" in window && !reduceMotion) {
    var revealObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("in");
        revealObserver.unobserve(entry.target);
      });
    }, { threshold: 0.1, rootMargin: "0px 0px -6% 0px" });
    reveals.forEach(function (el) { revealObserver.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add("in"); });
  }

  var ticking = false;
  function updateScroll() {
    ticking = false;
    var y = window.scrollY || document.documentElement.scrollTop;
    var scrollable = document.documentElement.scrollHeight - window.innerHeight;
    if (progress) {
      progress.style.width = Math.min(100, (y / Math.max(scrollable, 1)) * 100) + "%";
    }
    if (pageIndex) pageIndex.classList.toggle("show", y > window.innerHeight * 0.7);
  }
  function requestScrollUpdate() {
    if (ticking) return;
    ticking = true;
    window.requestAnimationFrame(updateScroll);
  }
  window.addEventListener("scroll", requestScrollUpdate, { passive: true });
  window.addEventListener("resize", requestScrollUpdate);
  updateScroll();

  if ("IntersectionObserver" in window) {
    var sectionObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        indexLinks.forEach(function (link) {
          link.classList.toggle("is-active", link.getAttribute("href") === "#" + entry.target.id);
        });
      });
    }, { rootMargin: "-30% 0px -55% 0px", threshold: 0 });
    indexLinks.forEach(function (link) {
      var section = document.querySelector(link.getAttribute("href"));
      if (section) sectionObserver.observe(section);
    });
  }

  /* Domain tabs */
  var domainBtns = Array.prototype.slice.call(document.querySelectorAll("[data-domain-tab]"));
  var domains = Array.prototype.slice.call(document.querySelectorAll("[data-domain]"));
  domainBtns.forEach(function (btn) {
    btn.addEventListener("click", function () {
      var id = btn.getAttribute("data-domain-tab");
      domainBtns.forEach(function (b) {
        var on = b === btn;
        b.classList.toggle("is-active", on);
        b.setAttribute("aria-selected", on ? "true" : "false");
      });
      domains.forEach(function (panel) {
        panel.classList.toggle("is-active", panel.getAttribute("data-domain") === id);
      });
    });
  });

  /* Checklist */
  var checks = Array.prototype.slice.call(document.querySelectorAll("[data-check]"));
  var summary = document.getElementById("checkSummary");
  var countEl = document.getElementById("checkCount");
  function updateChecks() {
    var n = checks.filter(function (el) { return el.classList.contains("is-on"); }).length;
    if (countEl) countEl.textContent = String(n);
    if (summary) summary.classList.toggle("is-show", n >= 1);
  }
  function toggleCheck(item) {
    item.classList.toggle("is-on");
    item.setAttribute("aria-checked", item.classList.contains("is-on") ? "true" : "false");
    updateChecks();
  }
  checks.forEach(function (item) {
    item.addEventListener("click", function () { toggleCheck(item); });
    item.addEventListener("keydown", function (e) {
      if (e.key === "Enter" || e.key === " ") {
        e.preventDefault();
        toggleCheck(item);
      }
    });
  });

  /* FAQ accordion */
  Array.prototype.slice.call(document.querySelectorAll("[data-faq]")).forEach(function (item) {
    var btn = item.querySelector("button");
    if (!btn) return;
    btn.addEventListener("click", function () {
      var open = item.classList.toggle("is-open");
      btn.setAttribute("aria-expanded", open ? "true" : "false");
    });
  });

  /* Letters infinite swipe (SSE-style) */
  var lettersCarousel = document.getElementById("lettersCarousel");
  if (lettersCarousel) {
    var LOOP_SETS = 3;
    var jumping = false;

    function syncLoop() {
      if (jumping) return;
      var setWidth = lettersCarousel.scrollWidth / LOOP_SETS;
      if (setWidth <= 0) return;
      if (lettersCarousel.scrollLeft < setWidth * 0.5) {
        jumping = true;
        lettersCarousel.scrollLeft += setWidth;
        jumping = false;
      } else if (lettersCarousel.scrollLeft >= setWidth * 2.5) {
        jumping = true;
        lettersCarousel.scrollLeft -= setWidth;
        jumping = false;
      }
    }

    function jumpMiddle() {
      var setWidth = lettersCarousel.scrollWidth / LOOP_SETS;
      if (setWidth > 0) lettersCarousel.scrollLeft = setWidth;
    }

    jumpMiddle();
    window.setTimeout(jumpMiddle, 120);
    window.setTimeout(jumpMiddle, 600);
    lettersCarousel.addEventListener("scroll", syncLoop, { passive: true });
    window.addEventListener("resize", jumpMiddle);

    /* drag to scroll on desktop */
    var isDown = false;
    var startX = 0;
    var startScroll = 0;
    lettersCarousel.addEventListener("mousedown", function (e) {
      isDown = true;
      startX = e.pageX;
      startScroll = lettersCarousel.scrollLeft;
    });
    window.addEventListener("mouseup", function () { isDown = false; });
    lettersCarousel.addEventListener("mouseleave", function () { isDown = false; });
    lettersCarousel.addEventListener("mousemove", function (e) {
      if (!isDown) return;
      e.preventDefault();
      lettersCarousel.scrollLeft = startScroll - (e.pageX - startX);
    });
  }
})();
