(function () {
  "use strict";

  var root = document.documentElement;
  var body = document.body;
  var header = document.querySelector("[data-site-header]");
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.querySelector(".site-nav");
  var progress = document.querySelector(".page-progress span");
  var openingHero = document.querySelector("[data-opening-hero]");
  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  function drawTechnicalLines(scope) {
    if (reduceMotion || !window.anime) return;
    var lines = scope.querySelectorAll(".graphic-route, .graphic-signal, .graphic-waves path, .graphic-orbits ellipse, .trace-lines path, .hero-buses path, .hero-thin path, .hero-pins path, .selected-graphic path, .selected-graphic rect, .selected-graphic circle");
    lines.forEach(function (line) {
      if (typeof line.getTotalLength !== "function" || line.dataset.drawn) return;
      var length = line.getTotalLength();
      line.dataset.drawn = "true";
      line.style.strokeDasharray = length;
      line.style.strokeDashoffset = length;
      window.anime({
        targets: line,
        strokeDashoffset: [length, 0],
        duration: 1300,
        delay: 120,
        easing: "easeInOutQuart"
      });
    });
  }

  function closeNavigation() {
    body.classList.remove("nav-open");
    if (toggle) toggle.setAttribute("aria-expanded", "false");
  }

  if (toggle) {
    toggle.addEventListener("click", function () {
      var open = body.classList.toggle("nav-open");
      toggle.setAttribute("aria-expanded", String(open));
    });
  }

  if (nav) {
    nav.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", closeNavigation);
    });
  }

  document.addEventListener("keydown", function (event) {
    if (event.key === "Escape") closeNavigation();
  });

  function updateScrollState() {
    var y = window.scrollY || window.pageYOffset;
    if (header) header.classList.toggle("is-scrolled", y > 20);
    if (openingHero) {
      var heroHeight = openingHero.offsetHeight;
      var exitProgress = Math.max(0, Math.min(1, (y - heroHeight * 0.58) / (heroHeight * 0.42)));
      openingHero.style.setProperty("--hero-exit", reduceMotion ? 0 : exitProgress.toFixed(3));
      body.classList.toggle("is-past-hero", y >= heroHeight - 80);
    }
    if (progress) {
      var total = document.documentElement.scrollHeight - window.innerHeight;
      progress.style.transform = "scaleX(" + (total > 0 ? Math.min(y / total, 1) : 0) + ")";
    }
  }

  var selector = document.querySelector("[data-work-selector]");
  if (selector) {
    var slides = Array.prototype.slice.call(selector.querySelectorAll("[data-work-slide]"));
    var previousButton = selector.querySelector("[data-work-prev]");
    var nextButton = selector.querySelector("[data-work-next]");
    var workViewport = selector.querySelector("[data-work-viewport]");
    var workTrack = selector.querySelector("[data-work-track]");
    var activeIndex = 0;
    var pointerStart = null;

    function updateWorkTrack() {
      var maxOffset = Math.max(0, workTrack.scrollWidth - workViewport.clientWidth);
      var progress = slides.length > 1 ? activeIndex / (slides.length - 1) : 0;
      workTrack.style.transform = "translate3d(" + (-maxOffset * progress) + "px,0,0)";
      previousButton.disabled = activeIndex === 0;
      nextButton.disabled = activeIndex === slides.length - 1;
      slides.forEach(function (slide, index) {
        slide.classList.toggle("is-active", index === activeIndex);
      });
    }

    function setSlide(nextIndex) {
      activeIndex = Math.max(0, Math.min(slides.length - 1, nextIndex));
      updateWorkTrack();
    }

    previousButton.addEventListener("click", function () { setSlide(activeIndex - 1); });
    nextButton.addEventListener("click", function () { setSlide(activeIndex + 1); });
    selector.addEventListener("keydown", function (event) {
      if (event.key === "ArrowLeft") setSlide(activeIndex - 1);
      if (event.key === "ArrowRight") setSlide(activeIndex + 1);
    });
    workViewport.addEventListener("pointerdown", function (event) { pointerStart = event.clientX; });
    workViewport.addEventListener("pointerup", function (event) {
      if (pointerStart === null) return;
      var delta = event.clientX - pointerStart;
      if (Math.abs(delta) > 55) setSlide(activeIndex + (delta < 0 ? 1 : -1));
      pointerStart = null;
    });
    window.addEventListener("resize", updateWorkTrack);
    updateWorkTrack();
    window.setTimeout(function () { drawTechnicalLines(workTrack); }, 650);
  }

  window.addEventListener("scroll", updateScrollState, { passive: true });
  updateScrollState();

  var revealItems = document.querySelectorAll("[data-reveal]");
  if (!reduceMotion && "IntersectionObserver" in window) {
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          drawTechnicalLines(entry.target);
          observer.unobserve(entry.target);
        }
      });
    }, { rootMargin: "0px 0px -9%", threshold: 0.08 });
    revealItems.forEach(function (item) { observer.observe(item); });
  } else {
    revealItems.forEach(function (item) { item.classList.add("is-visible"); });
  }

  var heroItems = document.querySelectorAll("[data-hero-reveal]");
  if (!reduceMotion && window.anime && heroItems.length) {
    window.anime({
      targets: heroItems,
      opacity: [0, 1],
      translateY: [28, 0],
      duration: 1150,
      delay: window.anime.stagger(115, { start: 100 }),
      easing: "cubicBezier(0.22, 0.72, 0.22, 1)"
    });
    window.setTimeout(function () { drawTechnicalLines(document.querySelector(".home-hero") || document); }, 500);
  } else {
    heroItems.forEach(function (item) {
      item.style.opacity = "1";
      item.style.transform = "none";
    });
  }

  if (!reduceMotion && window.matchMedia("(pointer: fine)").matches) {
    document.querySelectorAll("[data-cursor-field]").forEach(function (field) {
      var graphic = field.querySelector("svg");
      if (!graphic) return;
      field.addEventListener("pointermove", function (event) {
        var rect = field.getBoundingClientRect();
        var x = (event.clientX - rect.left) / rect.width - 0.5;
        var y = (event.clientY - rect.top) / rect.height - 0.5;
        graphic.style.transform = "translate3d(" + (x * 7) + "px," + (y * 7) + "px,0) scale(1.018)";
      });
      field.addEventListener("pointerleave", function () {
        graphic.style.transform = "";
      });
    });
  }

  root.classList.add("editorial-ready");
})();
