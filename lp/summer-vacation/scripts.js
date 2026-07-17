(function () {
  "use strict";

  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var revealItems = Array.prototype.slice.call(document.querySelectorAll(".reveal:not(.in)"));
  var progress = document.getElementById("progress");
  var sticky = document.getElementById("sticky");
  var textbook = document.getElementById("textbook");
  var footer = document.querySelector("footer");
  var ticking = false;

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

    if (sticky && textbook && footer) {
      var textbookTop = textbook.offsetTop;
      var footerTop = footer.offsetTop;
      sticky.classList.toggle(
        "show",
        scrollTop > textbookTop * 0.55 && scrollTop + viewportHeight < footerTop + 100
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
