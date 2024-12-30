document.addEventListener("DOMContentLoaded", () => {
    const hamburger = document.querySelector(".hamburger");
    const sideNav = document.querySelector(".side-nav");

    // let isMouseOverSideNav = false;

    // // 마우스가 햄버거 버튼 위에 있을 때 사이드 네비게이션 표시
    // hamburger.addEventListener("mouseover", () => {
    //     sideNav.classList.remove("hidden");
    // });

    // // 마우스가 햄버거 버튼을 벗어났을 때 사이드 네비게이션 숨기기
    // hamburger.addEventListener("mouseout", () => {
    //     setTimeout(() => {
    //         if (!isMouseOverSideNav) {
    //             sideNav.classList.add("hidden");
    //         }
    //     }, 500); // 짧은 딜레이 추가
    // });

    // // 사이드 네비게이션 위로 마우스가 들어올 때 숨기지 않음
    // sideNav.addEventListener("mouseover", () => {
    //     isMouseOverSideNav = true;
    //     sideNav.classList.remove("hidden");
    // });

    // // 사이드 네비게이션에서 마우스가 나갈 때 확인 후 숨기기
    // sideNav.addEventListener("mouseout", () => {
    //     isMouseOverSideNav = false;
    //     setTimeout(() => {
    //         if (!hamburger.matches(':hover')) {
    //             sideNav.classList.add("hidden");
    //         }
    //     }, 500); // 딜레이로 자연스러운 동작 구현
    // });

    // 클릭 시 사이드 네비게이션 표시/숨기기
    hamburger.addEventListener("click", () => {
        sideNav.classList.toggle("hidden");
        if (!sideNav.classList.contains("hidden")) {
            // # when the side nav is hidden, change the hamburger icon position
            hamburger.style.right = "150px";
        }
    });
});

function lorem_ipsum(id) {
    document.getElementById(id).innerText = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam. Maecenas ligula massa, varius a, semper congue, euismod non, mi.";
    document.getElementById(id).innerText += "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam. Maecenas ligula massa, varius a, semper congue, euismod non, mi.";
}

lorem_ipsum("about_li");
lorem_ipsum("education_li");
lorem_ipsum("publication_li");