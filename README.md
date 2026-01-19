# Development Environment (Local)

This folder contains the **local development setup** for the Security Microservice.

The development environment is designed to:
- Run **without Docker**
- Automatically install dependencies
- Run **unit tests before starting the app**
- Support rapid iteration and debugging

---

## 🛠 Tech Stack (Dev)

- Python 3.11+
- FastAPI
- Pytest
- Loguru
- python-dotenv

---

## 📁 Structure

dev/
│
├── app/ # Application source code
├── tests/ # Unit tests
├── requirements.txt # Dev dependencies
├── .env.dev # Development environment variables
├── run-dev.bat # One-click dev runner (Windows)
└── README.md


---

## ⚙️ Environment Configuration

The file `.env.dev` contains development-only configuration such as:

- Fernet encryption key
- Token TTL
- Log level



---

## 🧪 Testing Strategy

- Tests are written using `pytest`
- Tests run **automatically before the app starts**
- Failed tests prevent the server from running

---

## 🚀 How This Is Used

This setup mirrors how backend developers:
- Work locally
- Validate changes with tests
- Run services without containers during development