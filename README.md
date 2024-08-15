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
- [Folder Structure](#folder-structure)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

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
Create a virtual environment and activate it:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Apply migrations:

bash
Copy code
python manage.py migrate
Create a superuser (for accessing the admin panel):

bash
Copy code
python manage.py createsuperuser
Start the development server:

bash
Copy code
python manage.py runserver
Visit http://127.0.0.1:8000/ in your browser.

Docker Setup
To run the project in Docker:

Build the Docker image:

bash
Copy code
docker-compose build
Start the containers:

bash
Copy code
docker-compose up
Access the application at http://localhost:8000/.

Usage
Creating a Blog Post
Navigate to the "Create New Blog" button on the homepage.
Fill in the title and content of your blog.
Save the blog post, and it will appear on the homepage.
Viewing Blog Posts
On the homepage, all blogs are listed.
Click on any blog title to open its details in a modal.
You can also edit or delete your own blogs.
Folder Structure
csharp
Copy code
scribble/
├── scribble/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── blog/
│   ├── migrations/
│   ├── templates/
│   │   └── blog/
│   │       ├── blogView.html
│   │       └── base.html
│   ├── static/
│   │   └── blog/
│   │       ├── blogView.css
│   │       └── blogView.js
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
├── manage.py
└── README.md
API Endpoints
GET /blogs/ - List all blogs
POST /blogs/ - Create a new blog
GET /blogs/<id>/ - Get details of a specific blog
PUT /blogs/<id>/ - Update a specific blog
DELETE /blogs/<id>/ - Delete a specific blog
Contributing
Contributions are welcome! Please open an issue or submit a pull request for any changes or improvements.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
If you have any questions or feedback, feel free to reach out:

Email: your.email@example.com
GitHub: yourusername
