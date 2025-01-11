# Open Source Project

Welcome to the project! This repository contains both the frontend and backend components of the application. Below, you'll find a quick guide to help you get started.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
  - [Backend Setup](#backend-setup)
  - [Frontend Setup](#frontend-setup)
- [Project Structure](#project-structure)

---

## Project Overview

This project is a full-stack application with the following features:

- **Backend**: A REST API built with Python and FastAPI for user authentication and data management.
- **Frontend**: A modern user interface built with React and TypeScript.

---

## Technologies Used

- **Backend**: FastAPI, SQLAlchemy, Alembic
- **Frontend**: React, TypeScript, TailwindCSS, Vite
- **Database**: PostgreSQL

---

## Getting Started

### Prerequisites

- [Python 3.12](https://www.python.org/)
- [Node.js](https://nodejs.org/) and [npm](https://www.npmjs.com/)
- PostgreSQL database

### Backend Setup

1. **Clone the repository**:

   ```bash
   git clone https://github.com/neevan0842/VeloPass-MiniProject.git
   cd VeloPass-MiniProject/backend
   ```

2. **Create a virtual environment and activate it**

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables: Create a .env file in the backend directory**

5. **Run database migrations:**

   ```bash
   alembic upgrade head
   ```

6. **Start the backend server:**

   ```bash
   fastapi dev
   ```

7. **Access API Documentation:**

After starting the server, access API documentation at http://localhost:8000/docs.

### Frontend Setup

1. **Navigate to the frontend directory:**

   ```bash
   cd ../frontend
   ```

2. **Install dependencies:**

   ```bash
   npm install
   ```

3. **Start the development server:**

   ```bash
   npm run dev
   ```

Open your browser and navigate to http://localhost:5173.

## Project Structure

```bash
.
├── backend           # Backend code (FastAPI)
│   ├── app           # Main application code
│   └── alembic       # Database migrations
├── frontend          # Frontend code (React + Vite)
│   └── src           # Source code for UI components
└── model             # Placeholder for future ML models or data files
```
