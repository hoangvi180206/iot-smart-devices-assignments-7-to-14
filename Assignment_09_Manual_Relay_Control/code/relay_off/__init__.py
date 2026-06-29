import logging
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("relay_off HTTP trigger processed a request.")

    # TODO: Replace this placeholder with your IoT Hub command/direct method.
    # Example idea:
    # send_device_command(device_id="plant-device", command_name="relay_off")

    return func.HttpResponse(
        "Relay OFF command sent successfully.",
        status_code=200
    )
