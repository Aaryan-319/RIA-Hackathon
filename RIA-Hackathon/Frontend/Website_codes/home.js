document.addEventListener("DOMContentLoaded", function () {
    // FAQ Toggle (if you have FAQ items)
    const faqItems = document.querySelectorAll(".faq-item");

    faqItems.forEach(item => {
        item.querySelector(".faq-question").addEventListener("click", function () {
            item.classList.toggle("active");
        });
    });

    // Slide-in Animation for elements
    document.querySelectorAll(".slide-in").forEach(element => {
        element.style.display = "none";
        setTimeout(() => element.style.display = "block", 0);
        element.classList.add("slide-down");
    });

    // Fade-in Animation for elements
    document.querySelectorAll(".fade-in").forEach(element => {
        element.style.display = "none";
        setTimeout(() => element.style.display = "block", 0);
        element.classList.add("fade-in-effect");
    });

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

    // Confirm Vote Functionality (when confirm button is clicked)
    document.querySelectorAll(".vote-btn").forEach(button => {
        button.addEventListener("click", function () {
            const candidateName = this.closest('.participant').querySelector('h3').innerText;
            alert(`You have voted for ${candidateName}! Your vote has been recorded.`);
        });
    });
});
