
# Still Life — Still Life Photography Gallery

Still Life is a photography gallery built with Django. It presents photographs in a simple, editorial-style layout, with individual pages for viewing each photograph and its details.

## Features

- Browse photographs in a responsive gallery.
- View individual photographs and their descriptions.
- Organise photographs by category.
- Display photographer information and source links.
- Add and manage photographs and categories through Django's admin panel.

## Built With

- Python
- Django
- HTML
- CSS
- SQLite
- Pillow

## Running Locally

1. Clone this repository:

   ```bash
   git clone <repository-url>
   cd still-life-photography-gallery
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   ```

   Windows:

   ```bash
   .venv\Scripts\activate
   ```

3. Install the dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Create the database tables:

   ```bash
   python manage.py migrate
   ```

5. Create an administrator account:

   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

7. Open `http://127.0.0.1:8000/` in your browser.

   To manage photographs and categories, visit `http://127.0.0.1:8000/admin/`.

## Photograph Content

The gallery uses photographs sourced from Wikimedia Commons. The photographs selected for this project were identified as being released under CC0 1.0. Individual source links and photographer information are recorded in the gallery where available.

Uploaded photographs are stored locally in the `media/` directory. The local SQLite database is not included in this repository, so a fresh setup requires adding gallery entries through the admin panel.

## Acknowledgements

AI tools were used to generate the HTML templates and CSS styling. The Django application setup, models, views, URL routing, database migrations, and admin configuration were developed as part of my learning process with AI assistance.
