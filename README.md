# Event Scheduler Application

A Django-based event management system with CRUD functionality and search/filter capabilities.

## Features

- Add, edit, and delete events with title, date/time, location, and description
- Status tracking (upcoming, attending, maybe, declined)
- Search events by title, description, or location
- Filter by status and date range (today, week, month)
- Responsive design with Bootstrap 5
- Crispy forms for better form rendering

- For the AI part I made a small llm to generate the description using transformers

## Installation

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run migrations: `python manage.py migrate`
6. Create a superuser: `python manage.py createsuperuser` (optional)
7. Run the development server: `python manage.py runserver`
8. Open your browser to `http://localhost:8000`

## Usage

- View all events on the home page
- Use the search and filter options to find specific events
- Click "Add Event" to create a new event
- Click on an event to view details
- Edit or delete events from the detail view

## Admin Interface

Access the admin interface at `http://localhost:8000/admin/` to manage events with a more advanced interface.
