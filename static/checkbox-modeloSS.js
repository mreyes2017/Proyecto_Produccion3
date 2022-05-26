const inputsDesv = document.querySelector("#CDesvEstandar");
const cuadroDesv = document.querySelector("#DesvEstandar");
const inputs = document.querySelector("#checkeadoCostodePedir");
const cuadro = document.querySelector("#checkCostodePedir");

const inputsCosto = document.querySelector("#checkeadoTasa");
const cuadroTasa = document.querySelector("#checkTasa");

cuadroDesv.addEventListener("click", function () {
  inputsDesv.toggleAttribute("disabled");
});

cuadro.addEventListener("click", function () {
  inputs.toggleAttribute("disabled");
});

cuadroTasa.addEventListener("click", function () {
  inputsCosto.toggleAttribute("disabled");
});
