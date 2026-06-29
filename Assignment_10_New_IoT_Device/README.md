# Assignment 10 - Build a New IoT Device

## Goal

Build a new IoT device using a sensor and an actuator. Send telemetry to IoT Hub and use serverless code to control the actuator.

## Proposed device

Battery monitoring and protection device:

- Sensor: INA226 voltage/current sensor and/or DS18B20 temperature sensor
- Actuator: relay module
- Microcontroller: ESP32
- Cloud: Azure IoT Hub
- Serverless logic: Azure Function triggered by telemetry

## Files

- `code/esp32_battery_monitor/esp32_battery_monitor.ino`
- `code/azure_function_telemetry_trigger/__init__.py`
- `code/azure_function_telemetry_trigger/function.json`
- `report.md`
- `screenshots/`

## Note

Replace all placeholder values before testing. Do not commit real connection strings or secrets.
