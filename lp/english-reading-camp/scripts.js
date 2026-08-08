(function () {
  "use strict";

  // 審査フォームURL（LINE公式アカウント経由）
  var FORM_URL = "https://liff.line.me/1656043253-rkMxPZMQ/landing?follow=%40499yrupi&lp=fnK0MJ&liff_id=1656043253-rkMxPZMQ";

  var DEADLINE = new Date("2026-08-08T22:00:00+09:00").getTime();
  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var progress = document.getElementById("progress");
  var stickyCta = document.getElementById("stickyCta");
  var heroCta = document.getElementById("heroCta");
  var reveals = Array.prototype.slice.call(document.querySelectorAll(".reveal"));
  var formLinks = Array.prototype.slice.call(document.querySelectorAll("[data-form-link]"));
  var closedApplied = false;

  function bindFormLinks() {
    formLinks.forEach(function (el) {
      el.setAttribute("href", FORM_URL);
      if (FORM_URL.indexOf("REPLACE") !== -1) {
        el.addEventListener("click", function (event) {
          event.preventDefault();
          window.alert("審査フォームのURLを設置してください（scripts.js の FORM_URL）。");
        });
      }
    });
  }

  function disableFormLinks() {
    formLinks.forEach(function (el) {
      el.removeAttribute("href");
      el.removeAttribute("target");
      el.setAttribute("aria-disabled", "true");
      el.setAttribute("tabindex", "-1");
      el.addEventListener("click", function (event) {
        event.preventDefault();
      });
    });
  }

  function applyClosedState() {
    if (closedApplied) return;
    closedApplied = true;
    document.body.classList.add("is-closed");
    document.body.style.setProperty("--sticky-bottom", "72px");
    if (stickyCta) stickyCta.classList.remove("is-visible");
    disableFormLinks();
  }

  bindFormLinks();

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

    if (diff <= 0) {
      applyClosedState();
      document.querySelectorAll("[data-countdown]").forEach(function (root) {
        setUnit(root, "days", 0);
        setUnit(root, "hours", 0);
        setUnit(root, "mins", 0);
        setUnit(root, "secs", 0);
      });
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
      var pastIntro = y > Math.min(520, window.innerHeight * 0.7);
      var finalInView = false;
      if (heroCta) {
        var rect = heroCta.getBoundingClientRect();
        finalInView = rect.top < window.innerHeight - 40 && rect.bottom > 0;
      }
      var show = pastIntro && !finalInView;
      stickyCta.classList.toggle("is-visible", show);
      document.body.style.setProperty("--sticky-bottom", show ? "70px" : "0px");
    }
  }

  window.addEventListener("scroll", function () {
    if (ticking) return;
    ticking = true;
    window.requestAnimationFrame(onScroll);
  }, { passive: true });

  onScroll();

  /* 5日後カード：スワイプで見えるものから順にチェック */
  var outcomeTrack = document.getElementById("outcomeTrack");
  var outcomeCards = Array.prototype.slice.call(document.querySelectorAll("[data-outcome]"));
  var outcomeCount = document.querySelector("[data-outcome-count]");
  var outcomeBar = document.querySelector("[data-outcome-bar]");
  var outcomeTotal = outcomeCards.length;

  function updateOutcomeProgress() {
    var checked = outcomeCards.filter(function (card) {
      return card.classList.contains("is-checked");
    }).length;
    if (outcomeCount) outcomeCount.textContent = String(checked);
    if (outcomeBar) {
      outcomeBar.style.width = outcomeTotal
        ? Math.round((checked / outcomeTotal) * 100) + "%"
        : "0%";
    }
  }

  function markOutcome(card) {
    if (card.classList.contains("is-checked")) return;
    card.classList.add("is-checked");
    updateOutcomeProgress();
  }

  if (outcomeTrack && outcomeCards.length) {
    if ("IntersectionObserver" in window) {
      var outcomeObserver = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          markOutcome(entry.target);
        });
      }, {
        root: outcomeTrack,
        threshold: 0.55,
        rootMargin: "0px"
      });

      outcomeCards.forEach(function (card) {
        outcomeObserver.observe(card);
      });
    }

    // 最初のカードは表示直後にチェック
    window.setTimeout(function () {
      if (outcomeCards[0]) markOutcome(outcomeCards[0]);
    }, reduceMotion ? 0 : 280);

    if (reduceMotion) {
      outcomeCards.forEach(markOutcome);
    }
  }
})();
