
# Blog App with Flask

A simple and efficient blog REST API built using Flask and SQLAlchemy.

## Features

- **User Authentication**: Registration, login, and logout with JWT-based authentication.
- **CRUD Operations for Blog Posts**: Create, read, update, and delete blog posts.
- **Pagination**: API support for paginated display of blog posts.
- **Database Integration**: Uses SQLite
- **RESTful Architecture**: Clean and scalable API design.

## Getting Started

Follow these steps to set up and run the application on your local machine.

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- A database system (SQLite, MySQL, or PostgreSQL)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/blog-rest-api.git
   cd blog-rest-api
   ```

2. Set up a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure the database in `config.py` (default is SQLite).

5. Set up the database:

   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

6. Run the application:

   ```bash
   flask run
   ```

### API Endpoints

#### Authentication

- `POST /auth/register` - Register a new user
- `POST /auth/login` - Login and retrieve an access token
- `POST /auth/logout` - Logout the user

#### Blog Posts

- `POST /blogs` - Create a new blog post (requires authentication)
- `GET /blogs` - Retrieve a paginated list of blog posts
- `GET /blogs/<id>` - Retrieve a single blog post by ID
- `PUT /blogs/<id>` - Update a blog post (requires authentication)
- `DELETE /blogs/<id>` - Delete a blog post (requires authentication)
