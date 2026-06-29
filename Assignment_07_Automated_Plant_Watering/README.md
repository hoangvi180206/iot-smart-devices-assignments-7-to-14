# Assignment 07 - Automated Plant Watering

## Goal

Build a more efficient watering cycle by calculating how long the pump should run based on soil moisture readings.

## What I did

I measured or simulated soil moisture readings after adding a fixed amount of water each second. Then I calculated the average decrease in the soil moisture reading per second. This value is used by the server code to calculate the required pump time instead of running the pump for a fixed duration.

## Files

- `report.md` - explanation and calculation
- `code/watering_calibration.py` - calibration and pump-time calculation
- `screenshots/` - output screenshots

## How to run

```bash
python code/watering_calibration.py
```
