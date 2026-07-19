(function () {
  "use strict";

  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var opening = document.getElementById("opening");
  var openingSkip = document.getElementById("openingSkip");
  var progress = document.getElementById("progress");
  var reveals = Array.prototype.slice.call(document.querySelectorAll(".reveal"));
  var openingSeen = false;

  try {
    openingSeen = sessionStorage.getItem("summer-core-opening-seen") === "1";
  } catch (error) {
    openingSeen = false;
  }

  function closeOpening() {
    if (!opening || opening.classList.contains("is-hidden")) return;
    opening.classList.add("is-hidden");
    document.body.classList.remove("is-locked");
    try {
      sessionStorage.setItem("summer-core-opening-seen", "1");
    } catch (error) {
      // The animation still works when storage is unavailable.
    }
  }

  if (openingSeen || reduceMotion) {
    opening.classList.add("is-hidden");
  } else {
    document.body.classList.add("is-locked");
    window.setTimeout(closeOpening, 3900);
  }

  if (openingSkip) openingSkip.addEventListener("click", closeOpening);

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
  }

  function requestScrollUpdate() {
    if (ticking) return;
    ticking = true;
    window.requestAnimationFrame(updateScroll);
  }

  window.addEventListener("scroll", requestScrollUpdate, { passive: true });
  window.addEventListener("resize", requestScrollUpdate);
  updateScroll();
})();
