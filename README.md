# Scribble

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Setup](#setup)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Docker Setup](#docker-setup)
- [Usage](#usage)
  - [Creating a Blog Post](#creating-a-blog-post)
  - [Viewing Blog Posts](#viewing-blog-posts)


## Project Overview

**Scribble** is a blogging platform where users can create, view, and manage their blog posts. The application allows users to format their content, organize posts, and interact with a sleek and user-friendly interface.

## Features

- **User Authentication**: Sign up, log in, and manage user sessions.
- **Create Blog Posts**: Users can create and publish their own blog posts.
- **View Blogs**: List all blogs, view individual blog posts, and see detailed content in a modal.
- **Manage Blogs**: Edit or delete blog posts.
- **Responsive Design**: Optimized for both desktop and mobile viewing.

## Tech Stack

- **Backend**: Django, Django REST Framework
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite (default), MySQL (optional)
- **Authentication**: Django's built-in authentication
- **Deployment**: Docker, Gunicorn, Nginx

## Setup

### Prerequisites

- Python 3.x
- Django 3.x or later
- Docker (optional for deployment)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/scribble.git
   cd scribble


2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations:**

    ```bash
    python manage.py migrate
    ```

5. **Create a superuser (for accessing the admin panel):**

    ```bash
    python manage.py createsuperuser
    ```

6. **Start the development server:**

    ```bash
    add the api key in the BLOG_APP/views.py
    python manage.py runserver
    ```

7. **Visit the application in your browser:**

    [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

### Docker Setup

1. **Build the Docker image:**

    ```bash
    docker-compose build
    ```

2. **Start the containers:**

    ```bash
    docker-compose up
    ```

3. **Access the application:**

    [http://localhost:8000/](http://localhost:8000/)

## Usage

### Creating a Blog Post

- Navigate to the "Create New Blog" button on the homepage.
- Fill in the title and content of your blog.
- Save the blog post, and it will appear on the homepage.

### Viewing Blog Posts

- On the homepage, all blogs are listed.
- Click on any blog title to open its details in a modal.
- You can also edit or delete your own blogs.



