# Project Execution Guide: Blogging Platform API

This guide provides complete instructions for setting up, running, and
testing the Blogging Platform API. The project is fully containerized
using Docker, requiring no manual Python or dependency installations.

## Prerequisites

-   **Docker Desktop** must be installed and actively running on the
    host machine.

## Step-by-Step Instructions to Run

### Step 1: Open Terminal

Extract the project archive and open a terminal (Command Prompt,
PowerShell, or Mac/Linux Terminal). Navigate to the project root
directory (the folder containing `docker-compose.yml` and `manage.py`).

### Step 2: Build and Start the Project

Run the following command to build the Docker image, install all
required libraries, apply database migrations, and start the server:

``` bash
docker-compose up --build -d
```

**Note:** The `-d` flag runs the containers in detached mode/background,
allowing you to use the same terminal for subsequent commands.

### Step 3: Create an Admin User (Superuser)

Because the database is initialized fresh, a superuser must be created
to access the Django Admin panel. Run:

``` bash
docker-compose exec web python manage.py createsuperuser
```

Follow the terminal prompts to enter a username, email (optional), and
password.

### Step 4: Access the Application

Once the server is running, the following endpoints are available:

-   **Swagger API Documentation (Test APIs here):**
    <http://localhost:8000/api/docs/>
-   **Django Admin Panel:** <http://localhost:8000/admin/>

### Step 5: Stop the Server (When Finished)

To stop and remove the running containers, use:

``` bash
docker-compose down
```

## How to Test the APIs (Using Swagger UI)

The primary method for testing is via the interactive Swagger UI at
<http://localhost:8000/api/docs/>.

### 1. Register a User (Writer or Viewer)

-   Expand the `POST /api/accounts/register/` endpoint.
-   Click **Try it out**.
-   Provide the JSON payload (`username`, `password`, `name`,
    `phone_number`, and `role`: `"writer"` or `"viewer"`).
-   Click **Execute**. A `201 Created` response indicates success.

### 2. Login to Retrieve a Token

-   Expand the `POST /api/login/` endpoint.
-   Click **Try it out**.
-   Enter the registered `username` and `password`.
-   Click **Execute**. Copy the `access` token from the JSON response.

### 3. Authorize Swagger to Test Protected Routes

-   Scroll to the top of the Swagger page and click the **Authorize**
    button.
-   In the input box, type `Bearer <your_access_token>` (ensure the word
    `Bearer` is followed by a single space before the token).
-   Click **Authorize** and close the popup. The Swagger UI is now
    authenticated.

### 4. Test Blog Posts

-   **Create a Post:** Use `POST /api/blogs/posts/` (requires a Writer
    token).
-   **View All Posts:** Use `GET /api/blogs/posts/` (public access).
-   **View My Posts:** Use `GET /api/blogs/posts/my_posts/` (requires a
    Writer token).
-   **Edit/Delete:** Use `PUT` or `DELETE` on `/api/blogs/posts/{id}/`
    (restricted to the author who created the post).

## Role-Based Access Control (RBAC) Rules Implemented

-   **Unauthenticated Users:** Read-only access to view posts (`GET`).
-   **Viewer Role:** Read-only access to view posts (`GET`).
-   **Writer Role:** Read access, plus the ability to create new posts.
    Writers can only edit or delete posts they authored.
-   **Superuser / Admin:** Full administrative access via the Django
    Admin panel.
