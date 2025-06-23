🎬 Cinema Reservation System (CLI App)
Course: Introduction to Programming
Language: Python
Semester: 1st
Academic Year: 2023/2024
Project Type: Console-based application

📌 Project Overview
A terminal-based cinema reservation system that allows users to explore movies, reserve seats, and manage ticket data. The application supports multiple user roles with different permissions and functionalities, using a role-based console menu.

👥 User Roles
Unregistered Customer

Can view movie and projection info via search

Cannot reserve tickets directly; must register or call/visit in person

Registered Customer

Can search and reserve tickets for available projection times

Can cancel reservations and view personal bookings

Must arrive at least 30 minutes before the show to complete purchase in person

Seller

Can reserve and sell tickets to registered or unregistered customers

Can cancel and manage reservations

Manager

Registers new sellers and managers

Has access to internal reports and system overview

🔍 Core Features
User registration, login, logout, profile editing

Search movies and projection schedules

Seat availability viewer with selection

Reservation creation and cancellation

Role-based console interface (menu per role)

File-based data persistence using Python’s pickle

🧠 Technical Highlights
Language: Python

Serialization: Used pickle for storing user and system data as objects

File Handling: Input/output through .txt and .pkl files

Menu System: Clean CLI interface for each user role

Validation: Input validation and role-based access control
