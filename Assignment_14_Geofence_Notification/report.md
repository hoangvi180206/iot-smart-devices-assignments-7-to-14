# Assignment 14 Report - Send Notifications Using Twilio

## Objective

The objective of this assignment is to send a notification when GPS coordinates are inside a geofence. The notification can be an SMS or email. In this implementation, I used the SMS option with Twilio.

## Geofence Logic

The geofence is represented by a target latitude and longitude. The function calculates the distance between the current GPS coordinate and the target coordinate. If the distance is less than or equal to the geofence radius, the coordinate is considered inside the geofence.

## Example Configuration

```text
Target latitude: 10.762622
Target longitude: 106.660172
Radius: 500 meters
```

## Notification Rule

This assignment sends a notification only when the GPS coordinate is inside the geofence.

```text
if distance <= radius:
    send SMS notification
else:
    do not send SMS
```

## Result

When the GPS coordinates are inside the geofence, the Azure Function creates a Twilio SMS output message.

## Conclusion

This assignment shows how geofencing can be combined with cloud functions and notification services. It is useful for transport systems because it can alert users when a vehicle arrives near a destination.
