///////////////////////////////////
// REAL USER LOGIN TO THE PAGE //
///////////////////////////////////
const username = document.querySelector("#username");
const password = document.querySelector("#password");
const AdminLoginBtn = document.querySelector(".Admin_LoginBtn");

const ClearInputs = () => {
  username.value = "";
  password.value = "";
};

AdminLoginBtn.addEventListener("click", (e) => {
  e.preventDefault();

  if (username.value === "DS_GROUP" && password.value === "DSDSDS") {
    ClearInputs();
    alert("Welcome to Ds group");
    window.open("admin.html");
  } else {
    ClearInputs();
    alert("Wrong Password! Try Again");
  }
});

///////////////////////////////////
// ADMIN PANNEL  //
///////////////////////////////////
