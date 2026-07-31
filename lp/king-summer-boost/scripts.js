/**
 * 王様の夏休み 追い込みチャレンジ
 */
(function () {
  "use strict";

  var INTRO_KEY = "king-summer-boost-intro-seen";
  var intro = document.getElementById("boostIntro");
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
      intro.classList.remove("boost-intro--entering");
      intro.classList.add("boost-intro--showing");
    }, 100);
    setTimeout(function () {
      intro.classList.remove("boost-intro--showing");
      intro.classList.add("boost-intro--exiting");
    }, 4800);
    setTimeout(function () {
      markIntroSeen();
      finishIntro();
    }, 5600);
  } else if (intro) {
    finishIntro();
  }

  var revealEls = Array.prototype.slice.call(document.querySelectorAll(".reveal"));

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
  var ticking = false;

  function onScroll() {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(function () {
      var vh = window.innerHeight || document.documentElement.clientHeight;
      revealCheck(vh);
      if (progress) {
        var doc = document.documentElement;
        var max = doc.scrollHeight - doc.clientHeight;
        var pct = max > 0 ? (window.scrollY / max) * 100 : 0;
        progress.style.width = Math.min(100, Math.max(0, pct)) + "%";
      }
      ticking = false;
    });
  }

  window.addEventListener("scroll", onScroll, { passive: true });
  window.addEventListener("resize", onScroll, { passive: true });
  onScroll();
})();
