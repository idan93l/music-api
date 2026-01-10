# 🎵 Music API – Final DevOps Project
### *(Phase 1: Dockerization · Phase 2: Kubernetes · Phase 3: Helm & CI/CD Ready)*

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Docker](https://img.shields.io/badge/Docker-Ready-blue)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Deployed-brightgreen)
![Helm](https://img.shields.io/badge/Helm-Deployed-blueviolet)
![CI](https://img.shields.io/badge/Jenkins-Ready-orange)

---

## 👋 Welcome

Welcome!  
This repository is part of my **DevOps Engineering course final project**.

It demonstrates an end-to-end DevOps workflow:

- Python Flask microservice
- Docker containerization
- Docker Hub publishing
- Kubernetes Deployment + Service
- Health checks (Liveness & Readiness)
- Helm-based Kubernetes packaging
- CI/CD-ready deployment workflow

The project evolves gradually across course phases.

---

# 📁 Project Structure

```
music-api/
│
├── app.py                     # Flask application
├── requirements.txt           # Dependencies
├── Dockerfile                 # Container image definition
├── docker-compose.yml         # Local Docker orchestration
├── README.md                  # Documentation
│
├── k8s/                       # Raw Kubernetes manifests (Phase 2)
│   ├── configmap.yaml
│   ├── secret.yaml
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── hpa.yaml
│   └── cronjob.yaml
│
└── helm/                      # Helm chart (Phase 3)
    └── music-api/
        ├── Chart.yaml
        ├── values.yaml
        └── templates/
            ├── deployment.yaml
            ├── service.yaml
            ├── ingress.yaml
            ├── httproute.yaml
            ├── serviceaccount.yaml
            └── _helpers.tpl
```

> ℹ️ The `k8s/` directory is kept for learning and comparison.  
> **Helm is the preferred deployment method from Phase 3 onward.**

---

# 🎯 Phase 1 — Dockerization

Phase 1 includes:

- Python Flask application
- Dockerfile creation
- docker-compose setup
- Docker Hub image publishing
- Local development documentation

---

## 🎹 Flask Application Overview

### ✔ `GET /`
🎶 This is Music API, Ready to Rock? 🎸

### ✔ `GET /beat`
Random rhythm generator.

### ✔ `GET /chord`
Generates a chord based on music theory.

### ✔ `GET /scale`
Returns a random scale or mode.

### ✔ `GET /progression`
Chord progression generator.

### ✔ `GET /health`
Health endpoint used for Kubernetes probes.

### ✔ `GET /config`
Shows application configuration.

---

## 🧪 Running Locally (Python)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

---

# 🐳 Docker (Phase 1)

```bash
docker build -t bourree90s/music-api:0.3 .
docker run --rm -p 5000:5000 bourree90s/music-api:0.3
```

---

# 🚀 Phase 3 — Helm

```bash
minikube start
helm upgrade --install music-api-test helm/music-api
minikube service music-api-test
```

---

# 🤖 CI/CD Ready

Deployment command used by CI/CD:

```bash
helm upgrade --install music-api-test helm/music-api
```

---

🎸 **Rock on!**
