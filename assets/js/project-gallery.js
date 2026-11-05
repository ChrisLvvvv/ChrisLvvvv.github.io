(function () {
  "use strict";

  document.querySelectorAll("[data-project-gallery]").forEach(function (gallery) {
    var slides = Array.prototype.slice.call(gallery.querySelectorAll("[data-project-slide]"));
    var previous = gallery.querySelector("[data-project-previous]");
    var next = gallery.querySelector("[data-project-next]");
    var count = gallery.querySelector("[data-project-image-count]");
    var activeIndex = 0;

    if (slides.length < 2 || !previous || !next || !count) return;

    function showSlide(index) {
      activeIndex = Math.max(0, Math.min(slides.length - 1, index));
      slides.forEach(function (slide, slideIndex) {
        slide.hidden = slideIndex !== activeIndex;
      });
      previous.disabled = activeIndex === 0;
      next.disabled = activeIndex === slides.length - 1;
      count.textContent = (activeIndex + 1) + " / " + slides.length;
    }

    previous.addEventListener("click", function () { showSlide(activeIndex - 1); });
    next.addEventListener("click", function () { showSlide(activeIndex + 1); });
    gallery.addEventListener("keydown", function (event) {
      if (event.key === "ArrowLeft" || event.key === "ArrowRight") {
        event.preventDefault();
        showSlide(activeIndex + (event.key === "ArrowRight" ? 1 : -1));
      }
    });

    showSlide(0);
  });
})();
