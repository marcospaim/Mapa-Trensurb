var map = L.map('map').setView([-30, -51.19], 13);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '© OpenStreetMap'
}).addTo(map);

var layerGroup = L.layerGroup().addTo(map);

var circle = L.circle([-30, -51.19], {
    color: 'red',
    fillColor: '#f03',
    fillOpacity: 1,
    radius: 40
}).addTo(layerGroup);

function radians_to_degrees(radians)
{
  var pi = Math.PI;
  return radians * (180/pi);
}
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
        console.log(data[x].Latitude)
        lat = radians_to_degrees(data[x].Latitude)
        lon = radians_to_degrees(data[x].Longitude)
        if (data[x].Orientacao > 120){ //sentido sul/mercado
            xcolor = 'blue'
        }
        else {
            xcolor = 'red'
        }
        var circle = L.circleMarker([lat, lon], {
            color: xcolor,
            fillColor: xcolor,
            fillOpacity: 1,
            radius: 8
        }).bindPopup(`<b>${data[x].Elemento}</b><br>Velocidade: ${data[x].Velocidade}<br>Orientação: ${data[x].Orientacao}<br>Data e hora: ${data[x]['Data e Hora']}`)
        .on('mouseover', function (e) {
            this.openPopup();
        })
        .addTo(layerGroup);
    }
}