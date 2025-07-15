# Commission Management Application

This is a containerizable commission management application for field sales reps, covering multiple product lines and individual products.

## Features

*   **Commission Calculation**: Automatically calculates commissions in real time based on product-, rep-, and period-specific rules. This includes flat rates, tiered (accelerator) percentages, base salary + commission, and margin-based incentives.
*   **Flexible Commission Plans**: Define unique rates, tiers, and special campaign overrides per product line, product, and salesperson.
*   **Data Import**: Accept sales data uploads via CSV/Excel, and also support import from external systems, ensuring centralized, up-to-date figures.
*   **Sales Rep Dashboard**: Provide each rep with a dynamic dashboard showing current sales, achieved thresholds, active tiers, and projected payout to date.
*   **Reporting**: Offer robust reporting with detailed breakdowns by rep, product, and time period—exportable as PDF or CSV for payroll and accounting.
*   **Approval Workflow**: After auto-calculation, commissions enter a verification queue, where managers can approve or reject. All actions must be audit-logged for transparent, traceable records.
*   **Notifications**: Trigger automatic notifications (email or in-app) when reps hit tier thresholds, when commissions are approved, or when exceptional conditions occur.
*   **"What-If" Simulation**: Reps or managers can model different sales scenarios or goal adjustments and immediately see projected commission outcomes.
*   **Admin Console**: Authorized users can manage reps, product lines, products, commission structures, regions, and user permissions—without touching code.
*   **Secure and Compliant**: Ensure secure, compliant data handling (e.g., GDPR), with role-based access, encrypted storage, and detailed audit trails.
*   **Modular and Scalable**: Designed for modular growth—easily adding new reps, products, regions, or more complex commission schemes in the future.
*   **Container-Friendly**: The architecture is fully container-friendly (Docker-ready), with clear separation of services, database, and background jobs.

## Getting Started

### Prerequisites

*   [Docker](https://docs.docker.com/get-docker/)
*   [Docker Compose](https://docs.docker.com/compose/install/)

### Setup

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/commission-management-app.git
    cd commission-management-app
    ```

2.  **Environment Variables:**

    Create a `.env` file in the root directory of the project and add the following environment variables:

    ```
    DATABASE_URL=postgresql://user:password@db:5432/commission_db
    SECRET_KEY=thisissecret
    MAIL_SERVER=smtp.mailtrap.io
    MAIL_PORT=2525
    MAIL_USERNAME=user
    MAIL_PASSWORD=password
    MAIL_USE_TLS=True
    MAIL_USE_SSL=False
    ```

3.  **Build and run the application:**

    ```bash
    docker-compose up --build
    ```

    The application will be available at `http://localhost:5000`.

## Usage

*   **Register a new user:**

    Send a `POST` request to `/register` with the following JSON payload:

    ```json
    {
        "username": "testuser",
        "password": "testpassword",
        "email": "test@test.com",
        "role": "commission_manager"
    }
    ```

*   **Login:**

    Send a `POST` request to `/login` with the following `Authorization` header:

    ```
    Authorization: Basic <base64-encoded-username-and-password>
    ```

*   **Create a new sale:**

    Send a `POST` request to `/sales` with the following JSON payload and an `x-access-token` header containing the JWT:

    ```json
    {
        "user_id": 1,
        "product_id": 1,
        "quantity": 10,
        "sale_date": "2023-10-27T10:00:00"
    }
    ```

*   **Get sales for a user:**

    Send a `GET` request to `/sales` with an `x-access-token` header containing the JWT.

*   **Upload a CSV file:**

    Send a `POST` request to `/upload/csv` with a `multipart/form-data` payload containing the CSV file and an `x-access-token` header containing the JWT.

*   **Upload an Excel file:**

    Send a `POST` request to `/upload/excel` with a `multipart/form-data` payload containing the Excel file and an `x-access-token` header containing the JWT.

*   **Generate a CSV report:**

    Send a `GET` request to `/report/csv` with an `x-access-token` header containing the JWT.

*   **Generate a PDF report:**

    Send a `GET` request to `/report/pdf` with an `x-access-token` header containing the JWT.

*   **Simulate commission:**

    Send a `POST` request to `/simulate` with the following JSON payload:

    ```json
    {
        "sales": [
            {
                "product_id": 1,
                "quantity": 10
            },
            {
                "product_id": 2,
                "quantity": 20
            }
        ]
    }
    ```