document.addEventListener("DOMContentLoaded", function () {
    // Smooth Scrolling for Navigation Links
    document.querySelectorAll(".nav-links a").forEach(link => {
        link.addEventListener("click", function (e) {
            if (this.getAttribute("href").startsWith("#")) {
                e.preventDefault();
                document.querySelector(this.getAttribute("href")).scrollIntoView({
                    behavior: "smooth"
                });
            }
        });
    });

    // Slide-in Animation for Hero Section
    const heroContent = document.querySelector(".hero-content");
    heroContent.style.display = "none"; // Hide initially
    setTimeout(() => {
        heroContent.style.display = "block"; // Show after page loads
        heroContent.classList.add("slide-in"); // Apply animation class
    }, 100);

    // Fade-in effect for the Support Section
    const supportSection = document.querySelector(".support");
    supportSection.style.display = "none";
    setTimeout(() => {
        supportSection.style.display = "flex"; // Show support section
        supportSection.classList.add("fade-in"); // Apply fade-in effect
    }, 300);

    // Optional FAQ Toggle (if you add any FAQ items in the future)
    const faqItems = document.querySelectorAll(".faq-item");

    faqItems.forEach(item => {
        item.querySelector(".faq-question").addEventListener("click", function () {
            item.classList.toggle("active");
        });
    });

    // Handle CTA button hover animation (optional)
    const ctaButton = document.querySelector(".cta-btn");
    if (ctaButton) {
        ctaButton.addEventListener("mouseenter", function () {
            ctaButton.style.transform = "scale(1.05)";
        });
        ctaButton.addEventListener("mouseleave", function () {
            ctaButton.style.transform = "scale(1)";
        });
    }
});
