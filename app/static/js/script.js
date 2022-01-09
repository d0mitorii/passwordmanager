$(document).ready(function() {

    var buttons = document.getElementsByClassName("copyBtn");
    var popuptext = document.getElementsByClassName("popuptext");

    for (let i = 0; i < buttons.length; i++) {
        buttons[i].addEventListener("click", function() {
            navigator.clipboard.writeText($(this).val());
            popuptext[i].style.transition = '0.5s';
            popuptext[i].style.opacity = 1;
            setTimeout(hiddenText, 500, popuptext[i]);
        });
    }

    function hiddenText(popuptext) {
        popuptext.style.opacity = 0;
        popuptext.style.transition = '1s';

    }
});