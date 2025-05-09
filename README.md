# Web Scraper Analytics App

A modular, full-stack web application that allows users to input a URL and scrape detailed element data (tags, classes, innerText, attributes) from the target web page. It also logs user metrics (IP, country, duration, browser info, etc.) for analytics—even for anonymous users.

## 🛇 Architecture

### Frontend (FE)
- Vue.js + Vuetify for a clean, Google-style minimalist UI
- Navigation menu with historic search results
- Anonymous users receive UUID stored in browser cache (purgeable)
- Persistent local data for user history

### Backend (BE)
- Python FastAPI
- OOP, modular and layered structure (API, business, data layers)
- Redis for Pub/Sub & task queue
- Asynchronous processing with Celery (or FastAPI background tasks)
- Alembic for DB migrations

### Database
- PostgreSQL (initially relational)
- Future option: MongoDB for non-relational data archiving

### ORM & Validation
- SQLAlchemy (ORM)
- Pydantic (data validation and schema generation)

## 🔍 Features

- Input field to scrape any URL (e.g., `https://www.example.com`)
- Extract all elements: tags, classes, innerText, and properties
- Display results in a data table
- Record search metadata in DB:
  - Request IP and country
  - Target URL
  - Response time (in seconds)
  - Time spent on page
  - Client/browser metadata
  - UUID for anonymous session

## 📊 Analytics

- Dashboard for historical data (left nav menu)
- Filtering and export features
- Performance metrics (backend processing time, queue time)

## 🧠 Future Enhancements

- Anonymous session tracking with Redis or JWT
- Admin dashboard for usage statistics
- Optionally archive old data to MongoDB

## 📁 Project Structure (Modular)

```text
backend/
├── app/
│   ├── api/
│   ├── business/
│   ├── data/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   ├── workers/
│   └── main.py
├── alembic/
frontend/
├── app/
│   ├── components/
│   ├── views/
│   ├── router/
│   └── App.vue
```

## 🧪 Tech Stack

| Layer      | Technology       |
| ---------- | ---------------- |
| Frontend   | Vue.js + Vuetify |
| Backend    | Python FastAPI   |
| Validation | Pydantic         |
| ORM        | SQLAlchemy       |
| Messaging  | Redis Pub/Sub    |
| Queue      | Redis / Celery   |
| DB         | PostgreSQL       |
| Migrations | Alembic          |

## 🚀 Getting Started

### Prerequisites
- Docker
- Python 3.11+
- Node.js + PNPM

### Setup

```bash
# Frontend
cd frontend
pnpm install
pnpm dev

# Backend
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Docker Compose (Production/Staging)

Use `.env` for environment control.

```bash
docker-compose -f docker-compose.staging.yml up --build
```

---

Let me know if you'd like the full codebase scaffold for this. Want me to generate that next?
