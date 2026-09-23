/* Clearpine Technologies — minimal progressive enhancement.
   Deferred, tiny, no dependencies. Nothing here is required for content to render. */
(function () {
  "use strict";

  // Mobile navigation toggle
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.getElementById("site-nav");

  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });

    // Close menu on Escape
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && nav.classList.contains("open")) {
        nav.classList.remove("open");
        toggle.setAttribute("aria-expanded", "false");
        toggle.focus();
      }
    });
  }

  // Current year in footer
  var y = document.querySelectorAll("[data-year]");
  for (var i = 0; i < y.length; i++) {
    y[i].textContent = new Date().getFullYear();
  }

  // Contact form: mailto fallback so the site works on static hosting with no backend.
  var form = document.getElementById("contact-form");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var data = new FormData(form);
      var body = [
        "Name: " + (data.get("name") || ""),
        "Company: " + (data.get("company") || ""),
        "Email: " + (data.get("email") || ""),
        "Phone: " + (data.get("phone") || ""),
        "Service: " + (data.get("service") || ""),
        "",
        (data.get("message") || "")
      ].join("\n");

      var subject = "Website enquiry - " + (data.get("service") || "General");
      window.location.href =
        "mailto:info@clearpinetech.ca?subject=" +
        encodeURIComponent(subject) +
        "&body=" +
        encodeURIComponent(body);
    });
  }
})();
