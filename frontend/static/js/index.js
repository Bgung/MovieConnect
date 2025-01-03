document.addEventListener("DOMContentLoaded", () => {
    const hamburger = document.querySelector(".hamburger");
    const sideNav = document.querySelector(".side-nav");

    // 클릭 시 사이드 네비게이션 표시/숨기기
    hamburger.addEventListener("click", () => {
        sideNav.classList.toggle("hidden");
        if (!sideNav.classList.contains("hidden")) {
            // # when the side nav is hidden, change the hamburger icon position
            hamburger.style.right = "150px";
        }
    });
});
