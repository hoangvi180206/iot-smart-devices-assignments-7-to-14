# Assignment 10 Report - Build a New IoT Device

## Objective

The objective of this assignment is to build a new IoT device that uses both a sensor and an actuator. The device sends telemetry to IoT Hub, and serverless code reacts to the telemetry to control the actuator.

## Device Design

For this assignment, I designed a battery monitoring and protection device.

| Component | Role |
|---|---|
| ESP32 | Main microcontroller |
| INA226 | Measures voltage and current |
| DS18B20 | Measures battery temperature |
| Relay module | Disconnects the load when the battery is unsafe |
| Azure IoT Hub | Receives telemetry and sends commands |
| Azure Function | Processes telemetry and controls the relay |

## System Flow

```text
Sensor readings -> ESP32 -> IoT Hub -> Azure Function -> Relay command -> ESP32 -> Relay
```

## Telemetry Data

The ESP32 sends telemetry data such as:

```json
{
  "voltage": 4.15,
  "current": 0.85,
  "temperature": 34.2,
  "risk": "normal"
}
```

## Serverless Logic

The Azure Function receives telemetry events. If the voltage, current, or temperature becomes unsafe, the function sends a command to turn off the relay.

Example logic:

```text
if voltage > 4.2 or temperature > 45:
    send relay_off command
else:
    keep relay on
```

## Conclusion

This IoT device improves safety by monitoring battery conditions and automatically controlling a relay when abnormal telemetry is detected.
