# 🚀 Cloud-Native DevOps Platform

> From code commit to Kubernetes deployment, monitoring, and real-time alerting — fully automated.

![CI/CD](https://img.shields.io/badge/CI/CD-GitHub%20Actions-success)
![Docker](https://img.shields.io/badge/Docker-Multi--Architecture-blue)
![Kubernetes](https://img.shields.io/badge/Kubernetes-K3s-326CE5)
![Helm](https://img.shields.io/badge/Helm-Packaged-0F1689)
![Terraform](https://img.shields.io/badge/Terraform-IaC-623CE4)
![Prometheus](https://img.shields.io/badge/Monitoring-Prometheus-E6522C)
![Grafana](https://img.shields.io/badge/Grafana-Dashboards-F46800)
![Alertmanager](https://img.shields.io/badge/Alerts-Telegram-success)

---

# 🎯 Project Goal

This project simulates a modern DevOps environment used in production systems.

The objective was not only to deploy an application, but also to build the surrounding ecosystem required to operate, monitor, troubleshoot, and continuously deliver software in a cloud-native environment.

The platform includes:

✅ Containerization
✅ CI/CD Automation
✅ Infrastructure as Code
✅ Kubernetes Orchestration
✅ Helm Packaging
✅ Monitoring & Observability
✅ Alerting & Incident Notification

---

# 🏛 System Architecture

```text
                   ┌─────────────────┐
                   │    Developer    │
                   └────────┬────────┘
                            │
                            ▼
                   ┌─────────────────┐
                   │     GitHub      │
                   └────────┬────────┘
                            │ Push
                            ▼
              ┌──────────────────────────┐
              │ GitHub Actions Pipeline  │
              └────────┬─────────────────┘
                       │
                       ▼
              ┌──────────────────────────┐
              │  Docker Hub Registry     │
              └────────┬─────────────────┘
                       │
                       ▼
            ┌──────────────────────────────┐
            │ Kubernetes Cluster (K3s)     │
            └─────────────┬────────────────┘
                          │
                 ┌────────┴────────┐
                 ▼                 ▼
          ┌─────────────┐   ┌─────────────┐
          │   Service   │   │   Helm      │
          └──────┬──────┘   └─────────────┘
                 │
                 ▼
         ┌─────────────────┐
         │ Flask Todo App  │
         └─────────────────┘

──────────────────────────────────────────

      Prometheus ───► Grafana

      Alertmanager ─► Telegram
```

---

# 🔥 Highlights

### 🚢 Multi-Architecture Docker Images

Built and published images for:

* linux/amd64
* linux/arm64

This allows the same image to run seamlessly on:

* Apple Silicon (M1/M2/M3)
* ARM Servers
* Raspberry Pi
* Cloud VMs
* Traditional x86 Infrastructure

---

### ☸ Kubernetes Deployment

Application is deployed on a K3s cluster using:

* Deployments
* Services
* Health Checks
* Rolling Updates
* Self-Healing Pods

A failed container is automatically restarted by Kubernetes.

---

### 📦 Helm Packaging

Deployment manifests are managed through Helm Charts.

Benefits:

* Reusable deployments
* Versioned releases
* Easy upgrades
* Environment-specific configuration

---

### ⚙️ Infrastructure as Code

Infrastructure provisioning is managed with Terraform.

Everything is defined declaratively and can be recreated consistently.

---

### 🔄 Automated CI/CD

Every push to the main branch triggers:

```text
Code Push
    │
    ▼
Run Tests
    │
    ▼
Build Docker Image
    │
    ▼
Build Multi-Arch Image
    │
    ▼
Push to Docker Hub
```

No manual image building required.

---

### 📊 Monitoring & Observability

Prometheus continuously scrapes metrics from:

* Application
* Kubernetes
* Node Exporter

Grafana dashboards provide real-time visibility into:

* CPU Usage
* Memory Usage
* Pod Health
* Node Metrics
* Application Metrics

---

### 🚨 Real-Time Alerting

Alertmanager is integrated with Telegram.

Example alerts:

🔥 High CPU Usage

🔥 High Memory Usage

🔥 Pod CrashLoopBackOff

🔥 Application Unreachable

🔥 Node Down

Notifications are delivered instantly to Telegram.

---

# 🧰 Technology Stack

| Layer              | Technologies            |
| ------------------ | ----------------------- |
| Application        | Flask                   |
| Database           | PostgreSQL              |
| Runtime            | Gunicorn                |
| Containers         | Docker                  |
| Registry           | Docker Hub              |
| CI/CD              | GitHub Actions          |
| Infrastructure     | Terraform               |
| Orchestration      | Kubernetes (K3s)        |
| Package Management | Helm                    |
| Monitoring         | Prometheus              |
| Visualization      | Grafana                 |
| Alerting           | Alertmanager + Telegram |
| OS                 | Ubuntu Linux            |

---

# 📂 Repository Structure

```text
devops-lab
│
├── .github/workflows
│   └── ci.yml
│
├── todo-app
│   ├── app.py
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── tests/
│   ├── terraform/
│   ├── k8s/
│   └── helm/
│
└── monitoring/
```


---


# 💡 Key DevOps Skills Demonstrated

* Linux Administration
* Git & GitHub
* Docker
* Multi-Architecture Images
* Docker Hub
* CI/CD Pipelines
* GitHub Actions
* Infrastructure as Code
* Terraform
* Kubernetes
* Helm
* Monitoring
* Alerting
* Observability
* Production Troubleshooting
* Incident Response

---

# 🚀 Future Improvements

* ArgoCD (GitOps)
* Ingress & Reverse Proxy
* TLS Certificates
* Secret Management
* Kubernetes Security Hardening
* Cloud Deployment (AWS)

---

# 👨‍💻 Author

**Saros Shojaei**

Computer Engineer
DevOps Engineer Journey

Building cloud-native systems, automation pipelines, and modern infrastructure.
