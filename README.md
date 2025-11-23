# 🎵 Music API – Final DevOps Project  
### *(Phase 1: Dockerization + Phase 2: Kubernetes)*

This repository contains **Idan’s Music API**, a musical-themed web application built as the Final DevOps Engineer Course Project.  
It demonstrates real-world DevOps skills across both phases:

- **Phase 1** – Python Flask + Docker + Docker Hub + Compose  
- **Phase 2** – Kubernetes (Deployment, Service, HPA, ConfigMap, Secret, CronJob, Probes)

This README thoroughly documents everything needed for setup, evaluation, and deployment.

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

Phase 1 requires:

- Python Flask application  
- “Hello World” endpoint  
- Dockerfile  
- docker-compose  
- Building/pushing image to Docker Hub  
- Documentation  

Below is everything required and more.

---

## 🎹 Application Overview (Flask)

The application exposes several music-related endpoints:

### `GET /`
Returns a friendly greeting using ConfigMap values:

```
🎶 This is Idan's Music API. Ready to Rock? 🎸
```

### `GET /beat`
Returns a randomized drum pattern:

```json
{
  "bpm": 120,
  "steps": 12,
  "hit_probability": 0.6,
  "pattern": [1,0,1,1,0,0,1,0,1,0,1,1]
}
```

### `GET /chord`
Random chord with theory rules (major/minor/7th/sus/etc.).

### `GET /scale`
Random musical scale or mode (Ionian, Dorian, Phrygian, Pentatonic, Blues, etc.).

### `GET /progression`
Generates a chord progression in a random key.

### `GET /health`
Used for Kubernetes liveness/readiness probes.

### `GET /config`
Shows live configuration derived from ConfigMap & Secret.

---

# 🧪 Running Locally (Python)

### 1. Create virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run

```bash
python app.py
```

### 4. Test

```text
http://localhost:5000/
http://localhost:5000/beat
http://localhost:5000/chord
http://localhost:5000/scale
http://localhost:5000/progression
http://localhost:5000/config
http://localhost:5000/health
```

---

# 🐳 Phase 1 — Running with Docker

### Build the image

```bash
docker build -t bourree90s/music-api:v1 .
```

(You can also build `v2`, `v3`, etc.)

### Run container

```bash
docker run --rm -p 5000:5000 bourree90s/music-api:v1
```

Open: `http://localhost:5000/`

---

## 🐳 Docker Hub

Image repository:

```text
docker.io/bourree90s/music-api
```

Latest version used in Kubernetes:

```text
docker.io/bourree90s/music-api:v3
```

Pull from Docker Hub:

```bash
docker pull bourree90s/music-api:v3
docker run --rm -p 5000:5000 bourree90s/music-api:v3
```

---

# 🐚 Running with docker-compose

The project includes a `docker-compose.yml` file.

### Start

```bash
docker-compose up
```

### Stop

```bash
docker-compose down
```

This is useful for local development with a single command.

---

# 🚀 Phase 2 — Kubernetes Deployment

Phase 2 requires:

- Deployment  
- Service  
- Horizontal Pod Autoscaler  
- ConfigMap  
- Secret  
- CronJob  
- Probes  
- Documentation  

Everything is implemented in the `k8s/` directory.

---

# 📦 Kubernetes Manifests

All Kubernetes resources live in the `k8s/` folder.

## 1. ConfigMap (`k8s/configmap.yaml`)

Provides non-secret configuration:

```yaml
APP_NAME: "Idan's Music API"
DEFAULT_BPM: "120"
```

These values are injected into the container as environment variables.

---

## 2. Secret (`k8s/secret.yaml`)

Opaque secret with Base64-encoded values:

```yaml
SECRET_TOKEN: c3VwZXItc2VjcmV0LXRva2Vu
```

This is mounted as an environment variable in the container and used by the `/config` endpoint.

---

## 3. Deployment (`k8s/deployment.yaml`)

Key properties:

- `apiVersion: apps/v1`
- `kind: Deployment`
- Name: `music-api-deployment`
- **Image:** `bourree90s/music-api:v3`
- Replicas: `2`
- Labels: `app: music-api`
- Uses ConfigMap and Secret for environment variables
- Defines liveness & readiness probes

Example relevant section:

```yaml
containers:
  - name: music-api
    image: bourree90s/music-api:v3
    ports:
      - containerPort: 5000
    env:
      - name: APP_NAME
        valueFrom:
          configMapKeyRef:
            name: music-api-config
            key: APP_NAME
      - name: DEFAULT_BPM
        valueFrom:
          configMapKeyRef:
            name: music-api-config
            key: DEFAULT_BPM
      - name: SECRET_TOKEN
        valueFrom:
          secretKeyRef:
            name: music-api-secret
            key: SECRET_TOKEN
    livenessProbe:
      httpGet:
        path: /health
        port: 5000
      initialDelaySeconds: 10
      periodSeconds: 15
    readinessProbe:
      httpGet:
        path: /health
        port: 5000
      initialDelaySeconds: 5
      periodSeconds: 10
```

---

## 4. Service (`k8s/service.yaml`)

Exposes the application inside and outside the cluster:

- `type: NodePort`
- Cluster port: `5000`
- NodePort: `30080`
- Selector: `app: music-api`

This allows external access via the Minikube node IP and port 30080, or via `minikube service`.

---

## 5. Horizontal Pod Autoscaler (`k8s/hpa.yaml`)

The HPA automatically scales the Deployment based on CPU utilization:

- Min replicas: `1`
- Max replicas: `5`
- Target CPU utilization: `50%`

It watches the `music-api-deployment` and adjusts the number of pods as load changes (assuming metrics-server is installed in the cluster).

---

## 6. CronJob (`k8s/cronjob.yaml`)

A Kubernetes CronJob that runs every 5 minutes:

- Image: `curlimages/curl`
- Command: `curl` to `http://music-api-service:5000/progression`
- Demonstrates scheduled/background work in Kubernetes

This is useful for periodic tasks such as logging or triggering side effects.

---

# 🌐 Deploying to Kubernetes (Minikube Example)

### 1. Start Minikube

```bash
minikube start
```

### 2. Apply ConfigMap and Secret

```bash
kubectl apply -f k8s/configmap.yaml
kubectl apply -f k8s/secret.yaml
```

### 3. Apply Deployment and Service

```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

### 4. Apply HPA and CronJob

```bash
kubectl apply -f k8s/hpa.yaml
kubectl apply -f k8s/cronjob.yaml
```

### 5. Verify all resources

```bash
kubectl get pods
kubectl get svc
kubectl get hpa
kubectl get cronjob
```

You should see:

- Pods from `music-api-deployment`
- `music-api-service` with type `NodePort`
- `music-api-hpa`
- `music-api-cronjob`

---

## Accessing the Service

The recommended way with Minikube:

```bash
minikube service music-api-service --url
```

This prints a URL like:

```text
http://127.0.0.1:49160
```

Open that URL in a browser or with `curl`:

```bash
curl http://127.0.0.1:49160/
curl http://127.0.0.1:49160/beat
curl http://127.0.0.1:49160/scale
curl http://127.0.0.1:49160/config
curl http://127.0.0.1:49160/health
```

The root endpoint should respond with something like:

```text
🎶 This is Idan's Music API. Ready to Rock? 🎸
```

---

# 🔍 Health Probes

The Deployment defines the following probes:

### Liveness Probe

Checks that the container is still running correctly:

```yaml
livenessProbe:
  httpGet:
    path: /health
    port: 5000
  initialDelaySeconds: 10
  periodSeconds: 15
```

### Readiness Probe

Checks that the application is ready to receive traffic:

```yaml
readinessProbe:
  httpGet:
    path: /health
    port: 5000
  initialDelaySeconds: 5
  periodSeconds: 10
```

These are crucial for reliable rolling updates and stability in Kubernetes.

---

# 🧭 Versioning Strategy

Each meaningful change in the application results in a new Docker image tag:

- `v1` – Initial Dockerized version  
- `v2` – Extended musical features and configuration  
- `v3` – Stable final image used in Kubernetes (fixed `/beat`, emojis, `/config`, etc.)

The Deployment uses:

```yaml
image: bourree90s/music-api:v3
```

This is the version expected to be deployed in the cluster.

---

# 🏁 Conclusion

This project demonstrates the full DevOps lifecycle:

- ✅ Python Flask application development  
- ✅ Docker containerization and image publishing  
- ✅ docker-compose for local orchestration  
- ✅ Kubernetes Deployment & Service  
- ✅ Horizontal Pod Autoscaling (HPA)  
- ✅ ConfigMap & Secret management  
- ✅ CronJob for scheduled tasks  
- ✅ Liveness & Readiness probes  
- ✅ Clear, end-to-end documentation for both Phase 1 and Phase 2  

It fully satisfies the requirements for the **Final DevOps Engineer Course Project** (Phases 1 + 2), while adding a fun and practical musical theme.

---

🎉 **Enjoy, extend, and rock on!** 🎸
