import logging
import azure.functions as func


def main(event: func.EventHubEvent, outputblob: func.Out[str]):
    body = event.get_body().decode("utf-8")
    logging.info("Location telemetry received: %s", body)

    # The output binding writes this string to Blob Storage.
    outputblob.set(body)
