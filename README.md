# 📄 CV Generator API

A web application built with **Django** and **Django REST Framework** that allows users to create, view, and generate professional CVs in **PDF** format.  
The application provides a simple REST API to handle user profile data, render it into an HTML template, and convert it into a downloadable PDF.

---

## 🛠 Technologies Used
- **Django** – Web framework for backend logic
- **Django REST Framework (DRF)** – RESTful API creation
- **xhtml2pdf** – Convert HTML + CSS into PDF documents
- **Python** – Core programming language

---

## ✨ Features
- **Create Profile** – Add personal details, education, work experience, and skills
- **List Profiles** – Retrieve all existing profiles from the database
- **Generate PDF** – Download a CV in PDF format for any profile

---

## ⚙️ Project Setup

### 1️⃣ Clone the repository
```bash
git clone <your-repository-url>
cd CV-Generator
````

### 2️⃣ Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate      # On macOS/Linux
venv\Scripts\activate         # On Windows
```

### 3️⃣ Install dependencies

```bash
pip install Django djangorestframework xhtml2pdf
```

### 4️⃣ Apply database migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Run the development server

```bash
python manage.py runserver
```

Your API will be available at: **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**

---

## 📌 API Endpoints

| Method | Endpoint                  | Description                                                         |
| ------ | ------------------------- | ------------------------------------------------------------------- |
| GET    | `/profiles/`              | Returns a list of all profiles in JSON format                       |
| POST   | `/profiles/`              | Creates a new profile from JSON input                               |
| GET    | `/profiles/<int:pk>/pdf/` | Generates and downloads a PDF for the profile with the given **ID** |

---

## 🖥 How It Works

1. The **`generate_pdf_view`** function in `views.py` fetches the profile from the database.
2. The profile data is rendered into an HTML template (`cv_template.html`).
3. **xhtml2pdf** converts the HTML + CSS into a PDF.
4. The server returns the PDF as an **HttpResponse** with headers to prompt a file download.

---

## 📂 Project Structure

```
CV-Generator/
├── manage.py
├── db.sqlite3
├── mysite/              # Project settings
├── profiles/            # App with models, views, serializers
├── templates/           # HTML templates for CVs
└── requirements.txt
```

---

## 📜 License

This project is licensed under the **MIT License** – feel free to modify and use.
