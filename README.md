<div id="top">


## Table of Contents
- [Overview](#overview)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Future Enhancements](#future-enhancements)

---
## Overview
This project is a simple web application built with Django that helps users manage their daily tasks. It allows users to add new tasks, mark them as completed, edit existing tasks, and delete tasks they no longer need.
Designed with scalability in mind, the application serves as a solid foundation for further enhancements and feature additions.​


## Project Structure

```sh
└── ToDo_app.git/
    ├── db.sqlite3
    ├── manage.py
    ├── templates
    │   ├── edit_task.html
    │   └── home.html
    ├── todo
    │   ├── __init__.py
    │   ├── __pycache__
    │   ├── admin.py
    │   ├── apps.py
    │   ├── migrations
    │   ├── models.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    └── todo_main
        ├── __init__.py
        ├── __pycache__
        ├── asgi.py
        ├── settings.py
        ├── urls.py
        ├── views.py
        └── wsgi.py
```

---

### Prerequisites

This project requires the following dependencies:

- **Programming Language:** Python

### Installation

Build ToDo_app.git from the source and intsall dependencies:

1. **Clone the repository:**

    ```sh
    ❯ git clone https://github.com/MattaKacz/ToDo_app.git
    ```

2. **Navigate to the project directory:**

    ```sh
    ❯ cd ToDo_app
    ```
3. **Create and activate virtual env:**

  	```sh
    ❯ python -m venv venv
	source venv/bin/activate  # Unix/macOS
	venv\Scripts\activate     # Windows
    ```

4. **Install the dependencies:**

  	```sh
    ❯ pip install -r requirements.txt
    ```
5. **Apply migrations:**

  	```sh
    ❯ python manage.py migrate
    ```
6. **Run the development server:**

  	```sh
    ❯ python manage.py runserver

    ```
7. **Open the application in your browser:**

  	```sh
    Go to http://127.0.0.1:8000/ to see the running application.

    ```

## Future Enhancements
The project is designed with scalability in mind. Potential future developments include:
- **User Authentication:** <br/>
Implementing a registration and login system to allow users to manage their own per
sonal task lists.
- **Task Categories:** <br/>
Adding the ability to group tasks into categories or projects.
- **Priorities and Deadlines:** <br/>
Allowing tasks to be assigned priority levels and deadlines for better organization.
- **Notifications:** <br/>
Integrating a notification system (e.g., email) to remind users about upcoming deadlines.
- **Responsive Design:** <br/>
Adapting the user interface for optimal experience on mobile devices.


<div align="right">

[![][back-to-top]](#top)

</div>




[back-to-top]: https://img.shields.io/badge/-BACK_TO_TOP-151515?style=flat-square


---
