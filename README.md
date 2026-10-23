
# Still Life — Photography Gallery

A Django-based photography gallery showcasing still-life photography. Visitors can browse a collection of photographs and open individual images to view their descriptions and details.

**Live Demo:** https://still-life-photography-gallery.onrender.com  
**Repository:** https://github.com/daniel-oa/still-life-photography-gallery

## Features

- Photography gallery homepage
- Individual photo detail pages
- Photo descriptions and photographer credits
- Photo categories
- Django admin interface for managing photos and categories
- Responsive layout for different screen sizes

## Technologies Used

- Python
- Django
- SQLite
- HTML
- CSS
- Pillow
- Gunicorn
- WhiteNoise
- Render

## Running Locally

### 1. Clone the repository

```bash
git clone https://github.com/daniel-oa/still-life-photography-gallery.git
cd still-life-photography-gallery
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
```

On Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Prepare the database

```bash
python manage.py migrate
python manage.py loaddata gallery_data
```

The fixture loads the sample photo and category records into the database.

### 5. Start the development server

```bash
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

### 6. Access the admin interface (optional)

Create an administrator account:

```bash
python manage.py createsuperuser
```

Then visit http://127.0.0.1:8000/admin/.

## Project Structure

```text
still-life-photography-gallery/
├── config/
├── gallery/
│   ├── fixtures/
│   │   └── gallery_data.json
│   ├── static/
│   │   └── gallery/
│   │       └── photos/
│   ├── templates/
│   │   └── gallery/
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── Procfile
├── requirements.txt
└── README.md
```

## Image Credits

The gallery uses photographs sourced from Wikimedia Commons and credited to their respective creators:

- **A Quiet Read** — Praveenapraviii
- **A Study Break** — Punker1999
- **Objects on Display** — Daderot
- **Morning Coffee** — Noobshots
- **Fruit Bowl** — Gerda Arendt

The photographs were identified as public-domain/CC0 contributions. Please consult each original Wikimedia Commons file page for its specific licensing details.

## Deployment

The application is deployed on Render. Django migrations and static-file collection are performed during deployment, and the sample gallery data is loaded from the included fixture.

## AI Assistance

AI tools were used to assist with writing the HTML templates and CSS styling. The project was configured, tested, and deployed as a Django application.

## Purpose

This project was developed as a practical exercise in building and deploying a web application using Django.
