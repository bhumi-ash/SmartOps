# SmartOps

> **A Self-Healing DevOps Platform**

Monitor • Detect • Recover • Notify

---

## Overview

SmartOps is an automated operations platform built to demonstrate modern DevOps practices in a practical environment. The application monitors the health of Docker containers and system resources, automatically recovers failed services, maintains operational logs, and provides real-time visibility through a web dashboard.

The project follows a modular architecture and integrates technologies such as Docker, Docker Compose, GitHub Actions, and SMTP-based notifications to simulate real-world infrastructure automation workflows.

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

## To begin with:

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