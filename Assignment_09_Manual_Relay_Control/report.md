# Assignment 09 Report - Add Manual Relay Control

## Objective

The objective of this assignment is to add a manual override to the relay control system using HTTP triggers in Azure Functions. This allows the relay to be turned on or off from a web request.

## Implementation

I created two HTTP triggers:

| Trigger | Purpose |
|---|---|
| `relay_on` | Sends a command to turn the relay on |
| `relay_off` | Sends a command to turn the relay off |

The `function.json` files use `authLevel: anonymous`, so the functions can be called directly from the browser during testing.

## Test URLs

```text
http://localhost:7071/api/relay_on
http://localhost:7071/api/relay_off
```

## Result

When the `relay_on` URL is opened, the function returns a message saying that the relay ON command was sent. When the `relay_off` URL is opened, the function returns a message saying that the relay OFF command was sent.

## Conclusion

This assignment adds a manual control path to the IoT system. In addition to automatic relay control based on sensor data, the user can manually control the relay through HTTP requests.
