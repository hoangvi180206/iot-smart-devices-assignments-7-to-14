# Assignment 07 - Watering calibration
# This script calculates the average moisture decrease per second
# and estimates how long the pump should run.

moisture_readings = [643, 621, 601, 579, 560, 539, 521]
target_moisture = 450
current_moisture = 560

# Calculate decrease between consecutive readings
moisture_decreases = []
for i in range(1, len(moisture_readings)):
    decrease = moisture_readings[i - 1] - moisture_readings[i]
    moisture_decreases.append(decrease)

average_decrease_per_second = sum(moisture_decreases) / len(moisture_decreases)

print("Moisture readings:", moisture_readings)
print("Moisture decreases per second:", moisture_decreases)
print(f"Average decrease per second: {average_decrease_per_second:.2f}")

if current_moisture > target_moisture:
    difference = current_moisture - target_moisture
    pump_time = difference / average_decrease_per_second
    print(f"Current moisture: {current_moisture}")
    print(f"Target moisture: {target_moisture}")
    print(f"Pump should run for {pump_time:.2f} seconds")
else:
    print("No watering needed")
