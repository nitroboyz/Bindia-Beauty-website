const btn = document.getElementById("menuBtn");

const menu = document.getElementById("desktopMenu")

btn.addEventListener("click", () => {
    menu.classList.toggle("open")
})

console.log("JS loaded");
