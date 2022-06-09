'use strict'

$(document).ready(function(){
    console.log("hola");
});

//urls servidor
let urlCharM ="http://127.0.0.1:8000/monitoreo/";

//Etiquetas html
let mostrarfecha = document.getElementById('fecha_m');
let mostrartemp = document.getElementById('dato_T');
let mostraroxig = document.getElementById('dato_O');
let chartM = "chartM";


var dataCm = $.get(urlCharM);

//==================================Grafica=================================================
var myChart;
const ctx = document.getElementById(chartM).getContext('2d');
function updateChart(d1, d2, label){

    myChart.data.datasets[0].data=d1;
    myChart.data.datasets[1].data=d2;
    myChart.data.labels = label;
    myChart.update();
}

function graficar(){
   
        
        
       
        myChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: 0,
                datasets: [{
                    label: 'Temperatura °C',
                    data: 0,
                    backgroundColor: 'rgba(255, 99, 132, 0.2)',
                    borderColor: 'rgba(255, 99, 132, 1)',
                    tension: 0.4,
                    yAxisID: 'y'
                },{label: 'Oxígeno mg/L',
                    data: 0,
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

    }


//Tablas
graficar();
setInterval(()=>{
    dataCm.done(function(resp){
        var Xhr=resp['hora']
        var Xf = resp['fecha']
        var Yoxig = resp['oxigeno']
        var Ytemp = resp['temperatura']
        
        var lastHr = Xhr[Xhr.length-1];
        var lastXf = Xf[Xf.length-1];
        var lastOxig = Yoxig[Yoxig.length-1];
        var lastTemp = Ytemp[Ytemp.length-1];
        //console.log(lastHr, lastOxig, lastTemp);
        var nuevoArray = new Array();
        var nuevoArray = [lastHr, lastOxig, lastTemp]; 
        //console.log(datos, typeof datos);
        //mostrarfecha.innerHTML = 
        mostraroxig.innerHTML = lastXf + ' - ' + lastHr + '<br>'  + 'Oxígeno disuelto: ' + lastOxig + ' mg/L' + '<br>' + 'Temperatura: ' + lastTemp + ' °C';
        //mostrartemp.innerHTML = lastTemp;
        console.log(lastHr, lastOxig, lastTemp);
   
        updateChart(Yoxig, Ytemp, Xhr);
        
        //var arr = Object.entries(datos);
        /*var tsrt = document.createTextNode(lastXf + '-' + lastHr);
        var str = document.createTextNode('Oxígeno disuelto: ' + lastOxig + ' mg/L' + '   '+ 'Temperatura: ' + lastTemp + '°C');
        document.getElementById("fecha_m").appendChild(tsrt);
        document.getElementById("dato_m").appendChild(str);    */             
});
}, 1000);



/*
setInterval(()=>{

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
    
}, 1000);*/

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



/*
setInterval(()=>{
    var datos=[];
    console.log(typeof datos);
    var datos = resumenM();
    //console.log(datos, typeof datos);

    var fecha = datos['0'];
    var oxigeno = datos['2'];
    var temperatura = datos['3'];
    mostrarfecha.innerHTML = fecha;
    mostraroxig.innerHTML = oxigeno;
    mostrartemp.innerHTML = temperatura

}, 1000);*/



