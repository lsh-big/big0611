document.addEventListener("DOMContentLoaded", () => {
    const cards = document.querySelectorAll(".tilt-card");

    cards.forEach((card) => {
        card.addEventListener("mousemove", (event) => {
        const rect = card.getBoundingClientRect();
        const x = event.clientX - rect.left;
        const y = event.clientY - rect.top;
        const rotateY = ((x / rect.width) - 0.5) * 10;
        const rotateX = ((0.5 - y / rect.height)) * 10;

        card.style.setProperty("--rx", `${rotateX}deg`);
        card.style.setProperty("--ry", `${rotateY}deg`);
});

        card.addEventListener("mouseleave", () => {
        card.style.setProperty("--rx", "0deg");
        card.style.setProperty("--ry", "0deg");
    });
});
});
const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
        if(entry.isIntersecting){
            entry.target.classList.add("show");
        }
    });
});

document.querySelectorAll(".section").forEach(section=>{
    observer.observe(section);
});
const topBtn = document.getElementById("topBtn");

if (topBtn) {

    window.addEventListener("scroll", () => {
        if (window.scrollY > 300) {
            topBtn.classList.add("show");
        } else {
            topBtn.classList.remove("show");
        }
    });


    topBtn.addEventListener("click", () => {
        window.scrollTo({
            top: 0,
            behavior: "smooth"
        });
    });

}

// topBtn.addEventListener("click", () => {
//     window.scrollTo({
//         top: 0,
//         behavior: "smooth"
//     });
// });
const indicator = document.querySelector(".scroll-indicator");

window.addEventListener("scroll", () => {
    if(window.scrollY > 100){
        indicator.style.opacity = "0";
        indicator.style.pointerEvents = "none";
    }else{
        indicator.style.opacity = "1";
    }
});