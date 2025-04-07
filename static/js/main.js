//var map = L.map('map').setView([51.505, -0.09], 13);
var map = L.map('map').fitWorld();

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '© OpenStreetMap'
}).addTo(map);

map.locate({setView: true, maxZoom: 16});

function onLocationFound(e) {
    var radius = e.accuracy;

    L.marker(e.latlng).addTo(map)
        .bindPopup("You are within " + radius + " meters from this point").openPopup();

    L.circle(e.latlng, radius).addTo(map);
}

map.on('locationfound', onLocationFound);
const mousePositionControl = L.control({ position: 'bottomleft' });
 mousePositionControl.onAdd = function() {
            const div = L.DomUtil.create('div', 'leaflet-control-mouseposition');
            div.innerHTML = 'Lat: , Lng: ';
            return div;
        };

        // Add the custom control to the map
        mousePositionControl.addTo(map);

        // Update the mouse position on the map when it moves
        map.on('mousemove', function(e) {
            const lat = e.latlng.lat.toFixed(4); // Get latitude and round it
            const lng = e.latlng.lng.toFixed(4); // Get longitude and round it
            mousePositionControl.getContainer().innerHTML = `Lat: ${lat}, Lng: ${lng}`;
        });

var imageUrl = 'static/images/tst_home.png',
    imageBounds = [[30.0513, 31.2424], [30.0474, 31.2466]];
L.imageOverlay(imageUrl, imageBounds).addTo(map);
