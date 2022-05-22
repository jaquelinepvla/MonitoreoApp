'use strict'

$(document).ready(function(){
    console.log("hola");
});

//urls servidor
let urlMonitoreo ="http://127.0.0.1:8000/";
let urlCharM ="https://iotacuicola.herokuapp.com/monitoreo/";
let urlPronostico = "http://127.0.0.1:8000/Prediccion/";

//Etiquetas html
let tablaM = "tablaM";
let tablaP = "tablaP";
let chartM = "chartM";
let chartP = "chartP";

var dataM = $.get(urlMonitoreo);
var dataCm = $.get(urlCharM);

//Tablas
function resumenM(){
    dataCm.done(function(resp){
        var Xhr=resp['hora']
        var Xf = resp['fecha']
        var Yoxig = resp['oxigeno']
        var Ytemp = resp['temperatura']
        
        var lastHr = Xhr[Xhr.length-1];
        var lastXf = Xf[Xf.length-1];
        var lastOxig = Yoxig[Yoxig.length-1];
        var lastTemp = Ytemp[Ytemp.length-1];
        console.log(lastHr, lastOxig, lastTemp);
    
        var tsrt = document.createTextNode(lastXf + '-' + lastHr);
        var str = document.createTextNode('Oxígeno disuelto: ' + lastOxig + ' mg/L' + '   '+ 'Temperatura: ' + lastTemp + '°C');
        document.getElementById("fecha_m").appendChild(tsrt);
        document.getElementById("dato_m").appendChild(str); 

});

}

/*function tablas(){

    //Recolectar datos del servidor
    dataM.done(function (response){
     
        let tablaMonitoreo = document.getElementById(tablaM);
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
            td.innerText = element.f;
            fila.appendChild(td);

            cuerpoTabla.appendChild(fila)
            
        });
                        
        tablaMonitoreo.appendChild(cuerpoTabla);

    });
}*/

function grficar(){

    dataCm.done(function (resp){
        var Xhr=resp['hora']
        var Yoxig = resp['oxigeno']
        var Ytemp = resp['temperatura']
       
        console.log("JSON DATA:", Xhr, Yoxig, Ytemp);
        const ctx = document.getElementById(chartM).getContext('2d');
        const myChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: Xhr,
                datasets: [{
                    label: 'Temperatura °C',
                    data: Ytemp,
                    backgroundColor: 'rgba(255, 99, 132, 0.2)',
                    borderColor: 'rgba(255, 99, 132, 1)',
                    tension: 0.4,
                    yAxisID: 'y'
                },{label: 'Oxígeno mg/L',
                    data: Yoxig,
                    backgroundColor: 'rgba(0, 26, 104, 0.2)',
                    borderColor: 'rgba(0, 26, 104, 1)',
                    tension: 0.4,
                    yAxisID: 'o'
                }]
            },
            options: {
                layout:{
                padding:{
                    bottom: 30,
                    right: 20,
                    left: 20,
                    top:5
                    
                }
                
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        type: 'linear',
                        position: 'left'
                    },
                    o:{
                    beginAtZero: true,
                        type: 'linear',
                        position: 'right',
                        grid:{
                        drawOnChartArea: false

                        }

                    }
                }
            }
        }); 
    });
}


grficar();
resumenM();


