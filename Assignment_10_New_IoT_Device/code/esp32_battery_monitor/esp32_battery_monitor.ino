/*
  Assignment 10 - ESP32 Battery Monitoring Device
  Replace placeholder values before testing.

  Sensor examples:
  - INA226 for voltage/current
  - DS18B20 for temperature

  Actuator:
  - Relay module
*/

#include <WiFi.h>
#include <ArduinoJson.h>

#define RELAY_PIN 5

const char* WIFI_SSID = "YOUR_WIFI_SSID";
const char* WIFI_PASSWORD = "YOUR_WIFI_PASSWORD";

// TODO: Add IoT Hub/MQTT connection settings here.
// Do not commit real connection strings or keys.

float readVoltage() {
  // TODO: Replace with INA226 reading.
  return 4.10;
}

float readCurrent() {
  // TODO: Replace with INA226 reading.
  return 0.75;
}

float readTemperature() {
  // TODO: Replace with DS18B20 reading.
  return 32.5;
}

String calculateRisk(float voltage, float current, float temperature) {
  if (voltage > 4.2 || temperature > 45.0 || current > 2.0) {
    return "high";
  }
  if (voltage > 4.1 || temperature > 40.0 || current > 1.5) {
    return "warning";
  }
  return "normal";
}

void setRelay(bool enabled) {
  digitalWrite(RELAY_PIN, enabled ? HIGH : LOW);
}

void sendTelemetry(float voltage, float current, float temperature, String risk) {
  StaticJsonDocument<256> doc;
  doc["voltage"] = voltage;
  doc["current"] = current;
  doc["temperature"] = temperature;
  doc["risk"] = risk;

  char payload[256];
  serializeJson(doc, payload);

  Serial.print("Telemetry: ");
  Serial.println(payload);

  // TODO: Publish payload to Azure IoT Hub.
}

void setup() {
  Serial.begin(115200);
  pinMode(RELAY_PIN, OUTPUT);
  setRelay(true);

  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  Serial.print("Connecting to WiFi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println(" connected");
}

void loop() {
  float voltage = readVoltage();
  float current = readCurrent();
  float temperature = readTemperature();
  String risk = calculateRisk(voltage, current, temperature);

  if (risk == "high") {
    setRelay(false);
  } else {
    setRelay(true);
  }

  sendTelemetry(voltage, current, temperature, risk);
  delay(5000);
}
