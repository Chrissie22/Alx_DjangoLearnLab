# 📘 Introduction to Django

Welcome to the **Introduction to Django** section of the `Alx_DjangoLearnLab` repository. This part of the project introduces the foundational concepts of Django, focusing on setting up the development environment, implementing basic models, performing database operations, and customizing the Django admin interface.

## 📁 Project Directory


---

## ✅ Tasks Overview

### Task 0: Django Development Environment Setup

- **Objective:** Set up a Django project named `LibraryProject`.
- **Steps:**
  - Installed Django using pip.
  - Created a new Django project using `django-admin startproject LibraryProject`.
  - Ran the development server and accessed the welcome page
  - Familiarized with project structure (`settings.py`, `urls.py`, `manage.py`).

📄 Refer to: `LibraryProject/README.md`

---

### Task 1: Implementing and Interacting with Django Models

- **Objective:** Create a Django app called `bookshelf` with a `Book` model and demonstrate CRUD operations using the Django shell.
- **Book Model Fields:**
  - `title` (CharField, max_length=200)
  - `author` (CharField, max_length=100)
  - `publication_year` (IntegerField)
- **Operations Performed:**
  - Create a Book instance (`1984`, George Orwell, 1949)
  - Retrieve the book
  - Update title to `Nineteen Eighty-Four`
  - Delete the book

📄 Documentation files:
- `create.md`, `retrieve.md`, `update.md`, `delete.md` (inside the LibraryProject folder)

---

### Task 2: Utilizing the Django Admin Interface

- **Objective:** Register and manage the `Book` model in the Django admin interface.
- **Admin Customizations:**
  - Displayed `title`, `author`, and `publication_year` in list view.
  - Enabled list filtering and search functionality.

📁 Code Location: `bookshelf/admin.py`

---

## 🚀 Technologies Used

- Python
- Django 
- SQLite (default database)
- Git & GitHub

---

## 🧠 Key Learnings

- Django project/app structure and configuration
- Model definition and migration
- Interacting with Django ORM via the shell
- Admin interface customization
- Effective use of Git for version control

---

## 🗂️ Repository Structure

- 📂 `Alx_DjangoLearnLab`
  - 📂 `Introduction_to_Django`
    - 📂 `LibraryProject`
      - 📂 `bookshelf` – app with models, admin config
      - 📄 `manage.py` – project entry point
      - 📄 `README.md` – task-specific instructions
    - 📄 `README.md` – **← this file**

---
