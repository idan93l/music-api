# 🎵 Music API – Final DevOps Project  
### *(Phase 1: Dockerization + Phase 2: Kubernetes)*

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Docker](https://img.shields.io/badge/Docker-Ready-blue)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Deployed-brightgreen)
![Build](https://img.shields.io/badge/CI-Pending-lightgrey)

---

## 👋 Welcome

Welcome!  
This repository is part of my **DevOps Engineering course final project**.

It demonstrates an end‑to‑end DevOps workflow:

- Python Flask microservice  
- Docker containerization  
- Docker Hub publishing  
- Kubernetes Deployment + Service  
- Autoscaling with HPA  
- Environment configuration via ConfigMap & Secret  
- Scheduled tasks using CronJob  
- Liveness & Readiness probes  
- Thorough documentation  

The project is still **in progress**, improving as the course continues.

---

# 📁 Project Structure

```
music-api/
│
├── app.py                     # Flask application
├── requirements.txt           # Dependencies
├── Dockerfile                 # Container image definition
├── docker-compose.yml         # Local Docker orchestration
├── README.md                  # (This file)
│
└── k8s/                       # Kubernetes manifests
    ├── configmap.yaml
    ├── secret.yaml
    ├── deployment.yaml
    ├── service.yaml
    ├── hpa.yaml
    └── cronjob.yaml
```

---

# 🎯 Phase 1 — Dockerization

Phase 1 includes:

- A Python Flask application  
- A “Hello World” (or better) endpoint  
- Dockerfile creation  
- docker-compose setup  
- Docker Hub image publishing  
- Local environment documentation  

---

## 🎹 Flask Application Overview

### ✔ `GET /`
```
🎶 This is Idan's Music API. Ready to Rock? 🎸
```

### ✔ `GET /beat`
Random rhythm generator.

### ✔ `GET /chord`
Generates a chord based on music theory.

### ✔ `GET /scale`
Returns a random scale or mode.

### ✔ `GET /progression`
Chord progression generator.

### ✔ `GET /health`
Used for Kubernetes probes.

### ✔ `GET /config`
Shows configuration from ConfigMap + Secret.

---

## 🧪 Running Locally (Python)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Test via browser or curl:

```
http://localhost:5000/
http://localhost:5000/beat
http://localhost:5000/chord
http://localhost:5000/scale
http://localhost:5000/progression
```

---

# 🐳 Docker (Phase 1)

### Build image

```bash
docker build -t bourree90s/music-api:v3 .
```

### Run container

```bash
docker run --rm -p 5000:5000 bourree90s/music-api:v3
```

### Docker Hub

```
docker.io/bourree90s/music-api:v3
```

Pull it:

```bash
docker pull bourree90s/music-api:v3
```

---

# 🐚 docker-compose

Start:

```bash
docker-compose up
```

Stop:

```bash
docker-compose down
```

---

# 🚀 Phase 2 — Kubernetes

Phase 2 includes:

- Deployment  
- Service  
- HPA autoscaler  
- ConfigMap  
- Secret  
- CronJob  
- Probes  
- Documentation  

All manifests live inside `k8s/`.

---

# 🏗 Architecture Diagram

```
                 ┌──────────────────────┐
                 │   Music API (Flask)  │
                 │  🎶 /beat /scale ... │
                 └──────────┬───────────┘
                            │ Dockerfile
                            ▼
                   Docker Image (v3)
                            │
                            ▼
               ┌─────────────────────────┐
               │      Kubernetes         │
               │                         │
               │  Deployment (2 pods)    │
               │  Service (NodePort)     │
               │  HPA (autoscaler)       │
               │  ConfigMap + Secret     │
               │  CronJob (curl task)    │
               │  Liveness/Readiness     │
               └─────────────────────────┘
                            │
                            ▼
               Access via `minikube service`
```

---

# 📦 Kubernetes Components

## 1. ConfigMap

Provides non-secret config:

```yaml
APP_NAME: "Idan's Music API"
DEFAULT_BPM: "120"
```

## 2. Secret

Base64‑encoded:

```yaml
SECRET_TOKEN: c3VwZXItc2VjcmV0LXRva2Vu
```

## 3. Deployment

Uses:

```
image: bourree90s/music-api:v3
```

Includes:

- 2 replicas  
- ConfigMap + Secret env  
- Liveness probe  
- Readiness probe  

## 4. Service

NodePort:

```
5000 → 30080
```

## 5. HPA

Autoscaler:

- min: 1  
- max: 5  
- CPU target: 50%  

## 6. CronJob

Runs every 5 minutes:

- Uses curl image  
- Calls `/progression`  

---

# 🌐 Deploying to Kubernetes

### Start Minikube

```bash
minikube start
```

### Apply manifests

```bash
kubectl apply -f k8s/configmap.yaml
kubectl apply -f k8s/secret.yaml
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl apply -f k8s/hpa.yaml
kubectl apply -f k8s/cronjob.yaml
```

### Access service

```bash
minikube service music-api-service --url
```

---

# 🔍 Probes

### Liveness
```
GET /health
```

### Readiness
```
GET /health
```

---

# 🧭 Versioning

| Version | Description |
|--------|-------------|
| v1 | Initial build |
| v2 | Expanded music logic + config |
| v3 | Stable full version deployed to Kubernetes |

Deployment uses:

```
image: bourree90s/music-api:v3
```

---

# 🏁 Conclusion

This project demonstrates:

- Python Flask microservice  
- Docker packaging + Docker Hub publishing  
- docker-compose orchestration  
- Kubernetes Deployment  
- NodePort Service  
- Horizontal Pod Autoscaler  
- ConfigMap / Secret configuration  
- CronJob scheduling  
- Health probes  
- Full documentation  

A complete DevOps workflow, built step‑by‑step.

---

🎸 **Rock on!**
