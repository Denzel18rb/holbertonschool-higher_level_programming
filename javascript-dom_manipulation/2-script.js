document.addEventListener("DOMContentLoaded", function () {
    const redHeader = document.querySelector("#red_header");

    redHeader.addEventListener("click", function () {
        const headerElement = document.querySelector("header");
        headerElement.setAttribute('class','red');
    });
});
