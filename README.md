# Blogging Platform API

A production-ready, fully containerized RESTful API for a blogging
platform. Built with **Django**, **Django REST Framework (DRF)**, and
**Docker**, this project features robust JWT authentication, role-based
access control (RBAC), and interactive API documentation via Swagger UI.

## Key Features

-   **Custom User Model:** Extended Django's default user model to
    include custom fields (`name`, `phone_number`, and `role`).
-   **Role-Based Access Control (RBAC):**
    -   **Writers** can create, read, update, and delete their own blog
        posts.
    -   **Viewers** have read-only access to all published posts.
    -   Unauthenticated users can view posts but cannot modify them.
-   **JWT Authentication:** Secure login and registration system using
    JSON Web Tokens (`djangorestframework-simplejwt`).
-   **Custom Permissions:** Security logic is abstracted into
    `permissions.py` for clean, modular views.
-   **Modular Routing:** Utilizes DRF's `ModelViewSets` and
    `DefaultRouter` for standard, predictable endpoint structures.
-   **Dockerized:** Completely containerized for consistent development
    and deployment environments.
-   **Swagger UI:** Fully documented endpoints with built-in
    authorization testing.

------------------------------------------------------------------------

## Tech Stack

-   **Core:** Python 3.12, Django, Django REST Framework
-   **Authentication:** SimpleJWT
-   **Database:** SQLite (default for quick start)
-   **Documentation:** `drf-spectacular` (Swagger UI)
-   **Deployment/Environment:** Docker, Docker Compose, Gunicorn

------------------------------------------------------------------------

## Quick Start (Docker)

The application is fully containerized. You do not need to install
Python, virtual environments, or any dependencies manually.

### Prerequisites

-   **Docker Desktop** must be installed and running on your machine.

### 1. Clone the Repository

``` bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

### 2. Build and Start the Containers

Run the following command to build the image, apply migrations, and
start the server in the background:

``` bash
docker-compose up --build -d
```

### 3. Create an Admin User (Superuser)

Because the database starts fresh, you need to create a superuser to
access the Django Admin panel:

``` bash
docker-compose exec web python manage.py createsuperuser
```

Follow the terminal prompts to set a username and password.

### 4. Access the Application

-   **Interactive API Docs (Swagger UI):**
    <http://localhost:8000/api/docs/>
-   **Django Admin Panel:** <http://localhost:8000/admin/>

### 5. Stop the Server

``` bash
docker-compose down
```

------------------------------------------------------------------------

## API Endpoints Overview

Here is a quick summary of the core endpoints. For complete payload
details, testing, and response schemas, please use the Swagger UI.

### Authentication & Users

  ---------------------------------------------------------------------------------
  Method            Endpoint                    Description       Access
  ----------------- --------------------------- ----------------- -----------------
  `POST`            `/api/accounts/register/`   Register a new    Public
                                                user              

  `POST`            `/api/login/`               Login to get JWT  Public
                                                access and        
                                                refresh tokens    

  `POST`            `/api/login/refresh/`       Refresh an        Public
                                                expired access    
                                                token             
  ---------------------------------------------------------------------------------

### Blog Posts

  ------------------------------------------------------------------------------------
  Method            Endpoint                       Description       Access
  ----------------- ------------------------------ ----------------- -----------------
  `GET`             `/api/blogs/posts/`            List all blog     Public
                                                   posts             

  `POST`            `/api/blogs/posts/`            Create a new blog Writer Only
                                                   post              

  `GET`             `/api/blogs/posts/{id}/`       Retrieve a        Public
                                                   specific post     

  `PUT`             `/api/blogs/posts/{id}/`       Update a post     Author Only

  `DELETE`          `/api/blogs/posts/{id}/`       Delete a post     Author Only

  `GET`             `/api/blogs/posts/my_posts/`   List all posts by Writer Only
                                                   the logged-in     
                                                   user              
  ------------------------------------------------------------------------------------

------------------------------------------------------------------------

## How to Test APIs (via Swagger)

Testing the API directly from the browser is straightforward:

1.  Go to <http://localhost:8000/api/docs/>.
2.  **Register a user** using the `/api/accounts/register/` endpoint.
    Set the role to `writer`.
3.  **Login** using `/api/login/`. Copy the `access` token from the JSON
    response.
4.  Scroll to the top of the Swagger page and click the **Authorize**
    button.
5.  Enter your token in the format `Bearer <your_access_token>`. Include
    the word `Bearer` followed by a space.
6.  Click **Authorize**. You can now execute protected routes, such as
    creating or deleting posts.
