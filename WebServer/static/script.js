function fetchSensorDataAndUpdateUI() {
  fetch('/latest-sensor-data')
    .then(response => response.json())
    .then(data => {
      document.getElementById('room-temp').textContent = data.Temperature ? `${data.Temperature}°C` : '--';
      document.getElementById('room-humidity').textContent = data.Humidity ? `${data.Humidity}%` : '--';
      document.getElementById('room-light').textContent = data.Light ? `${data.Light} lux` : '--';
      document.getElementById('patient-heartbeat').textContent = data.HeartRate ? `${data.HeartRate} BPM` : '--';
      document.getElementById('patient-oxygen').textContent = data.BloodOxygen ? `${data.BloodOxygen}%` : '--';
      document.getElementById('body-temp').textContent = data.BodyTemperature ? `${data.BodyTemperature}°C` : '--';
    })
    .catch(error => console.error('Error fetching sensor data:', error));
}

function submitRule() {
  // Prepare data from form fields
  const ruleData = {
    name: document.getElementById('rule-name').value,
    action: document.getElementById('action-dropdown').value,
    actuator: document.getElementById('actuator-dropdown').value,
    comparison: document.getElementById('comparison-dropdown').value,
    sensor: document.getElementById('sensor-dropdown').value,
    value: document.getElementById('value-input').value,
  };

  // Send rule data to the server
  fetch('/submit-rule', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(ruleData)
  })
  .then(response => response.json())
  .then(data => {
    console.log(data);
    // Handle response data, such as confirming rule submission
  })
  .catch(error => console.error('Error setting rule:', error));
}

// Event listener for the rule submission form
document.getElementById('rule-form').addEventListener('submit', function(event) {
  event.preventDefault(); // Prevent the form from submitting the traditional way
  submitRule();
});




// Fetch data every 5 seconds
setInterval(fetchSensorDataAndUpdateUI, 5000);

// Initial fetch
fetchSensorDataAndUpdateUI();
