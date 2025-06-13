# Controller Backend (Django + DRF)

This is the backend controller for the multi-subnet computer management and backup system. It is built with Django and Django REST Framework (DRF), and is responsible for orchestrating monitoring, backups, and communication with agent services.

---

## Project Structure

```
backend/
├── controller_backend/    # Django project root
│   ├── settings.py        # Main settings (DRF, monitoring app registered)
│   ├── urls.py            # Project URL routing
│   └── ...
├── monitoring/           # Monitoring app (system status, API)
│   ├── serializers.py    # DRF serializers
│   ├── api_views.py      # DRF API views
│   ├── urls.py           # App URL routing
│   └── ...
├── .env                  # Environment variables (e.g., DATABASE_URL)
├── requirements.txt      # Python dependencies
└── ...
```

---

## Setup & Usage

1. **Activate the virtual environment**
   ```powershell
   .\backend_venv\Scripts\Activate.ps1
   ```

2. **Install dependencies**
   ```powershell
   pip install -r requirements.txt
   ```

3. **Configure Environment**
   - Edit `.env` to set your database and other secrets.
   - Example:
     ```
     DATABASE_URL="postgresql://user:password@host/db?sslmode=require"
     ```

4. **Apply Migrations**
   ```powershell
   python manage.py migrate
   ```

5. **Run the Development Server**
   ```powershell
   python manage.py runserver
   ```
   - Visit: http://localhost:8000/monitoring/ping/

---

## Monitoring API

- **GET /monitoring/ping/**
  - Returns: `{ "status": "ok" }`
  - Purpose: Health check for backend controller.

---

## Adding More Features
- Create new Django apps for other domains (e.g., `backups`).
- Use DRF for all API endpoints (serializers, API views, routers).
- Keep code modular: separate business logic, serializers, and views.

---

## Database
- Uses environment variable `DATABASE_URL` for configuration (see `.env`).
- Supports PostgreSQL (recommended for production).

---

## Next Steps
- Expand the monitoring app for more system status endpoints.
- Add authentication and security for agent communication.
- Integrate with agent services for distributed monitoring and backup.
