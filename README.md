
# Remind-Me-Later Backend API

This Django project provides a backend API for the **Remind-Me-Later** web app, which allows users to schedule reminders via SMS or Email.

##  Features

- Create a new reminder (date, time, message, method)
- View all saved reminders
- Ready to integrate with any frontend via API calls
- CORS enabled for frontend-backend communication

---

##  Project Structure

```
remindmelater/
├── remindmelater/        # Project settings and URLs
│   ├── settings.py
│   ├── urls.py
├── reminders/            # App for handling reminders
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│   ├── admin.py
│   ├── tests.py
├── manage.py
└── README.md
```

---

##  Setup Instructions

1. **Clone the repo or extract the zip**

2. **Create and activate a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run migrations**
```bash
python manage.py migrate
```

5. **Start the server**
```bash
python manage.py runserver
```

6. (Optional) **Access Django Admin**
```bash
python manage.py createsuperuser
```

---

##  API Endpoints

| Method | URL                          | Description         |
|--------|------------------------------|---------------------|
| POST   | `/api/reminders/create/`     | Create new reminder |
| GET    | `/api/reminders/`            | List all reminders  |

###  Sample JSON for POST
```json
{
  "date": "2025-06-01",
  "time": "15:30:00",
  "message": "Take a break",
  "reminder_method": "email"
}
```

---

##  CORS

Cross-Origin Requests are enabled using `django-cors-headers`.  
You can connect this backend with a frontend hosted at a different domain or port (e.g. React at `localhost:3000`).

---

##  Notes

- `admin.py` and `tests.py` are unused for now, as this was a minimal API build.
- Message delivery (SMS/email) is not handled here — only scheduling logic.

---

##  Author

This project was built as part of an intial internship assignment screening.
