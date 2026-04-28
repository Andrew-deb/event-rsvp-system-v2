# Event RSVP System

A FastAPI backend for creating events and managing RSVPs, built with SQLAlchemy ORM and PostgreSQL.

## Setup

### 1. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure the database

> ⚠️ **IMPORTANT NOTE:**  
> This project is currently configured to use a **PostgreSQL instance hosted on a cloud cluster**.  
> The connection string in the `.env` file points to this remote database and should work out of the box.  
>  
> However, if you would like to use a **local PostgreSQL** instance instead, simply update the  
> `DATABASE_URL` in the `.env` file with your local credentials using the format below:
>
> ```
> DATABASE_URL=postgresql://<username>:<password>@<host>:<port>/<database>
> ```
>
> **Example for a local setup:**
> ```
> DATABASE_URL=postgresql://postgres:password@localhost:5432/event_rsvp_db
> ```
>
> Make sure the local PostgreSQL database exists first:
> ```sql
> CREATE DATABASE event_rsvp_db;
> ```

### 4. Run the application

```bash
uvicorn app.app:app --reload
```

The API will be available at `http://localhost:8000`.  
Interactive docs at `http://localhost:8000/docs`.

## API Endpoints

| Method | Endpoint                    | Description              |
| ------ | --------------------------- | ------------------------ |
| POST   | `/events/`                  | Create a new event       |
| GET    | `/events/`                  | List all events          |
| POST   | `/events/{event_id}/rsvp`   | RSVP to an event         |
| GET    | `/events/{event_id}/rsvps`  | Get RSVPs for an event   |

## Project Structure

```
app/
├── api/v1/          # API route handlers
├── core/            # Database configuration
├── models/          # SQLAlchemy ORM models
├── repositories/    # Database query functions
├── schemas/         # Pydantic request/response schemas
├── services/        # Business logic layer
└── app.py           # FastAPI application entry point
```
