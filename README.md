@@ -1,201 +1,32 @@
# Bus Boarding Sequence Generator
# Sarvm.ai FastAPI Backend

A Django web application that generates an optimal boarding sequence for bus bookings based on seat proximity to the front entry, minimizing aisle congestion and improving boarding efficiency.
This project is now powered by FastAPI and Uvicorn.

---

## 🚀 Features

- **CSV Upload:** Upload a CSV file of bookings (`Booking_ID,Seats`).
- **Smart Boarding Sequence:** Generates a boarding order based on seat proximity to the front.
- **Visual Results:** Displays the sequence in a clean, styled table.
- **CSV Download:** Download the generated sequence as a CSV.
- **No Database Required:** All processing is in-memory/session-based.
- **Bootstrap UI:** Clean, responsive interface (no JavaScript required).

---

## 🛠️ Tech Stack

- **Backend:** Django (latest LTS)
- **Frontend:** Django Templates, HTML, CSS (Bootstrap)
- **Language:** Python 3.x

---

## 📦 Project Structure

```
bus_boarding/           # Django project settings
boarding/               # Main app: views, forms, templates, static
  ├── templates/boarding/
  │     ├── upload.html
  │     └── result.html
  ├── static/boarding/
  │     └── style.css
  ├── forms.py
  ├── views.py
  └── urls.py
sample_data/
  ├── example.csv
  └── test_input.csv
README.md
manage.py
```

---

## ⚡ Quickstart

1. **Clone the repository**
2. **Install dependencies**:
   ```bash
   pip install django
   ```
3. **Run migrations** (no DB needed for basic use):
   ```bash
   python manage.py migrate
   ```
4. **Start the development server**:
   ```bash
   python manage.py runserver
   ```
5. **Open your browser** and go to [http://localhost:8000/](http://localhost:8000/)

---

## 📥 Usage

1. **Visit the homepage**
2. **Upload a CSV file** in the format:
   ```csv
   Booking_ID,Seats
   101,A1,B1
   120,A20,C2
   102,B2,B3
   103,A2
   ```
3. **View the generated boarding sequence** in a styled table.
4. **Download the result as a CSV** if desired.

---

## 🧪 Example Input/Output

**Input CSV:**
```
Booking_ID,Seats
101,A1,B1
120,A20,C2
102,B2,B3
103,A2
```

**Output Table:**
| Seq | Booking_ID |
|-----|------------|
| 1   | 103        |
| 2   | 101        |
| 3   | 120        |
| 4   | 102        |

**Output CSV:**
```
Seq,Booking_ID
1,103
2,101
3,120
4,102
```

---

## 🧠 Boarding Logic & Constraints

- Passengers board from the front (row A is closest).
- For bookings with multiple seats, the closest row is used.
- If two bookings are in the same row, the lower Booking_ID boards first.
- Bookings with empty seat lists are skipped (with a warning).

### Boarding Logic Illustration
## Running Locally

```sh
pip install -r requirements.txt
uvicorn main:app --reload
```
+-----------------------------+
|        Bus Layout          |
+-----------+-----------+----+
| A20 / B20 |           | C20 / D20 |
|-----------+-----------+-----------|
|                                   |
|                                   |
|           X                       |
|           Y        <- If X is standing, Y can't cross
|                                   |
|                                   |
|                                   |
|                                   |
| A1  / B1  |           | C1  / D1  |
|-----------+-----------+-----------|
|           Entry (Front)          |
+-----------------------------+
```

**Explanation:**
- The bus is entered from the front (bottom of the diagram).
- Rows are labeled A, B, C, D from left to right, and numbered from 1 (front) to 20 (back).
- Passengers with seats closer to the front (lower row letters, lower numbers) should board first.
- If a passenger (X) is standing in the aisle, another passenger (Y) behind cannot cross until X is seated.
- The boarding sequence is designed to minimize aisle congestion and allow smooth boarding from front to back.
- For bookings with multiple seats, the seat closest to the front determines the boarding order for that booking.
- If two bookings are in the same row, the one with the lower Booking_ID boards first.
- Bookings with empty seat lists are skipped (with a warning).

---

## 📁 Sample Data

- `sample_data/example.csv` — Simple example
- `sample_data/test_input.csv` — Includes multiple seats, same row, empty seat, and different Booking_IDs

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to fork the repo and submit a pull request.

---

## 📄 License
## Render Deployment

This project is open source and available under the [MIT License](LICENSE).

---

**Author:**
- [Your Name] 

## Render Deployment Notes

- Make sure `gunicorn` is in your requirements.txt (already added).
- Set your Render start command to:

```
gunicorn bus_boarding.wsgi:application --bind 0.0.0.0:$PORT
```

This ensures your Django app binds to the correct port and uses a production-ready WSGI server. 

## Static Files on Render

- Make sure you have the following in your `bus_boarding/settings.py`:
  ```python
  STATIC_URL = '/static/'
  STATIC_ROOT = BASE_DIR / 'staticfiles'
  ```
- In your Render dashboard, set your **Build Command** to:
- **Build Command:**
  ```sh
  pip install -r requirements.txt
  ```
  pip install -r requirements.txt && python manage.py collectstatic --noinput
- **Start Command:**
  ```sh
  uvicorn main:app --host 0.0.0.0 --port $PORT
  ```
- In your Render dashboard, add a **Static Site** or **Static Directory** for `/static` or `/staticfiles` if needed, so Render can serve your static files.
- In your templates, always use `{% load static %}` and reference static files with `{% static 'boarding/style.css' %}`.

This ensures your CSS/JS (including dark mode) will work in production. 
## Features
- File upload
- Result display
- Static file serving

## Project Structure
- `main.py` — FastAPI app
- `boarding/static/boarding/` — Static files
- `boarding/templates/boarding/` — Jinja2 templates
- `sample_data/` — Example CSV files 
