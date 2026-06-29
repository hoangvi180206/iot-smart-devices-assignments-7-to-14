import logging
import json
import azure.functions as func


def main(event: func.EventHubEvent):
    body = event.get_body().decode("utf-8")
    logging.info("Telemetry received: %s", body)

    try:
        telemetry = json.loads(body)
    except json.JSONDecodeError:
        logging.error("Invalid telemetry JSON")
        return

    voltage = float(telemetry.get("voltage", 0))
    current = float(telemetry.get("current", 0))
    temperature = float(telemetry.get("temperature", 0))

    unsafe = voltage > 4.2 or current > 2.0 or temperature > 45.0

    if unsafe:
        logging.warning("Unsafe battery condition. Send relay_off command.")
        # TODO: Send cloud-to-device command or direct method to ESP32.
    else:
        logging.info("Battery condition normal.")
