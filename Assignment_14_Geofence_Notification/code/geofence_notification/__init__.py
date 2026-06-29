import json
import math
import logging
import azure.functions as func

TARGET_LAT = 10.762622
TARGET_LON = 106.660172
RADIUS_METERS = 500


def haversine_distance(lat1, lon1, lat2, lon2):
    radius_earth = 6371000
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    a = (
        math.sin(delta_phi / 2) ** 2
        + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) ** 2
    )
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return radius_earth * c


def main(event: func.EventHubEvent, message: func.Out[str]):
    body = event.get_body().decode("utf-8")
    logging.info("GPS telemetry received: %s", body)

    telemetry = json.loads(body)
    latitude = float(telemetry["latitude"])
    longitude = float(telemetry["longitude"])

    distance = haversine_distance(latitude, longitude, TARGET_LAT, TARGET_LON)
    logging.info("Distance to geofence center: %.2f meters", distance)

    if distance <= RADIUS_METERS:
        sms_text = (
            f"IoT alert: device is inside the geofence. "
            f"Distance: {distance:.2f} meters."
        )
        message.set(sms_text)
        logging.info("SMS notification created")
    else:
        logging.info("Device is outside geofence. No SMS sent.")
