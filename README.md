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
- Jenkins CI/CD pipeline

---

# 📁 Project Structure

```
music-api/
│
├── app.py                     # Flask application
├── requirements.txt           # Dependencies
├── Dockerfile                 # Container image definition
├── docker-compose.yml         # Local Docker orchestration
├── Jenkinsfile                # CI/CD pipeline
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

---

# 🎯 Phase 1 — Dockerization

- Flask microservice
- Dockerfile
- docker-compose
- Docker Hub publishing

```bash
docker build -t bourree90s/music-api:0.3 .
docker run --rm -p 5000:5000 bourree90s/music-api:0.3
```

---

# 🚀 Phase 2 — Kubernetes

Phase 2 uses raw Kubernetes manifests (`k8s/`):

- Deployment
- Service
- ConfigMap & Secret
- Health probes
- HPA
- CronJob

```bash
kubectl apply -f k8s/
```

---

# 🧩 Phase 3 — Helm

Helm is used as the **primary deployment method**.

```bash
minikube start
helm upgrade --install music-api-test helm/music-api
minikube service music-api-test
```

### Health Checks

```
GET /health
```

---

# 🤖 CI/CD — Jenkins

This project includes a **Jenkinsfile** implementing a CI/CD pipeline.

Pipeline stages:
1. Checkout code
2. Build Docker image
3. Push image to Docker Hub
4. Deploy to Kubernetes using Helm

Key deployment command:

```bash
helm upgrade --install music-api-test helm/music-api
```

---

# 🧭 Versioning

| Version | Description |
|--------|-------------|
| v1 | Flask + Docker |
| v2 | Kubernetes manifests |
| v3 | Helm + Jenkins pipeline |

---

# 🏁 Conclusion

This project demonstrates a complete DevOps workflow:

- Dockerized Flask service
- Kubernetes deployment
- Helm packaging
- Jenkins CI/CD automation
- Health monitoring
- Clear documentation

---

🎸 **Rock on!**
