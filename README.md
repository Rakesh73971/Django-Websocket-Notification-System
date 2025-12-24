
# 🔔 Django WebSocket Notification System

A real-time notification system built using **Django**, **Django Channels**, **WebSockets**, **Redis**, and **Docker**.
This project demonstrates how to push live notifications from server to clients using WebSocket connections.

---

## 🚀 Features

* Real-time notifications using WebSockets
* Django Channels with ASGI support
* Redis as Channel Layer backend
* Dockerized setup (App + Redis)
* Simple frontend for sending & receiving notifications
* Production-style architecture (Daphne server)

---

## 🛠️ Tech Stack

* **Backend:** Django, Django Channels
* **WebSockets:** ASGI, Daphne
* **Message Broker:** Redis
* **Containerization:** Docker, Docker Compose
* **Frontend:** HTML, JavaScript (WebSocket API)

---

## 📁 Project Structure

```
notification-1/
│
├── app/                    # Django app (consumers, routing)
├── notification/           # Django project (settings, asgi)
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── manage.py
├── db.sqlite3
└── README.md
```

---

## ⚙️ Requirements

Make sure you have the following installed:

* Docker
* Docker Compose

(No need to install Python locally 🎯)

---

## 📦 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/django-websocket-notifications.git
cd notification-1
```

---

### 2️⃣ Build & Run with Docker

```bash
docker-compose up --build
```

This will start:

* Django app on **port 8000**
* Redis on **port 6379**

---

### 3️⃣ Open in Browser

```
http://localhost:8000
```

WebSocket endpoint:

```
ws://localhost:8000/ws/notifications/
```

---

## 🧠 How It Works

1. Client establishes a WebSocket connection
2. Django Channels handles the connection via ASGI
3. Messages are routed through Redis channel layers
4. Connected clients receive real-time notifications instantly

---

## 📜 Example WebSocket Message

**Client sends:**

```json
{
  "message": "New notification!"
}
```

**All connected clients receive:**

```json
{
  "message": "New notification!"
}
```

---

## 🐳 Docker Services

### Web Service

* Runs Django using Daphne
* Handles HTTP + WebSocket traffic

### Redis Service

* Acts as a message broker for Channels
* Enables real-time communication

---

## ⚠️ Important Notes

* `runserver` is NOT used (WebSockets need ASGI server)
* `daphne` is used for production-ready WebSocket support
* Redis hostname is `redis` (Docker service name)

---


