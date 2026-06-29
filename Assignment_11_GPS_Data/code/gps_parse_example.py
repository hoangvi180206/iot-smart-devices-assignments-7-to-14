# Assignment 11 - Parse GPS/NMEA data
# This script parses example GPGGA and GPRMC sentences.


def nmea_to_decimal(raw_value, direction):
    if not raw_value:
        return None

    # Latitude format: DDMM.MMMM
    # Longitude format: DDDMM.MMMM
    dot_index = raw_value.find('.')
    degree_digits = dot_index - 2

    degrees = float(raw_value[:degree_digits])
    minutes = float(raw_value[degree_digits:])
    decimal = degrees + minutes / 60

    if direction in ["S", "W"]:
        decimal *= -1

    return decimal


def parse_gpgga(sentence):
    parts = sentence.split(',')
    return {
        "type": "GPGGA",
        "utc_time": parts[1],
        "latitude": nmea_to_decimal(parts[2], parts[3]),
        "longitude": nmea_to_decimal(parts[4], parts[5]),
        "fix_quality": parts[6],
        "satellites": parts[7],
        "altitude_m": parts[9]
    }


def parse_gprmc(sentence):
    parts = sentence.split(',')
    speed_knots = float(parts[7]) if parts[7] else 0.0
    speed_kmh = speed_knots * 1.852
    return {
        "type": "GPRMC",
        "utc_time": parts[1],
        "status": parts[2],
        "latitude": nmea_to_decimal(parts[3], parts[4]),
        "longitude": nmea_to_decimal(parts[5], parts[6]),
        "speed_knots": speed_knots,
        "speed_kmh": round(speed_kmh, 2),
        "date": parts[9]
    }


sample_gpgga = "$GPGGA,123519,1046.4400,N,10639.3600,E,1,08,0.9,10.5,M,46.9,M,,*47"
sample_gprmc = "$GPRMC,123520,A,1046.4400,N,10639.3600,E,022.4,084.4,230626,003.1,W*6A"

print(parse_gpgga(sample_gpgga))
print(parse_gprmc(sample_gprmc))
