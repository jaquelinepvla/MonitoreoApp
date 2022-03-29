$(document).ready(function(){
    console.log("hola");
});

//============ Recolectar datos del servidor para el monitoreo==============

$.get("http://127.0.0.1:8000/", function(response){
console.log(response);

//TABLA 
let tablaMonitoreo = document.getElementById('tablaM');
let cuerpoTabla = document.createElement('tbody');

         
    response.forEach((element) => {
        let fila = document.createElement('tr');
                    
        let td = document.createElement('td');
        td.innerText = element.O;
        fila.appendChild(td);
                    
        td = document.createElement('td');
        td.innerText = element.temp;
        fila.appendChild(td);

        td = document.createElement('td');
        td.innerText = element.t;
        fila.appendChild(td);

        td = document.createElement('td');
        td.innerText = element.f;
        fila.appendChild(td);
        cuerpoTabla.appendChild(fila)
    
    });
                
tablaMonitoreo.appendChild(cuerpoTabla);
});


//=================Recolectar datos del servidor para el pronóstico============

$.get("http://127.0.0.1:8000/Prediccion/", function(response){
console.log(response);

//TABLA
let tablaMonitoreo = document.getElementById('tablaP');
let cuerpoTabla = document.createElement('tbody');

          
    response.forEach((element) => {
        let fila = document.createElement('tr');
                    
        let td = document.createElement('td');
        td.innerText = element.O;
        fila.appendChild(td);
                    
        td = document.createElement('td');
        td.innerText = element.temp;
        fila.appendChild(td);

        td = document.createElement('td');
        td.innerText = element.t;
        fila.appendChild(td);

        td = document.createElement('td');
        td.innerText = element.f;
        fila.appendChild(td);
        cuerpoTabla.appendChild(fila)
    
    });
                
tablaMonitoreo.appendChild(cuerpoTabla);
});


