/**
 * THINKING保護者通信 — LP scripts
 */
(function () {
  "use strict";

  var INTRO_KEY = "parent-letter-202510-intro-seen";
  var intro = document.getElementById("parentIntro");
  var reduceMo = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  function hasSeenIntro() {
    try {
      return window.sessionStorage.getItem(INTRO_KEY) === "1";
    } catch (e) {
      return false;
    }
  }

  function markIntroSeen() {
    try {
      window.sessionStorage.setItem(INTRO_KEY, "1");
    } catch (e) {
      /* private browsing */
    }
  }

  function finishIntro() {
    if (!intro) return;
    intro.remove();
    document.body.style.overflow = "";
    window.scrollTo(0, 0);
  }

  if (intro && !reduceMo && !hasSeenIntro()) {
    document.body.style.overflow = "hidden";
    setTimeout(function () {
      intro.classList.remove("parent-intro--entering");
      intro.classList.add("parent-intro--showing");
    }, 100);
    setTimeout(function () {
      intro.classList.remove("parent-intro--showing");
      intro.classList.add("parent-intro--exiting");
    }, 3800);
    setTimeout(function () {
      markIntroSeen();
      finishIntro();
    }, 4600);
  } else if (intro) {
    finishIntro();
  }

  var revealEls = Array.prototype.slice.call(
    document.querySelectorAll(".reveal, [data-stagger]")
  );

  function revealCheck(vh) {
    for (var i = revealEls.length - 1; i >= 0; i--) {
      var el = revealEls[i];
      var r = el.getBoundingClientRect();
      if (r.top < vh * 0.9 && r.bottom > 0) {
        el.classList.add("in");
        revealEls.splice(i, 1);
      }
    }
  }

  var progress = document.getElementById("progress");
  var quicknav = document.getElementById("quicknav");
  var hero = document.querySelector(".hero");
  var foot = document.querySelector(".foot");
  var pllEls = Array.prototype.slice.call(document.querySelectorAll("[data-pll]"));
  var navBtns = quicknav
    ? Array.prototype.slice.call(quicknav.querySelectorAll("[data-sec]"))
    : [];
  var sections = navBtns.map(function (btn) {
    return document.getElementById(btn.dataset.sec);
  });
  var ticking = false;

  function setActiveNav(id) {
    navBtns.forEach(function (btn) {
      btn.classList.toggle("is-active", btn.dataset.sec === id);
    });
  }

  function updateActiveSection(vh) {
    if (!sections.length) return;
    var marker = vh * 0.35;
    var current = "contents";

    sections.forEach(function (sec, i) {
      if (!sec) return;
      var r = sec.getBoundingClientRect();
      if (r.top <= marker) {
        current = navBtns[i].dataset.sec;
      }
    });

    setActiveNav(current);
  }

  function frame() {
    ticking = false;
    var sTop = window.scrollY || document.documentElement.scrollTop;
    var vh = window.innerHeight;
    var h = document.documentElement.scrollHeight - vh;

    if (progress) {
      progress.style.width = Math.min(100, (sTop / h) * 100) + "%";
    }

    revealCheck(vh);
    updateActiveSection(vh);

    if (quicknav && hero) {
      var heroBottom = hero.offsetTop + hero.offsetHeight;
      var footTop = foot ? foot.offsetTop : document.documentElement.scrollHeight;
      var viewBottom = sTop + vh;
      quicknav.classList.toggle("show", sTop > heroBottom * 0.5 && viewBottom < footTop + 80);
    } else if (quicknav) {
      quicknav.classList.toggle("show", sTop > 120);
    }

    if (!reduceMo) {
      pllEls.forEach(function (el) {
        var r = el.getBoundingClientRect();
        var prog = (r.top + r.height / 2 - vh / 2) / vh;
        el.style.transform =
          "translate3d(0," + (prog * parseFloat(el.dataset.pll)).toFixed(1) + "px,0)";
      });
    }
  }

  function onScroll() {
    if (!ticking) {
      ticking = true;
      requestAnimationFrame(frame);
    }
  }

  window.addEventListener("scroll", onScroll, { passive: true });
  window.addEventListener("resize", onScroll);
  frame();
  window.addEventListener("load", frame);
})();
