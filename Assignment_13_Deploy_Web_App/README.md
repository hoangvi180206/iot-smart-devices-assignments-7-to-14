# Assignment 13 - Deploy Web App

## Goal

Deploy a web app that visualizes location data on a map and keeps API keys out of the source code.

## Files

- `web/index.html`
- `web/app.js`
- `web/config.example.js`
- `report.md`
- `screenshots/`

## How to test locally

Copy `config.example.js` to `config.js`, then add your own map key locally.

```bash
cd web
cp config.example.js config.js
python -m http.server 8000
```

Open:

```text
http://localhost:8000
```

## Important

Do not commit a real map subscription key. Keep the real key in Azure Static Web Apps configuration, GitHub secrets, or a local untracked `config.js` file.
