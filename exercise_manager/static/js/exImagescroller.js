document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".img-btn-container").forEach(container => {
        const images = container.querySelector(".ex-img").children;
        const prevButton = container.querySelector(".prev");
        const nextButton = container.querySelector(".next");
        var st = 0
        nextButton.addEventListener('click', function () {
            if (st === 0) {
                st = 1
                images[1].style.right = '0';
                images[0].style.left = '344px';
                nextButton.style.display = 'none';
                prevButton.style.display = 'block';
            }
        });
        prevButton.addEventListener('click', function () {
            if (st === 1) {
                st = 0
                images[0].style.left = '0';
                images[1].style.right = '344px';
                nextButton.style.display = 'block';
                prevButton.style.display = 'none';
            };
        });
    });
});