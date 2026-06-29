# Assignment 11 Report - GPS Data

## Objective

The objective of this assignment is to collect more data from GPS/NMEA messages. Besides latitude and longitude, GPS data can also include UTC time, date, altitude, and speed.

## Data Used

I used example NMEA sentences to parse GPS information:

- `$GPGGA` for position, time, fix quality, satellites, and altitude
- `$GPRMC` for position, time, date, and speed

## Parsed Fields

| Field | Meaning |
|---|---|
| Latitude | North/South position |
| Longitude | East/West position |
| UTC time | Time from GPS satellites |
| Date | Date from GPS data |
| Speed | Speed over ground |
| Altitude | Elevation above sea level |

## Result

The script parses the NMEA sentences and prints structured GPS data. This information can be sent as telemetry to IoT Hub for vehicle or asset tracking.

## Conclusion

GPS data is useful for IoT transport systems because it gives real-time location and movement information. Adding fields such as speed, time, and altitude makes the telemetry more useful for tracking and analysis.
