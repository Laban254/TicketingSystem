# Ticketing System: Powered by Django and Docker

Powered by Django with HTML and CSS, **Ticketwise** facilitates ticket creation and management for employees. Support members efficiently handle assigned tickets, update statuses, and resolve issues with detailed steps. Administrators oversee operations via an admin dashboard, where they can add employees and support members and manage their login details. Docker ensures seamless deployment and scalability, optimizing customer support processes.

## Table of Contents

-   [Introduction](https://www.phind.com/search?cache=qckgzmhpg0qrwoxsjy5zpalr#introduction)
-   [Prerequisites](https://www.phind.com/search?cache=qckgzmhpg0qrwoxsjy5zpalr#prerequisites)
-   [Environment Configuration](https://www.phind.com/search?cache=qckgzmhpg0qrwoxsjy5zpalr#environment-configuration)
-   [Installing Dependencies](https://www.phind.com/search?cache=qckgzmhpg0qrwoxsjy5zpalr#installing-dependencies)
-   [Building the Docker Image](https://www.phind.com/search?cache=qckgzmhpg0qrwoxsjy5zpalr#building-the-docker-image)
-   [Running the Application](https://www.phind.com/search?cache=qckgzmhpg0qrwoxsjy5zpalr#running-the-application)
-   [Using the Application](https://www.phind.com/search?cache=qckgzmhpg0qrwoxsjy5zpalr#using-the-application)
-   [Contributing](https://www.phind.com/search?cache=qckgzmhpg0qrwoxsjy5zpalr#contributing)
-   [License](https://www.phind.com/search?cache=qckgzmhpg0qrwoxsjy5zpalr#license)
-   [Contact](https://www.phind.com/search?cache=qckgzmhpg0qrwoxsjy5zpalr#contact)

## Introduction

Django, a powerful web framework for Python, combined with Docker's containerization platform, offers a robust solution for developing and deploying web applications. Docker encapsulates your Django application, along with its dependencies and runtime environment, within a container, ensuring consistency across different environments and simplifying deployment processes.

## Core Functionalities

### User Registration and Authentication

-   **User Creation**: Registers new users with roles (Customer or Engineer) and sends credentials via email.
-   **Login and Logout**: Manages user sessions, facilitating secure access.

### Ticket Management

-   **Ticket Creation**: Users can create support tickets, receive a unique ID, and get a confirmation email.
-   **Ticket Display**: Customers and Engineers view their active and resolved tickets.
-   **Ticket Assignment**: Tickets are assignable to Engineers, updating their status accordingly.
-   **Resolution**: Engineers can mark tickets as resolved, documenting resolution steps.

### Dashboard

-   Role-specific dashboards display ticket statistics, aiding in efficient oversight.

### Email Functionality

-   Automated emails for ticket creation and user account setup.

## Prerequisites

-   Docker: Ensure Docker is installed on your machine. You can download it from  [Docker Hub](https://www.docker.com/products/docker-desktop).

## Environment Configuration

Before running the application, you need to configure several environment variables. These variables are loaded from a  `.env`  file located at the root of your project. Here's a breakdown of some critical variables:

-   `DEBUG`: Controls whether debug mode is enabled. Set to  `0`  for production.
-   `DJANGO_SECRET_KEY`: A unique secret key for cryptographic signing.
-   `DJANGO_ALLOWED_HOSTS`: A comma-separated list of host/domain names that this site can serve.
-   `DJANGO_SU_NAME`,  `DJANGO_SU_EMAIL`,  `DJANGO_SU_PASSWORD`: Superuser credentials for the Django admin interface.
-   `EMAIL_HOST_USER`,  `EMAIL_HOST_PASSWORD`: Credentials for sending emails through SMTP (e.g., Gmail).

Example  `.env`  file content:

`DEBUG=0 DJANGO_SECRET_KEY=yoursecret key
DJANGO_ALLOWED_HOSTS=*
DJANGO_SU_NAME=admin username
DJANGO_SU_EMAIL=admin email
DJANGO_SU_PASSWORD=Admin_password
EMAIL_HOST_USER= host email
EMAIL_HOST_PASSWORD= email app password` 

## Installing Dependencies

1.  **Clone the Repository**: Clone the project repository to your local machine. 
 `git clone git@github.com:Laban254/TicketingSystem.git`
3.  **Navigate to the Project Directory**: Open a terminal and navigate to the project directory.

### Building the Docker Image

1.  **Build the Docker Image**: Run the following command to build the Docker image:

`docker build -t ticketing-system.` 

This command builds a Docker image named  `ticketing-system`  based on the Dockerfile in your project directory.

### Running the Application

1.  **Run the Docker Container**: After building your Docker image, run the container with the following command:

`docker run -d -p 8000:80 ticketing-system` 

This command runs the container in detached mode (`-d`) and maps port 8000 on your host to port 80 inside the container, allowing you to access the application at  `http://localhost:8000`.

### Using the Application

-   **Admin Dashboard**: Access the admin dashboard by visiting  `http://localhost:8000/admin`. Log in with the superuser credentials defined in the  `.env`  file.
-   **Ticket Management**: Navigate to  `http://localhost:8000/tickets`  to view and manage tickets.

## Contributing

Contributions to the Ticketing System are welcome. Please follow the standard fork-and-pull request workflow.

## License

Ticketwise is licensed under the MIT License. See the LICENSE file for details.

## Contact

For inquiries or feedback, please contact us at  [labanrotich6544@gmail.com](mailto:info@yourdomain.com).
