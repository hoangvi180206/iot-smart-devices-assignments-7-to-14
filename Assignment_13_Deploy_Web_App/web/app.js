// Assignment 13 - Location visualization example

const sampleLocation = {
  latitude: 10.762622,
  longitude: 106.660172,
  speed_kmh: 41.48,
  altitude_m: 10.5,
  timestamp: new Date().toISOString()
};

function loadLocation() {
  const output = document.getElementById('location-output');
  output.textContent = JSON.stringify(sampleLocation, null, 2);

  const map = document.getElementById('map');
  map.textContent = `Location: ${sampleLocation.latitude}, ${sampleLocation.longitude}`;
}

function checkConfig() {
  if (!window.APP_CONFIG || !window.APP_CONFIG.MAP_SUBSCRIPTION_KEY) {
    console.warn('Map subscription key is missing. Use config.js locally or cloud configuration when deployed.');
  }
}

checkConfig();
loadLocation();
