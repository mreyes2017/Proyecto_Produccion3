let cantidad_semanas=document.getElementById('cantidad_semanas');
const formulario=document.querySelector('#prueba');
const c=document.querySelector("#cantidad_semanas");
const demanda= document.getElementById('demanda');
    
   // método js que se dispara al momento que el usuario toca la tecla enter
   c.onkeydown = function(e){
    //var ev = document.all ? window.event : e;
    if(e.keyCode==13) {
       const x=document.querySelector("#cantidad_semanas").setAttribute("disabled",'disabled');
       demanda.disabled=false;
      
    }
}


    demanda.onkeydown=function(event) {
       if (event.keyCode == 13) {
           alert("estamos aqui");
       }
   };
 
 



function ingresar_datos() {
savearray = [];
var array = [];  
    for (var i = 0; i < cantidad_semanas.value; i++) {               
     array[i] = parseFloat(document.getElementById("demanda"+(i+1)).value);
            savearray.push (array[i]);  
     }     
}         
 