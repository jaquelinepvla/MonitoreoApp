'use strict'

$(document).ready(function(){
    console.log("hola");
});

//urls servidor
let urlMonitoreo ="http://127.0.0.1:8000/";
let urlPronostico = "http://127.0.0.1:8000/Prediccion/";

//Etiquetas html
let tablaM = "tablaM";
let tablaP = "tablaP";

function getData(){
    $.get(urlPronostico, function getDatos(response){
        return response

    });
}

//Tablas
function tablas(url, tabla){

    //Recolectar datos del servidor
    $.get(url, function getDatos(response){
        console.log("Se ha actualizado");    
        
        let tablaMonitoreo = document.getElementById(tabla);
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
}

//Generar tablas html


//tablas(urlMonitoreo, tablaM);
//data = getData();
//console.log(data);
//tablas(urlPronostico, tablaP);
setInterval(tablas, 10000, urlMonitoreo, tablaM)

