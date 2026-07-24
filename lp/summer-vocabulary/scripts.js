(function () {
  "use strict";

  /**
   * 300単語特典の配布リンク
   * ここを更新するとボタン／スティッキーCTAの飛び先が変わります。
   */
  var GIFT_LINKS = {
    words300: ""
  };

  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var opening = document.getElementById("opening");
  var openingSkip = document.getElementById("openingSkip");
  var revealItems = Array.prototype.slice.call(document.querySelectorAll(".reveal:not(.in)"));
  var progress = document.getElementById("progress");
  var sticky = document.getElementById("sticky");
  var wordsSection = document.getElementById("words300");
  var footer = document.querySelector("footer");
  var ticking = false;
  var openingSeen = false;

  try {
    openingSeen = sessionStorage.getItem("summer-vocabulary-opening-seen") === "1";
  } catch (error) {
    openingSeen = false;
  }

  function closeOpening() {
    if (!opening || opening.classList.contains("is-hidden")) return;
    opening.classList.add("is-hidden");
    document.body.classList.remove("is-locked");
    try {
      sessionStorage.setItem("summer-vocabulary-opening-seen", "1");
    } catch (error) {
      // Storage may be unavailable.
    }
  }

  if (opening) {
    if (openingSeen || reduceMotion) {
      opening.classList.add("is-hidden");
    } else {
      document.body.classList.add("is-locked");
      window.setTimeout(closeOpening, 3200);
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

    if (sticky && wordsSection && footer) {
      var sectionTop = wordsSection.offsetTop;
      var footerTop = footer.offsetTop;
      sticky.classList.toggle(
        "show",
        scrollTop > sectionTop * 0.45 && scrollTop + viewportHeight < footerTop + 100
      );
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
