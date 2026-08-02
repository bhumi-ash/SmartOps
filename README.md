# SmartOps

> **A Self-Healing DevOps Platform**

Monitor • Detect • Recover • Notify

---

## Overview

SmartOps is a self-healing DevOps platform built using Python, Flask, Docker, and GitHub Actions.

The platform continuously monitors system resources and Docker containers. When a monitored container stops unexpectedly, SmartOps automatically detects the failure, restarts the container, logs the incident, records the recovery action, and sends an email notification to the administrator.

The application itself is fully containerized using Docker and uses GitHub Actions for Continuous Integration.

---

## Features

- System Resource Monitoring (CPU, RAM, Disk)
- Docker Container Monitoring
- Automatic Container Recovery
- Incident Logging
- Recovery Activity Tracking
- Email Notifications
- Health Status Dashboard
- Dockerized Deployment
- Docker Compose Support
- GitHub Actions CI Pipeline

---

## 🛠 Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python |
| Backend | Flask |
| Monitoring | psutil |
| Containerization | Docker |
| Orchestration | Docker Compose |
| CI | GitHub Actions |
| Notifications | Gmail SMTP |
| Version Control | Git & GitHub |

---

## 🏗️ System Architecture

```text
                     +----------------------+
                     |      Browser         |
                     +----------+-----------+
                                |
                                ▼
                     +----------------------+
                     |   Flask Dashboard    |
                     +----------+-----------+
                                |
        +-----------------------+-----------------------+
        |                       |                       |
        ▼                       ▼                       ▼
+----------------+     +----------------+     +----------------+
| System Monitor |     | Docker Monitor |     | Health Engine  |
+----------------+     +----------------+     +----------------+
                                |
                                ▼
                     +----------------------+
                     | Docker SDK (Python)  |
                     +----------+-----------+
                                |
                                ▼
                     +----------------------+
                     |    Docker Engine     |
                     +----------+-----------+
                                |
               +----------------+----------------+
               |                                 |
               ▼                                 ▼
      +----------------+               +----------------+
      | Self-Healing   |               | Incident Log   |
      +----------------+               +----------------+
               |                                 |
               ▼                                 ▼
      +----------------+               +----------------+
      | Email Alerts   |               | Recovery Log   |
      +----------------+               +----------------+
```

## 🚀 Getting Started

### Clone the Repository

```bash
git clone https://github.com/<bhumi-ash>/SmartOps.git

cd SmartOps
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run SmartOps

```bash
python run.py
```

## 🐳 To run with Docker (Recommended)

```bash
docker compose up --build
```

SmartOps will be available at:

http://localhost:5000