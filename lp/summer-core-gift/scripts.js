(function () {
  "use strict";

  /**
   * 特典1〜6の配布リンク
   * ここを更新すると各ボタンの飛び先が変わります。
   */
  var GIFT_LINKS = {
    1: "#", // 英単語の核心
    2: "#", // イラスト英単語帳
    3: "#", // 英文法の核心
    4: "#", // 助動詞をイメージ理解する解説教材
    5: "#", // 英文解釈の核心
    6: "#"  // 英文解釈の入門
  };

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
    openingSeen = sessionStorage.getItem("summer-core-gift-opening-seen") === "1";
  } catch (error) {
    openingSeen = false;
  }

  function closeOpening() {
    if (!opening || opening.classList.contains("is-hidden")) return;
    opening.classList.add("is-hidden");
    document.body.classList.remove("is-locked");
    try {
      sessionStorage.setItem("summer-core-gift-opening-seen", "1");
    } catch (error) {
      // Storage may be unavailable.
    }
  }

  if (openingSeen || reduceMotion) {
    opening.classList.add("is-hidden");
  } else {
    document.body.classList.add("is-locked");
    window.setTimeout(closeOpening, 3900);
  }

  if (openingSkip) openingSkip.addEventListener("click", closeOpening);

  document.querySelectorAll("[data-gift-link]").forEach(function (link) {
    var key = link.getAttribute("data-gift-link");
    var url = GIFT_LINKS[key];
    if (url) link.setAttribute("href", url);
  });

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

  if ("IntersectionObserver" in window && !reduceMotion) {
    var revealObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("in");
        revealObserver.unobserve(entry.target);
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -5% 0px" });

    reveals.forEach(function (item) {
      revealObserver.observe(item);
    });
  } else {
    reveals.forEach(function (item) {
      item.classList.add("in");
    });
  }

  var ticking = false;
  function updateScroll() {
    ticking = false;
    var y = window.scrollY || document.documentElement.scrollTop;
    var scrollable = document.documentElement.scrollHeight - window.innerHeight;

    if (progress) {
      progress.style.width = Math.min(100, y / Math.max(scrollable, 1) * 100) + "%";
    }
    if (pageIndex) {
      pageIndex.classList.toggle("show", y > window.innerHeight * 0.55);
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
