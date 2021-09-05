////////////////////////
// NAVIGATION BAR //
////////////////////////
const navLinks = document.querySelectorAll(".nav__links");
const dropDownNav = document.querySelector(".dropDown");
navLinks.forEach((Element) =>
  Element.addEventListener("mouseover", () => {
    dropDownNav.classList.remove("navDisabled");
  })
);

navLinks.forEach((Element) => {
  Element.addEventListener("mouseout", function () {
    dropDownNav.classList.add("navDisabled");
  });
});
const dropDowncol1 = document.querySelector(".dropDown__col__1");
const dropDowncol2 = document.querySelector(".dropDown__col__2");
const dropDowncol3 = document.querySelector(".dropDown__col__3");

const goOut = function () {
  dropDowncol2.style.opacity = "0";
  dropDowncol3.style.opacity = "0";
};

dropDowncol1.addEventListener("mouseover", () => {
  dropDowncol2.style.opacity = "1";
});

dropDowncol2.addEventListener("mouseover", () => {
  dropDowncol2.style.opacity = "1";
  dropDowncol3.style.opacity = "1";
});

dropDowncol3.addEventListener("mouseover", () => {
  dropDowncol2.style.opacity = "1";
  dropDowncol3.style.opacity = "1";
});

dropDownNav.addEventListener("mouseover", () => {
  dropDownNav.classList.remove("navDisabled");
});

dropDownNav.addEventListener("mouseout", () => {
  dropDownNav.classList.add("navDisabled");
  goOut();
});

const navLinkManipulate_1 = document.querySelector("#nav__link_1");
const navLinkManipulate_2 = document.querySelector("#nav__link_2");
const navLinkManipulate_3 = document.querySelector("#nav__link_3");
const navLinkManipulate_4 = document.querySelector("#nav__link_4");
const navLinkManipulate_5 = document.querySelector("#nav__link_5");
const navLinkManipulate_6 = document.querySelector("#nav__link_6");
const ManipulatedLInks = document.querySelectorAll(".ManipulatedLInks");
const colOneOpen = document.querySelector("#colOneOpen");
const colTwoOpen = document.querySelector("#colTwoOpen");

navLinkManipulate_1.addEventListener("mouseover", () => {
  ManipulatedLInks.forEach(
    (Element) => (Element.textContent = "Random Link 1")
  );
});

navLinkManipulate_2.addEventListener("mouseover", () => {
  ManipulatedLInks.forEach(
    (Element) => (Element.textContent = "Random Link 2")
  );
});

navLinkManipulate_3.addEventListener("mouseover", () => {
  ManipulatedLInks.forEach(
    (Element) => (Element.textContent = "Random Link 3")
  );
});

navLinkManipulate_4.addEventListener("mouseover", () => {
  ManipulatedLInks.forEach(
    (Element) => (Element.textContent = "Random Link 4")
  );
});

navLinkManipulate_5.addEventListener("mouseover", () => {
  ManipulatedLInks.forEach(
    (Element) => (Element.textContent = "Random Link 5")
  );
});

navLinkManipulate_6.addEventListener("mouseover", () => {
  ManipulatedLInks.forEach(
    (Element) => (Element.textContent = "Random Link 6")
  );
});

dropDowncol2.style.opacity = "0";
dropDowncol3.style.opacity = "0";

colOneOpen.addEventListener("mouseover", () => {
  dropDowncol2.style.opacity = "1";
});

colTwoOpen.addEventListener("mouseover", () => {
  dropDowncol3.style.opacity = "1";
});

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
