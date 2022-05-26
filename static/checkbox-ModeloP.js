const inputsDesv = document.querySelector("#CDesvEstandar");
const cuadroDesv = document.querySelector("#DesvEstandar");

cuadroDesv.addEventListener("click", function () {
  inputsDesv.toggleAttribute("disabled");
});
