# AI Lead Management System

## Project Overview

AI Lead Management System is a full-stack web application developed using Flask and SQLite that helps businesses efficiently manage customer leads through a centralized dashboard.

The system allows users to submit lead information through a clean and responsive form interface. Submitted leads are stored in a database and can be viewed, searched, filtered, updated, and managed through an admin dashboard.

The project also includes automated AI-powered email response functionality using Groq LLM integration.

---

# Features

- Lead Submission Form
- SQLite Database Integration
- Admin Dashboard
- Search Leads by Name
- Filter Leads by Status
- Update Lead Status
- Delete Leads
- AI-Powered Automated Emails
- Responsive UI Design
- Professional Dashboard Interface

---

# Tech Stack

## Frontend
- HTML5
- CSS3

## Backend
- Python
- Flask

## Database
- SQLite

## Libraries Used
- Flask
- Flask-SQLAlchemy
- Flask-Mail
- python-dotenv
- groq

---

# AI Integration

The project integrates Groq LLM API with the Llama 3.1 model to automatically generate professional customer response emails.

## AI Features
- AI-generated professional email replies
- Dynamic email generation
- Business-context-aware responses
- Automatic email delivery
- Graceful fallback handling

---

# Project Workflow

```plaintext
User submits lead form
        ↓
Flask backend receives form data
        ↓
Lead stored in SQLite database
        ↓
Groq Llama 3.1 AI generates customer response email
        ↓
Automated email sent to customer
        ↓
Admin manages leads through dashboard
```

---

# Project Structure

```plaintext
LEAD_SYSTEM/
│
├── static/
│   └── style.css
│
├── templates/
│   ├── index.html
│   └── dashboard.html
│
├── Screenshots/
│
├── instance/
│
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
└── .env
```

---

# Database Schema

## Lead Table

| Column | Type | Description |
|---|---|---|
| id | Integer | Primary Key |
| name | String | Customer Name |
| email | String | Customer Email |
| phone | String | Phone Number |
| business | String | Business Type |
| message | Text | Customer Message |
| status | String | Lead Status |

---

# Installation Steps

## 1. Clone Repository

```bash
git clone YOUR_GITHUB_REPO_LINK
```

---

## 2. Open Project Folder

```bash
cd LEAD_SYSTEM
```

---

## 3. Create Virtual Environment

```bash
python -m venv venv
```

---

## 4. Activate Virtual Environment

### Windows

```bash
.\venv\Scripts\activate
```

---

## 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 6. Configure Environment Variables

Create `.env` file:

```env
EMAIL_USER=your_email
EMAIL_PASS=your_app_password
GROQ_API_KEY=your_groq_api_key
```

---

## 7. Run Application

```bash
python app.py
```

---

# Screenshots

- Homepage
- Lead Submission Form
- Dashboard
- Search by Name
- Search by Status
- AI Email Automation

---

# Future Improvements

- User Authentication System
- Cloud Deployment
- Analytics Dashboard
- Role-Based Access
- CSV Export
- Advanced AI Lead Insights

---

# Learning Outcomes

This project helped in understanding:

- Full-stack web development
- Flask backend architecture
- CRUD operations
- Database integration
- AI API integration
- Email automation
- Dashboard management
- Git & GitHub workflow
- Error handling

---

# Author

Praneeth Puli
