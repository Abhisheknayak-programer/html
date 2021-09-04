////////////////////////
// NAVIGATION BAR //
////////////////////////
const navLinks = document.querySelectorAll(".nav__links");
const dropDownNav = document.querySelector(".dropDown");
navLinks.forEach((Element) =>
  Element.addEventListener("mousedown", () => {
    dropDownNav.classList.toggle("navDisabled");
  })
);

////////////////////////
// IMAGE MANIPULATOR //
////////////////////////
const ImgBox = document.querySelector("#our_image");
const btn1 = document.querySelector(".btn1");
const btn2 = document.querySelector(".btn2");
const btn3 = document.querySelector(".btn3");
const btn4 = document.querySelector(".btn4");
const btn5 = document.querySelector(".btn5");
const btn6 = document.querySelector(".btn6");
let url1 =
  "https://dukemfg.com/wp-content/uploads/2014/05/Insignia-Slider-25.png";
let url2 =
  "https://dukemfg.com/wp-content/uploads/2014/05/Insignia-Slider-26.png";
let url3 =
  "https://dukemfg.com/wp-content/uploads/2014/05/Insignia-Slider-27.png";
let url4 =
  "https://dukemfg.com/wp-content/uploads/2014/05/Insignia-Slider-28.png";
let url5 =
  "https://dukemfg.com/wp-content/uploads/2014/05/Insignia-Slider-29.png";
let url6 =
  "https://dukemfg.com/wp-content/uploads/2014/05/Insignia-Slider-30.png";

btn1.addEventListener("click", () => {
  ImgBox.setAttribute("src", "");
  ImgBox.setAttribute("src", `${url1}`);
});

btn2.addEventListener("click", () => {
  ImgBox.setAttribute("src", "");
  ImgBox.setAttribute("src", `${url2}`);
});

btn3.addEventListener("click", () => {
  ImgBox.setAttribute("src", "");
  ImgBox.setAttribute("src", `${url3}`);
});

btn4.addEventListener("click", () => {
  ImgBox.setAttribute("src", "");
  ImgBox.setAttribute("src", `${url4}`);
});

btn5.addEventListener("click", () => {
  ImgBox.setAttribute("src", "");
  ImgBox.setAttribute("src", `${url5}`);
});

btn6.addEventListener("click", () => {
  ImgBox.setAttribute("src", "");
  ImgBox.setAttribute("src", `${url6}`);
});
