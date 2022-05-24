let cantidad_semanas=document.getElementById('cantidad_semanas');
const formulario=document.querySelector('#prueba');
const c=document.querySelector("#cantidad_semanas");
const demanda= document.getElementById('demanda[]');
    
   // método js que se dispara al momento que el usuario toca la tecla enter
   c.onkeydown = function(e){
    //var ev = document.all ? window.event : e;
    if(e.keyCode==13) {
        //desabilito el input donde ingrese la cntidad de semanas
       const x=document.querySelector("#cantidad_semanas").setAttribute("disabled",'disabled');
       //habilito el input 
       demanda.disabled=false;
      
    }
}


    demanda.onkeydown=function(event) {
       if (event.keyCode == 13) {
       // alert(cantidad_semanas.value);
       demanda.disabled=false;
        
           
               
       }
   };
 
   





 