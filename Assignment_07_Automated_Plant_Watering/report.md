# Assignment 07 Report - Build a More Efficient Watering Cycle

## Objective

The objective of this assignment is to make the watering system more efficient. Instead of turning on the pump for a fixed amount of time every time, the system calculates how long the pump should run based on the current soil moisture value and the target soil moisture value.

## Data Collection

I started with dry soil and measured the soil moisture value. Then I added water for a fixed amount of time and waited until the sensor value became stable. I repeated this process multiple times.

| Total pump time | Soil moisture reading | Moisture decrease |
|---|---:|---:|
| Dry | 643 | 0 |
| 1s | 621 | 22 |
| 2s | 601 | 20 |
| 3s | 579 | 22 |
| 4s | 560 | 19 |
| 5s | 539 | 21 |
| 6s | 521 | 18 |

## Average Calculation

The moisture decrease values were:

```text
22, 20, 22, 19, 21, 18
```

The average decrease per second is:

```text
(22 + 20 + 22 + 19 + 21 + 18) / 6 = 20.33
```

So, the soil moisture reading decreases by about **20.33 units per second** when the pump is running.

## Improved Server Logic

If the current soil moisture value is higher than the target value, the system calculates the required pump time:

```text
pump_time = (current_moisture - target_moisture) / average_decrease_per_second
```

Example:

```text
current_moisture = 560
target_moisture = 450
difference = 110
pump_time = 110 / 20.33 = 5.41 seconds
```

Therefore, the pump should run for about **5.4 seconds**.

## Conclusion

This approach makes the watering system more controlled and efficient. The pump only runs for the required amount of time instead of always using the same fixed duration.
