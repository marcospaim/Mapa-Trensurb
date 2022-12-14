
var map = L.map('map').setView([-30, -51.19], 13);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '© OpenStreetMap'
}).addTo(map);

//pane popup de informações
map.createPane('info');
map.getPane('info').style.zIndex = 999;

var layerGroup = L.layerGroup().setZIndex(3).addTo(map);
map.createPane('labels');
map.getPane('labels').style.zIndex = 700;

//caminho do trem
map.createPane('caminho');
map.getPane('caminho').style.zIndex = 300;
fetchPath()

// Estacoes
fetchEstacoes();


function radians_to_degrees(radians)
{
  var pi = Math.PI;
  return radians * (180/pi);
}

buscarGPS()
setInterval(buscarGPS, 4000);

function buscarGPS()
{
    fetch(`/gps`)
                    .then((res) => {
                        if (res.status !== 200) {
                            console.log(res.status);
                            return
                        }
                        res.json().then((data) => {
                                console.log(data)
                                atualizaMapa(data)
                            })
                            .catch((err) => console.log(err))
                    })
}
function atualizaMapa(data)
{
    data = data.Coordenadas
    // remove all the markers in one go
    layerGroup.clearLayers();

    for (x in data){
        lat = radians_to_degrees(data[x].Latitude)
        lon = radians_to_degrees(data[x].Longitude)
        if (data[x].Orientacao > 120 && data[x].Orientacao < 300){ //sentido sul/mercado
            xcolor = 'darkblue'
        }
        else {
            xcolor = 'darkred'
        }
        var redMarker = L.AwesomeMarkers.icon({icon: 'train', prefix: 'fa', markerColor: xcolor})

        var popup = L.popup([lat, lon],{pane: 'info', content: `<b>${data[x].Elemento}</b><br>Velocidade: ${data[x].Velocidade} km/h<br>Sentido: ${data[x].sentido}<br>Data e hora: ${data[x]['Data e Hora']}`})
    
        var trainMarker = L.marker([lat, lon], {
            icon: redMarker,
            pane: 'labels'
        })
        .bindPopup(popup)
        .on('mouseover', function (e) {
            this.openPopup();
        })
        .addTo(layerGroup);
    }
}

function fetchEstacoes()
{
    fetch(`/estacoes`)
                    .then((res) => {
                        if (res.status !== 200) {
                            console.log(res.status);
                            return
                        }
                        res.json().then((data) => {
                                console.log(data)
                                for(line in data){
                                    console.log(data[line][0])
                                    L.circleMarker([data[line][1], data[line][2]], {
                                        color: 'black',
                                        fillColor: 'white',
                                        fillOpacity: 1,
                                        weight: 2,
                                        radius: 15
                                    }).addTo(map);
                                    
                                    var text = L.tooltip({
                                        //pane: 'labels',
                                        permanent: true,
                                        direction: 'center',
                                        className: 'text',
                                    })
                                    .setContent(data[line][0])
                                    .setLatLng([data[line][1], data[line][2]]);
                                    text.addTo(map);
                                }
                            })
                            .catch((err) => console.log(err))
                    })
}

function fetchPath()
{
    fetch(`/path`)
                    .then((res) => {
                        if (res.status !== 200) {
                            console.log(res.status);
                            return
                        }
                        res.json().then((data) => {        
                                for(let i = 1; i < Object.keys(data).length; i++){
                                    //console.log(data[i][0], data[i][1])
                                    var pointA = new L.LatLng(data[i][0], data[i][1]);
                                    var pointB = new L.LatLng(data[i+1][0], data[i+1][1]);
                                    var pointList = [pointA, pointB];

                                    var firstpolyline = new L.Polyline(pointList, {
                                        pane: 'caminho',
                                        color: 'red',
                                        weight: 3,
                                        //opacity: 0.5,
                                        smoothFactor: 1
                                    });
                                    firstpolyline.addTo(map);
                                }
                                
                            })
                            .catch((err) => console.log(err))
                    })
}