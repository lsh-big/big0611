const menuBtn = document.getElementById("menuBtn");
const mobileNav = document.getElementById("mobileNav");

if(menuBtn){

    menuBtn.addEventListener("click",()=>{

        mobileNav.classList.toggle("active");

    });

}

document.querySelectorAll("a").forEach(link => {
    link.target = "_blank";
    link.rel = "noopener noreferrer";
});
