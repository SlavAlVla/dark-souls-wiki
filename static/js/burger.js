let condition = true;

function dragOut() {
    anime({
        targets: ".mini_menu",
        translateX: ["-105%", "-5%"],
        easing: "easeInOutQuad",
        direction: "alternate",
        duration: 800,
        loop: false
    });
    anime({
        targets: ".line1",
        translateY: ["0", "13px"],
        rotate: 135,
        easing: "easeInOutQuad",
        direction: "alternate",
        duration: 800,
        loop: false
    });
    anime({
        targets: ".line3",
        translateY: ["0", "-13px"],
        rotate: -135,
        easing: "easeInOutQuad",
        direction: "alternate",
        duration: 800,
        loop: false
    });
    anime({
        targets: ".line2",
        opacity: ["1", "0"],
        easing: "easeInOutQuad",
        direction: "alternate",
        duration: 800,
        loop: false
    });
    condition = false;
}

function dragIn() {
    anime({
        targets: ".mini_menu",
        translateX: ["-5%", "-105%"],
        easing: "easeInOutQuad",
        direction: "alternate",
        duration: 800,
        loop: false
    });
    anime({
        targets: ".line1",
        translateY: ["13px", "0"],
        rotate: 0,
        easing: "easeInOutQuad",
        direction: "alternate",
        duration: 800,
        loop: false
    });
    anime({
        targets: ".line3",
        translateY: ["-13px", "0"],
        rotate: 0,
        easing: "easeInOutQuad",
        direction: "alternate",
        duration: 800,
        loop: false
    });
    anime({
        targets: ".line2",
        opacity: ["0", "1"],
        easing: "easeInOutQuad",
        direction: "alternate",
        duration: 800,
        loop: false
    });
    condition = false;
    condition = true;
}

$(".burger_button").click(function() {
    if (condition)
        dragOut();
    else
        dragIn();
})

// let touchStartX;
// $(document).on("touchstart", function(event) {
//     touchStartX = event.originalEvent.touches[0].pageX;
// })

// $(document).on("touchend", function(event) {
//     if (event.originalEvent.changedTouches[0].pageX - touchStartX >= 100 && condition)
//         burgerOut();
//     else if (event.originalEvent.changedTouches[0].pageX - touchStartX <= -100 && !condition)
//         burgerIn();
// })