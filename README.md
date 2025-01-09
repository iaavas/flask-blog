
# Blog App with Flask

A simple and efficient  REST API built using Flask and SQLite.

## Getting Started

Follow these steps to set up and run the application on your local machine.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/iaavas/flask-blog.git
   cd flask-blog
   ```

2. Set up a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  
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

- `POST /api/register` - Register a new user
- `POST /api/login` - Login and retrieve an access token
- `POST /api/logout` - Logout the user

#### Blog Posts

- `POST /api/blogs` - Create a new blog post (requires authentication)
- `GET /api/blogs/?page=<number>` - Retrieve a paginated list of blog posts
- `GET /api/blogs/<id>` - Retrieve a single blog post by ID
- `PUT /api/blogs/<id>` - Update a blog post (requires authentication)
- `DELETE /api/blogs/<id>` - Delete a blog post (requires authentication)
