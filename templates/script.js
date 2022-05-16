const mode = document.querySelector(".ball");
const imgLog = document.querySelector(".logo_inner");
const imgmode = document.querySelector(".modeSN");

mode.addEventListener("click", function () {
  document.body.classList.toggle("dark");

  if (imgLog.src === "http://127.0.0.1:5500/Fornt-end/img/logo_1.jpg") {
    imgLog.src = "/Fornt-end/img/logonoche_1.jpg";
  } else {
    imgLog.src = "/Fornt-end/img/logo_1.jpg";
  }
  if (imgmode.src === "http://127.0.0.1:5500/Fornt-end/img/sun.png") {
    imgmode.src = "/Fornt-end/img/half-moon.png";
  } else {
    imgmode.src = "/Fornt-end/img/sun.png";
  }

  if (document.body.classList.contains("dark")) {
    localStorage.setItem("dark-mode", "true");
  } else {
    localStorage.setItem("dark-mode", "false");
  }
});

if (localStorage.getItem("dark-mode") === "true") {
  document.body.classList.add("dark");
  imgmode.src = "/Fornt-end/img/half-moon.png";
  imgLog.src = "/Fornt-end/img/logonoche_1.jpg";
} else {
  document.body.classList.remove("dark");
}
