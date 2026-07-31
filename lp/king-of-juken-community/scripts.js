/**
 * 受験の王様コミュニティ
 */
(function () {
  "use strict";

  var INTRO_KEY = "king-of-juken-community-intro-seen";
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
    }, 60);
    setTimeout(function () {
      intro.classList.remove("boost-intro--showing");
      intro.classList.add("boost-intro--exiting");
    }, 1600);
    setTimeout(function () {
      markIntroSeen();
      finishIntro();
    }, 2100);
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
  var quicknav = document.getElementById("quicknav");
  var navBtns = quicknav
    ? Array.prototype.slice.call(quicknav.querySelectorAll("[data-sec]"))
    : [];
  var sections = navBtns.map(function (btn) {
    return document.getElementById(btn.getAttribute("data-sec"));
  });
  var ticking = false;

  function setActiveNav(id) {
    for (var i = 0; i < navBtns.length; i++) {
      var on = navBtns[i].getAttribute("data-sec") === id;
      navBtns[i].classList.toggle("is-active", on);
    }
  }

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
      if (navBtns.length) {
        var active = "top";
        var mark = vh * 0.35;
        for (var i = 0; i < sections.length; i++) {
          var sec = sections[i];
          if (!sec) continue;
          if (sec.getBoundingClientRect().top <= mark) {
            active = navBtns[i].getAttribute("data-sec");
          }
        }
        setActiveNav(active);
      }
      ticking = false;
    });
  }

  window.addEventListener("scroll", onScroll, { passive: true });
  window.addEventListener("resize", onScroll, { passive: true });
  onScroll();

  function copyText(text) {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      return navigator.clipboard.writeText(text);
    }
    return new Promise(function (resolve, reject) {
      var ta = document.createElement("textarea");
      ta.value = text;
      ta.setAttribute("readonly", "");
      ta.style.position = "fixed";
      ta.style.left = "-9999px";
      document.body.appendChild(ta);
      ta.select();
      try {
        document.execCommand("copy");
        resolve();
      } catch (err) {
        reject(err);
      } finally {
        document.body.removeChild(ta);
      }
    });
  }

  Array.prototype.forEach.call(document.querySelectorAll(".copy-btn"), function (btn) {
    btn.addEventListener("click", function () {
      var targetId = btn.getAttribute("data-target");
      var el = targetId ? document.getElementById(targetId) : null;
      if (!el) return;
      var idle = btn.querySelector(".copy-btn__idle");
      var done = btn.querySelector(".copy-btn__done");
      copyText(el.textContent.replace(/^\n+|\n+$/g, "")).then(function () {
        btn.classList.add("is-copied");
        if (idle) idle.hidden = true;
        if (done) done.hidden = false;
        setTimeout(function () {
          btn.classList.remove("is-copied");
          if (idle) idle.hidden = false;
          if (done) done.hidden = true;
        }, 1800);
      }).catch(function () {
        /* ignore */
      });
    });
  });
})();
