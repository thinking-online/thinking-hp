(function () {
  "use strict";

  /**
   * 特典配布リンク
   * ここを更新すると各ボタンの飛び先が変わります。
   */
  var GIFT_LINKS = {
    words300: "/pdfs/summer300_wordlist.pdf",
    schedule1000: "/pdfs/plan30_schedule.pdf"
  };

  var LINE_URL = "https://liff.line.me/1656043253-rkMxPZMQ/landing?follow=%40499yrupi&lp=JDVkS9&liff_id=1656043253-rkMxPZMQ";

  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var opening = document.getElementById("opening");
  var openingSkip = document.getElementById("openingSkip");
  var revealItems = Array.prototype.slice.call(document.querySelectorAll(".reveal:not(.in)"));
  var progress = document.getElementById("progress");
  var sticky = document.getElementById("sticky");
  var wordsSection = document.getElementById("words300");
  var lineSection = document.getElementById("line");
  var lineFloat = document.getElementById("lineFloat");
  var lineFloatClose = document.getElementById("lineFloatClose");
  var footer = document.querySelector("footer");
  var ticking = false;
  var openingSeen = false;
  var lineFloatDismissed = false;

  try {
    openingSeen = sessionStorage.getItem("summer-vocabulary-opening-seen") === "1";
    lineFloatDismissed = sessionStorage.getItem("summer-vocabulary-line-float-dismissed") === "1";
  } catch (error) {
    openingSeen = false;
    lineFloatDismissed = false;
  }

  var openingCount = document.getElementById("openingCount");
  var countFrame = 0;

  function closeOpening() {
    if (!opening || opening.classList.contains("is-hidden")) return;
    if (countFrame) window.cancelAnimationFrame(countFrame);
    opening.classList.add("is-hidden");
    document.body.classList.remove("is-locked");
    try {
      sessionStorage.setItem("summer-vocabulary-opening-seen", "1");
    } catch (error) {
      // Storage may be unavailable.
    }
  }

  function animateCount(durationMs) {
    if (!openingCount) return;
    var start = null;

    function tick(now) {
      if (start === null) start = now;
      var progress = Math.min(1, (now - start) / durationMs);
      var eased = 1 - Math.pow(1 - progress, 3);
      openingCount.textContent = String(Math.round(eased * 300));
      if (progress < 1) {
        countFrame = window.requestAnimationFrame(tick);
      } else {
        openingCount.textContent = "300";
      }
    }

    countFrame = window.requestAnimationFrame(tick);
  }

  if (opening) {
    if (openingSeen || reduceMotion) {
      opening.classList.add("is-hidden");
      if (openingCount) openingCount.textContent = "300";
    } else {
      document.body.classList.add("is-locked");
      window.setTimeout(function () {
        animateCount(2200);
      }, 900);
      window.setTimeout(closeOpening, 4800);
    }
  }

  if (openingSkip) openingSkip.addEventListener("click", closeOpening);

  document.querySelectorAll("[data-gift-link]").forEach(function (link) {
    var key = link.getAttribute("data-gift-link");
    var url = GIFT_LINKS[key];
    if (url) {
      link.setAttribute("href", url);
    } else {
      link.addEventListener("click", function (event) {
        event.preventDefault();
      });
    }
  });

  document.querySelectorAll("[data-line-link]").forEach(function (link) {
    link.setAttribute("href", LINE_URL);
  });

  function dismissLineFloat() {
    lineFloatDismissed = true;
    if (lineFloat) {
      lineFloat.classList.remove("show");
      lineFloat.hidden = true;
    }
    try {
      sessionStorage.setItem("summer-vocabulary-line-float-dismissed", "1");
    } catch (error) {
      // Storage may be unavailable.
    }
  }

  if (lineFloatClose) {
    lineFloatClose.addEventListener("click", function (event) {
      event.preventDefault();
      event.stopPropagation();
      dismissLineFloat();
    });
  }

  function update() {
    ticking = false;

    var scrollTop = window.scrollY || document.documentElement.scrollTop;
    var viewportHeight = window.innerHeight;
    var scrollable = document.documentElement.scrollHeight - viewportHeight;

    if (progress) {
      progress.style.width = Math.min(100, (scrollTop / Math.max(scrollable, 1)) * 100) + "%";
    }

    for (var i = revealItems.length - 1; i >= 0; i -= 1) {
      var rect = revealItems[i].getBoundingClientRect();
      if (rect.top < viewportHeight * 0.88 && rect.bottom > 0) {
        revealItems[i].classList.add("in");
        revealItems.splice(i, 1);
      }
    }

    var stickyVisible = false;
    if (sticky && wordsSection && footer) {
      var sectionTop = wordsSection.offsetTop;
      var footerTop = footer.offsetTop;
      stickyVisible =
        scrollTop > sectionTop * 0.45 && scrollTop + viewportHeight < footerTop + 100;
      sticky.classList.toggle("show", stickyVisible);
    }

    if (lineFloat && !lineFloatDismissed) {
      var nearLineSection = false;
      if (lineSection) {
        var lineRect = lineSection.getBoundingClientRect();
        nearLineSection = lineRect.top < viewportHeight * 0.72 && lineRect.bottom > 80;
      }

      var shouldShowFloat =
        scrollTop > viewportHeight * 0.55 &&
        !nearLineSection &&
        scrollTop + viewportHeight < (footer ? footer.offsetTop + 40 : Infinity);

      lineFloat.hidden = false;
      lineFloat.classList.toggle("show", shouldShowFloat);
      lineFloat.classList.toggle("is-lifted", shouldShowFloat && stickyVisible);
    }
  }

  function scheduleUpdate() {
    if (!ticking) {
      ticking = true;
      window.requestAnimationFrame(update);
    }
  }

  if (reduceMotion) {
    revealItems.forEach(function (item) {
      item.classList.add("in");
    });
    revealItems = [];
  }

  window.addEventListener("scroll", scheduleUpdate, { passive: true });
  window.addEventListener("resize", scheduleUpdate);
  window.addEventListener("load", update);
  update();
})();
