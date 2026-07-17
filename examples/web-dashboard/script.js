const header = document.querySelector(".site-header");

if (header) {
  const setShadow = () => {
    header.toggleAttribute("data-scrolled", window.scrollY > 8);
  };

  setShadow();
  window.addEventListener("scroll", setShadow, { passive: true });
}
