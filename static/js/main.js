// Initialize the map and set a world fit view
var map = L.map('map').fitWorld();

// Add OpenStreetMap tile layer
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 25,
    attribution: '© OpenStreetMap'
}).addTo(map);

// Use the locate method to get the user's location
map.locate({
    setView: true,   // Automatically set the map view to the user's location
    maxZoom: 16,     // Zoom level when the user's location is found
    enableHighAccuracy: true, // Maximum accuracy
    timeout: 10000,  // Timeout for location request
    maximumAge: 0     // Don't use cached location
});

// Handle the locationfound event when user's location is obtained
map.on('locationfound', function(e) {
    var lat = e.latlng.lat;
    var lon = e.latlng.lng;

    // Add a marker at the user's location
    var userMarker = L.marker([lat, lon]).addTo(map);
    userMarker.bindPopup("You are here").openPopup();

    // Optional: add a circle around the location with accuracy radius
    var radius = e.accuracy;
    L.circle([lat, lon], radius).addTo(map);
});

// Handle the locationerror event in case of failure
map.on('locationerror', function(e) {
    console.log("Location error: " + e.message);
});

// Mouse position control (bottom-left corner)
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
    const lat = e.latlng.lat.toFixed(4); // Rounded latitude
    const lng = e.latlng.lng.toFixed(4); // Rounded longitude
    mousePositionControl.getContainer().innerHTML = `Lat: ${lat}, Lng: ${lng}`;
});

// Adding campus image overlay
var imageUrl = 'static/images/campus_ground_floor.png',
    imageBounds = [[30.23468, 31.70376], [30.23206, 31.70784]];
L.imageOverlay(imageUrl, imageBounds).addTo(map);
