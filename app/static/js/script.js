$(document).ready(function() {
    const btn = document.getElementById("btn_add");

    btn.addEventListener("click", ViewFormOfCreation);

    function ViewFormOfCreation() {
        const form = document.getElementsByClassName("form")[0].style = "display: flex";
        const button = document.getElementsByClassName("button")[0].style = "display: none";
    }
});