(function () {
  "use strict";

  // 審査フォームURL（確定したらここだけ差し替え）
  var FORM_URL = "https://forms.gle/REPLACE_ME";

  var DEADLINE = new Date("2026-08-08T22:00:00+09:00").getTime();
  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var progress = document.getElementById("progress");
  var stickyCta = document.getElementById("stickyCta");
  var heroCta = document.getElementById("heroCta");
  var reveals = Array.prototype.slice.call(document.querySelectorAll(".reveal"));

  document.querySelectorAll("[data-form-link]").forEach(function (el) {
    el.setAttribute("href", FORM_URL);
    if (FORM_URL.indexOf("REPLACE") !== -1) {
      el.addEventListener("click", function (event) {
        event.preventDefault();
        window.alert("審査フォームのURLを設置してください（scripts.js の FORM_URL）。");
      });
    }
  });

  function pad(n) {
    return n < 10 ? "0" + n : String(n);
  }

  function setUnit(root, name, value) {
    var el = root.querySelector('[data-unit="' + name + '"]');
    if (el) el.textContent = pad(value);
  }

  function updateCountdown() {
    var now = Date.now();
    var diff = DEADLINE - now;
    var closed = diff <= 0;

    if (closed) {
      document.body.classList.add("is-closed");
      document.body.style.setProperty("--sticky-bottom", "0px");
      return false;
    }

    document.body.classList.remove("is-closed");
    var totalSec = Math.floor(diff / 1000);
    var days = Math.floor(totalSec / 86400);
    var hours = Math.floor((totalSec % 86400) / 3600);
    var mins = Math.floor((totalSec % 3600) / 60);
    var secs = totalSec % 60;

    document.querySelectorAll("[data-countdown]").forEach(function (root) {
      setUnit(root, "days", days);
      setUnit(root, "hours", hours);
      setUnit(root, "mins", mins);
      setUnit(root, "secs", secs);
    });
    return true;
  }

  if (updateCountdown()) {
    window.setInterval(updateCountdown, 1000);
  }

  if ("IntersectionObserver" in window && !reduceMotion) {
    var revealObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("in");
        revealObserver.unobserve(entry.target);
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -6% 0px" });

    reveals.forEach(function (item) {
      revealObserver.observe(item);
    });
  } else {
    reveals.forEach(function (item) {
      item.classList.add("in");
    });
  }

  var ticking = false;
  function onScroll() {
    ticking = false;
    var y = window.scrollY || document.documentElement.scrollTop;
    var scrollable = document.documentElement.scrollHeight - window.innerHeight;

    if (progress) {
      progress.style.width = Math.min(100, (y / Math.max(scrollable, 1)) * 100) + "%";
    }

    if (stickyCta && !document.body.classList.contains("is-closed")) {
      var show = false;
      if (heroCta) {
        var rect = heroCta.getBoundingClientRect();
        show = rect.bottom < 0;
      } else {
        show = y > 480;
      }
      stickyCta.classList.toggle("is-visible", show);
      document.body.style.setProperty("--sticky-bottom", show ? "78px" : "0px");
    }
  }

  window.addEventListener("scroll", function () {
    if (ticking) return;
    ticking = true;
    window.requestAnimationFrame(onScroll);
  }, { passive: true });

  onScroll();
})();
