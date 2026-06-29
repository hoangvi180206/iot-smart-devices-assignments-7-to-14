# Assignment 12 Report - Store Location Data with Function Bindings

## Objective

The objective of this assignment is to use Azure Function output binding to save location telemetry into Blob Storage.

## What Is an Output Binding?

An output binding allows an Azure Function to write data to another Azure service without manually writing all the service connection code. In this assignment, the function receives location telemetry and writes it as a JSON blob.

## Implementation

The function receives telemetry from an Event Hub trigger. The output binding writes the data to Blob Storage.

The output path is:

```text
locations/{sys.utcnow}.json
```

Each GPS message is saved as a separate JSON file.

## Example Data

```json
{
  "latitude": 10.762622,
  "longitude": 106.660172,
  "speed_kmh": 41.48,
  "altitude_m": 10.5
}
```

## Conclusion

Using output bindings makes the code cleaner because the Azure Function does not need to manually create a Blob Storage client. The binding handles writing the output data to storage.
