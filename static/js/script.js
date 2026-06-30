const menuToggle = document.querySelector(".menu-toggle");
const navLinks = document.querySelector(".nav-links");
const navItems = document.querySelectorAll(".nav-links a");
const sections = document.querySelectorAll("main section[id]");
const contactForm = document.querySelector(".contact-form");
const formStatus = document.querySelector(".form-status");

menuToggle?.addEventListener("click", () => {
    const isOpen = navLinks.classList.toggle("open");
    menuToggle.setAttribute("aria-expanded", String(isOpen));
});

navItems.forEach((item) => {
    item.addEventListener("click", () => {
        navLinks.classList.remove("open");
        menuToggle?.setAttribute("aria-expanded", "false");
    });
});

const observer = new IntersectionObserver(
    (entries) => {
        entries.forEach((entry) => {
            if (!entry.isIntersecting) return;

            navItems.forEach((item) => {
                item.classList.toggle("active", item.getAttribute("href") === `#${entry.target.id}`);
            });
        });
    },
    {
        root: document.querySelector(".snap-wrapper"),
        threshold: 0.55
    }
);

sections.forEach((section) => observer.observe(section));

const encodeFormData = (form) => {
    const formData = new FormData(form);
    return new URLSearchParams(formData).toString();
};

contactForm?.addEventListener("submit", async (event) => {
    event.preventDefault();
    formStatus.textContent = "전송 중입니다...";

    try {
        const response = await fetch("/", {
            method: "POST",
            headers: { "Content-Type": "application/x-www-form-urlencoded" },
            body: encodeFormData(contactForm)
        });

        if (!response.ok) {
            throw new Error("Form submission failed");
        }

        contactForm.reset();
        formStatus.textContent = "메시지가 전송되었습니다. 빠르게 확인하겠습니다.";
    } catch (error) {
        formStatus.textContent = "전송에 실패했습니다. Netlify 배포 후 다시 시도해 주세요.";
    }
});
