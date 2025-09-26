#  Blog Project

A modern, full-stack blog platform built with **Django** and **React**, showcasing advanced web development techniques.  
This project demonstrates my ability to manage complex projects with extensive AI assistance, integrating backend, frontend, and deployment workflows seamlessly.

<br>

##  Features
- **Dynamic Rendering**: Posts are fetched and displayed dynamically via React, powered by a Django REST Framework API.  
- **User Authentication**: Secure login, logout, and signup with Django's authentication system.  
- **Responsive Design**: Sleek, warm-themed UI with Bootstrap 5, custom CSS animations, and mobile-friendly layouts.  
- **Interactive Search**: Real-time client-side search filtering using React.  
- **Admin Dashboard**: Manage posts, tags, and comments through Django's admin panel.  
- **RESTful API**: Exposes post data for seamless frontend–backend integration.  
- **Tested Codebase**: Unit tests ensure robust functionality for models and views.  

<br>

##  Tech Stack
- **Backend**: Django 4.2.16, Django REST Framework  
- **Frontend**: React 18, Bootstrap 5, Font Awesome  
- **Database**: SQLite (local), compatible with PostgreSQL for production  
- **Tools**: WhiteNoise (static files), Gunicorn (WSGI), Git for version control  

<br>

##  Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/YasinShamsedini/django_portfolio.git
cd django_portfolio/Blog
````

### 2. Set Up Virtual Environment

```bash
python -m venv venv
# Activate
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Migrations

```bash
python manage.py migrate
```

### 5. Create Superuser

```bash
python manage.py createsuperuser
```

### 6. Collect Static Files

```bash
python manage.py collectstatic
```

### 7. Run the Server

```bash
python manage.py runserver
```

👉 Access the app at [http://127.0.0.1:8000](http://127.0.0.1:8000)
👉 Manage content via the admin panel at `/admin`.

<br>

##  Screenshots

*Add screenshots of homepage, post detail, and admin panel here.*

<br>

##  AI Usage

This project was developed with extensive **AI assistance** to streamline complex tasks, demonstrating my ability to manage and deliver sophisticated full-stack applications.
The source code leverages AI-driven workflows for optimization, while documentation (including this README) was partially crafted with AI support to ensure clarity and professionalism.

*See the root portfolio README for the overall AI usage policy across projects.*

<br>

## Links

* **GitHub**: [YasinShamsedini/django_portfolio](https://github.com/YasinShamsedini/django_portfolio)
* **Live Demo(Not available yet.)

##  License
MIT License exists in main directory

