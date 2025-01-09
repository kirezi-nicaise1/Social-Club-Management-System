Social Club & Membership Management System
Project Description
This project is a web-based application built using Django that helps manage a social club's membership, events, and attendees. The system allows club administrators to:

Create and manage events.
Register new members.
Track member details (name, email, etc.).
Assign members to specific events.
The app includes authentication features, allowing for secure login/logout, and supports both superuser functionalities. The project also provides CRUD (Create, Read, Update, Delete) functionalities for members and events.

Features
Authentication: Secure login/logout.
Membership Management: Admin can add, update, delete, and view members.
Event Management: Admin can create,update, view, and delete events assign members to the events as attendees.
Attendee Management: Members can attend events, and admin can manage attendees.
Role-based Access: Admins have full access, while members can only view events and their own details.
Responsive UI: User-friendly design using Bootstrap to make it responsive and easy to navigate.
Technologies Used
Django (Python web framework)
Bootstrap (for responsive design)
HTML/CSS (for web page structure and styling)
PostgreSQL 

**Installation**
Prerequisites
Python 3.x or later
pip (Python package installer)
Steps to Run Locally
Clone the repository:
git clone https://github.com/kirezi-nicaise1/social-club-management.git

Navigate to the project directory:
cd social-club-management

Create a virtual environment:
python -m venv env

Activate the virtual environment:
On Windows:
env\Scripts\activate
On macOS/Linux:
source env/bin/activate

Install the required packages:
pip install -r requirements.txt

Apply database migrations:
python manage.py migrate

Create a superuser (admin user) to access the admin panel:
python manage.py createsuperuser
Follow the prompts to create the superuser account.

Run the development server:
python manage.py runserver
Open your browser and navigate to http://127.0.0.1:8000/ to use the app.

Usage
Admin Dashboard
Log in using the superuser account.
Manage members, events, and attendees from the admin dashboard.
