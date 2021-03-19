window.onscroll = function() {myFunction()};

let nav = document.getElementById("sticky-nav");
let sticky = nav.offsetTop;

function myFunction() {
  if (window.pageYOffset > sticky) {
    nav.classList.add("fixed-top");
  } else {
    nav.classList.remove("fixed-top");
  }
}