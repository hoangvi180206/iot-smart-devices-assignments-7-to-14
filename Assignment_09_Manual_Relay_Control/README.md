# Assignment 09 - Manual Relay Control

## Goal

Add two HTTP triggers to an Azure Functions App: one to turn the relay on and one to turn the relay off.

## Files

- `code/relay_on/__init__.py`
- `code/relay_on/function.json`
- `code/relay_off/__init__.py`
- `code/relay_off/function.json`
- `report.md`
- `screenshots/`

## Local test commands

Start the Functions app:

```bash
func start
```

Then test in the browser:

```text
http://localhost:7071/api/relay_on
http://localhost:7071/api/relay_off
```

## Note

The sample code returns a message and shows where the IoT device command should be sent. Replace the placeholder command section with your own IoT Hub direct method or device command code if required.
