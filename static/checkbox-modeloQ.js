const inputsCosto = document.querySelector("#checkeadoTasa");
const cuadroTasa = document.querySelector("#checkTasa");

cuadroTasa.addEventListener("click", function () {
  inputsCosto.toggleAttribute("disabled");
});
