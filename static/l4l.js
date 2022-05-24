let cantidad_semanas=document.getElementById('cantidad_semanas');
const formulario=document.querySelector('#formulario');
const c=document.querySelector("#cantidad_semanas");

    
   // método js que se dispara al momento que el usuario toca la tecla enter
   c.onkeydown = function(e){
    //var ev = document.all ? window.event : e;
    if(e.keyCode==13) {
       const x=document.querySelector("#cantidad_semanas").setAttribute("disabled",'disabled');
      agregar_input();
    }
}

function agregar_input(){
   formulario.innerHTML += "<label >Digite la demanda:</label><div class='field'><input type='number' id='demanda' name='demanda' required/></div>";
  }
  const demanda= document.querySelector("#demanda");
     demanda.keypress(function(event) {
        if (event.keyCode == 13) {
            alert("estamos aqui");
        }
    });



function ingresar_datos() {
savearray = [];
var array = [];  
    for (var i = 0; i < cantidad_semanas.value; i++) {               
     array[i] = parseFloat(document.getElementById("demanda"+(i+1)).value);
            savearray.push (array[i]);  
     }     
}         
 