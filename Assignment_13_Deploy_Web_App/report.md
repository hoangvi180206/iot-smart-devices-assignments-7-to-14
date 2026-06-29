# Assignment 13 Report - Deploy Web App

## Objective

The objective of this assignment is to deploy a web application that visualizes location data on a map. The assignment also requires that the map subscription key should not be hard-coded directly into the source code.

## Implementation

I created a simple web application with:

- `index.html` for the page structure
- `app.js` for loading and displaying location data
- `config.example.js` to show how configuration should be provided without committing real keys

## API Key Handling

The real map API key should not be committed to GitHub. Instead, it should be stored in a cloud configuration variable, GitHub secret, or a local `config.js` file that is not committed.

Example local configuration:

```javascript
window.APP_CONFIG = {
  MAP_SUBSCRIPTION_KEY: "YOUR_KEY_HERE"
};
```

## Deployment

The web app can be deployed using Azure Static Web Apps or another static hosting service. After deployment, the final URL should be added here:

```text
Deployed web app URL: [Add deployed link here]
```

## Conclusion

This assignment shows how IoT location data can be visualized on a web map. It also shows the importance of separating configuration values from source code to avoid exposing private API keys.
