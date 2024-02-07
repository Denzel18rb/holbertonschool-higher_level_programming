document.addEventListener("DOMContentLoaded", function () {
    const toogleHeader = document.querySelector("#toggle_header");
    const Header = document.querySelector("header");
    
    toogleHeader.addEventListener("click", function (){

    if(Header.getAttribute('class')=='green'){
            Header.setAttribute('class','red');
    }
    else if(Header.getAttribute('class')=='red'){
            Header.setAttribute('class','green');
    }
    });
})
