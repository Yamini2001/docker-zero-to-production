# 🐳 Docker Zero to Production

> A practical, hands-on Docker learning repository covering Docker fundamentals, commands, Dockerfiles, networking, volumes, Compose, security, troubleshooting, real-world projects, Docker hacks, and interview preparation.

---

## 📌 About This Repository

This repository documents my journey of learning **Docker from fundamentals to production-oriented concepts**.

The goal is not just to memorize Docker commands, but to understand:

* Why Docker is used
* How Docker works internally
* How images and containers work
* How to create production-oriented Dockerfiles
* How containers communicate
* How persistent storage works
* How multiple services work together using Docker Compose
* How to troubleshoot containers
* How to improve image security and efficiency
* How Docker fits into CI/CD and Kubernetes workflows

The repository combines **theory + commands + hands-on labs + real-world scenarios + troubleshooting + interview preparation**.

---

# 🎯 Learning Goals

By completing this repository, I aim to understand:

```text
Docker Fundamentals
       ↓
Docker Commands
       ↓
Images & Containers
       ↓
Dockerfile
       ↓
Networking
       ↓
Volumes
       ↓
Environment Variables
       ↓
Docker Compose
       ↓
Security
       ↓
Troubleshooting
       ↓
Docker Hacks
       ↓
CI/CD
       ↓
Kubernetes
       ↓
Real-World Projects
```

---

# 🏗️ Docker at a Glance

The basic Docker workflow can be understood as:

```text
                 Developer
                     |
                     ↓
                Dockerfile
                     |
                     ↓
                docker build
                     |
                     ↓
                Docker Image
                     |
                     ↓
               Container Registry
                     |
                     ↓
                docker pull
                     |
                     ↓
                 Container
                     |
          +----------+----------+
          |          |          |
       Network     Volume     Config
          |          |          |
          +----------+----------+
                     |
                     ↓
                Application
```

---

# 📚 Learning Roadmap

## 01. Docker Theory

Learn the core concepts before starting hands-on work.

Topics include:

* What is Docker?
* Why Docker?
* Containerization
* Docker vs Virtual Machines
* Docker Architecture
* Docker Client
* Docker Daemon
* Docker Images
* Docker Containers
* Image vs Container
* Dockerfile
* Docker Registry
* Image Tags
* Docker Volumes
* Docker Networking
* Environment Variables
* Docker Compose
* Docker and Microservices
* Docker and CI/CD
* Docker and Kubernetes
* Docker Layers
* Image Optimization
* Docker Security
* Container Lifecycle
* Stateless vs Stateful Containers
* Restart Policies
* Logging
* Monitoring
* Health Checks

📁 Detailed notes:

```text
01-theory/
```

---

# 💻 02. Docker Commands

A complete command reference is maintained separately.

### Check Docker installation

```bash
docker --version
```

### Docker information

```bash
docker info
```

### Download an image

```bash
docker pull nginx
```

### List images

```bash
docker images
```

### Run a container

```bash
docker run nginx
```

### Run in background

```bash
docker run -d nginx
```

### Run with a custom name

```bash
docker run -d --name my-nginx nginx
```

### Port mapping

```bash
docker run -d -p 8080:80 nginx
```

### List running containers

```bash
docker ps
```

### List all containers

```bash
docker ps -a
```

### Stop a container

```bash
docker stop my-nginx
```

### Start a stopped container

```bash
docker start my-nginx
```

### Restart a container

```bash
docker restart my-nginx
```

### Remove a container

```bash
docker rm my-nginx
```

### View logs

```bash
docker logs my-nginx
```

### Follow logs

```bash
docker logs -f my-nginx
```

### Enter a running container

```bash
docker exec -it my-nginx sh
```

### Inspect a container

```bash
docker inspect my-nginx
```

### Monitor resource usage

```bash
docker stats
```

### List networks

```bash
docker network ls
```

### List volumes

```bash
docker volume ls
```

### Docker disk usage

```bash
docker system df
```

### Docker Compose

```bash
docker compose up -d
```

### Stop Compose application

```bash
docker compose down
```

📁 Detailed command reference:

```text
02-docker-commands/
```

---

# 🐳 03. Dockerfile

A Dockerfile contains instructions used to build a Docker image.

Example:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]
```

Build the image:

```bash
docker build -t myapp:1.0 .
```

Run it:

```bash
docker run myapp:1.0
```

The basic relationship is:

```text
Dockerfile
     ↓
docker build
     ↓
Docker Image
     ↓
docker run
     ↓
Container
```

📁 Dockerfile experiments:

```text
03-dockerfile/
```

---

# 🔗 04. Docker Compose

Docker Compose is useful when an application contains multiple services.

Example:

```text
             Docker Compose
                   |
          +--------+--------+
          |        |        |
       Frontend Backend  Database
          |        |        |
          +--------+--------+
```

Example Compose file:

```yaml
services:

  backend:
    build: ./backend
    ports:
      - "8000:8000"

  database:
    image: postgres:16
    environment:
      POSTGRES_DB: appdb
      POSTGRES_USER: appuser
      POSTGRES_PASSWORD: password
```

Start:

```bash
docker compose up -d
```

Build and start:

```bash
docker compose up -d --build
```

View services:

```bash
docker compose ps
```

View logs:

```bash
docker compose logs -f
```

Stop:

```bash
docker compose down
```

📁 Compose projects:

```text
04-docker-compose/
```

---

# 🌐 05. Docker Networking

Docker containers often need to communicate with other containers.

Example:

```text
Frontend
    |
    ↓
Backend API
    |
    ↓
PostgreSQL
```

Create a network:

```bash
docker network create app-network
```

List networks:

```bash
docker network ls
```

Inspect:

```bash
docker network inspect app-network
```

Containers connected to the same custom network can communicate using service/container names.

📁 Networking labs:

```text
05-networking/
```

---

# 💾 06. Docker Volumes

Containers are often treated as replaceable, but application data may need to persist.

Create a volume:

```bash
docker volume create mydata
```

List volumes:

```bash
docker volume ls
```

Inspect:

```bash
docker volume inspect mydata
```

Example:

```bash
docker run -d \
  --name postgres \
  -v mydata:/var/lib/postgresql/data \
  postgres
```

Concept:

```text
Container
     |
     ↓
Docker Volume
     |
     ↓
Persistent Data
```

Typical use cases:

* Database storage
* Uploaded files
* Persistent application data
* Application-generated files

📁 Volume labs:

```text
06-volumes/
```

---

# 🔐 07. Docker Security

Containerization does not automatically make an application secure.

Important practices include:

### Use trusted base images

```dockerfile
FROM python:3.11-slim
```

### Avoid running unnecessarily as root

```dockerfile
USER appuser
```

### Do not store secrets in images

Avoid:

```dockerfile
ENV DB_PASSWORD=mysecret
```

Instead, provide configuration at runtime and use appropriate secret-management mechanisms for sensitive values.

### Use `.dockerignore`

Example:

```text
.git
.env
__pycache__
*.log
node_modules
```

### Scan images

Security scanning should be incorporated into the development/CI pipeline.

### Keep dependencies updated

Regularly update:

* Base images
* Application dependencies
* System packages

📁 Security examples:

```text
07-security/
```

---

# ⚡ 08. Real-World Projects

The repository will gradually include practical projects.

## Project 1 — Python API

```text
Python API
    ↓
Dockerfile
    ↓
Docker Image
    ↓
Container
```

Concepts:

* Dockerfile
* Image building
* Port mapping
* Environment variables
* Logs
* Health checks

---

## Project 2 — Python API + PostgreSQL

```text
             Docker Compose
                  |
          +-------+-------+
          |               |
       Python API     PostgreSQL
          |               |
          +---------------+
```

Concepts:

* Docker Compose
* Networking
* Volumes
* Environment variables
* Database persistence

---

## Project 3 — Full Stack Application

```text
React
  ↓
Backend API
  ↓
PostgreSQL
```

Concepts:

* Multiple containers
* Docker Compose
* Networking
* Environment configuration
* Production-oriented builds

---

## Project 4 — Big Data Streaming Pipeline

A future project will connect Docker with my Big Data learning:

```text
Python Producer
       ↓
     Kafka
       ↓
    PySpark
       ↓
  PostgreSQL
       ↓
   Dashboard
```

This project will help connect:

```text
Python
  +
SQL
  +
Docker
  +
Kafka
  +
PySpark
  +
Big Data
```

📁 Projects:

```text
08-real-world-projects/
```

---

# 🔥 09. Docker Hacks

This section focuses on practical tricks and troubleshooting techniques.

## Hack 1 — Container exits immediately

Check:

```bash
docker ps -a
```

Then:

```bash
docker logs <container>
```

Inspect:

```bash
docker inspect <container>
```

---

## Hack 2 — Port already in use

Check Docker port mapping:

```bash
docker port <container>
```

Run the application using another host port:

```bash
docker run -p 8081:8080 myapp
```

Concept:

```text
Host :8081
     ↓
Container :8080
```

---

## Hack 3 — Enter a running container

```bash
docker exec -it <container> sh
```

Then investigate:

```bash
ls
pwd
env
```

---

## Hack 4 — Check resource usage

```bash
docker stats
```

Useful for identifying:

* High CPU usage
* High memory usage
* Network activity
* Block I/O

---

## Hack 5 — Check Docker disk usage

```bash
docker system df
```

---

## Hack 6 — Clean unused resources

```bash
docker container prune
```

```bash
docker image prune
```

```bash
docker network prune
```

```bash
docker volume prune
```

```bash
docker system prune
```

> ⚠️ Cleanup commands should be used carefully because they can remove resources you still need.

📁 Docker hacks:

```text
09-docker-hacks/
```

---

# 🛠️ 10. Troubleshooting

Common problems and solutions will be documented here.

| Problem                    | First Checks                  |
| -------------------------- | ----------------------------- |
| Container exits            | `docker ps -a`, `docker logs` |
| Application unavailable    | `docker ps`, `docker port`    |
| Port conflict              | Host port/process check       |
| Container cannot connect   | `docker network inspect`      |
| Database data disappears   | Check volume configuration    |
| Image build fails          | Dockerfile + build logs       |
| High memory usage          | `docker stats`                |
| Permission error           | User/volume permissions       |
| Wrong environment          | Environment variables         |
| Container keeps restarting | Logs + restart policy         |

📁 Troubleshooting:

```text
10-troubleshooting/
```

---

# 🔄 Docker + CI/CD

A typical corporate workflow:

```text
Developer
    ↓
Git Push
    ↓
CI Pipeline
    ↓
Run Tests
    ↓
Docker Build
    ↓
Security Scan
    ↓
Container Registry
    ↓
Deployment
```

Possible tools:

* GitHub Actions
* Jenkins
* GitLab CI/CD
* Cloud container registries
* Kubernetes
* Cloud deployment platforms

---

# ☸️ Docker + Kubernetes

Docker and Kubernetes solve different parts of the container workflow.

```text
Application
     ↓
Dockerfile
     ↓
Docker Image
     ↓
Container Registry
     ↓
Kubernetes
     ↓
Deployment
     ↓
Pods
     ↓
Services
```

Docker is commonly used for image development/build workflows, while Kubernetes provides orchestration capabilities such as:

* Scheduling
* Scaling
* Service discovery
* Rolling updates
* Self-healing
* Desired-state management

📁 Kubernetes integration notes:

```text
01-theory/docker-kubernetes.md
```

---

# 📊 Docker Interview Preparation

Interview questions are organized into three levels.

## Beginner

1. What is Docker?
2. What is containerization?
3. Why is Docker used?
4. What is a Docker image?
5. What is a Docker container?
6. Image vs container?
7. What is a Dockerfile?
8. What is Docker Hub?
9. What is a Docker registry?
10. What is Docker Compose?

## Intermediate

11. Docker vs Virtual Machine?
12. What are Docker volumes?
13. What is Docker networking?
14. What is port mapping?
15. What are Docker image layers?
16. What is `.dockerignore`?
17. What is a multi-stage build?
18. CMD vs ENTRYPOINT?
19. COPY vs ADD?
20. What happens when `docker run` executes?

## Corporate / DevOps

21. How is Docker used in CI/CD?
22. How do you secure Docker images?
23. How do you reduce image size?
24. How do you troubleshoot a container?
25. How do containers communicate?
26. How do you persist database data?
27. How do you pass configuration?
28. How do you handle secrets?
29. How do you monitor containers?
30. How does Docker fit into Kubernetes?

📁 Interview preparation:

```text
11-interview-preparation/
```

---

# 📁 Repository Structure

```text
docker-zero-to-production/
│
├── README.md
│
├── 01-theory/
│   ├── docker-basics.md
│   ├── docker-architecture.md
│   ├── images-vs-containers.md
│   ├── dockerfile.md
│   ├── networking.md
│   ├── volumes.md
│   ├── docker-compose.md
│   ├── docker-security.md
│   └── docker-kubernetes.md
│
├── 02-docker-commands/
│   ├── 01-installation-and-version.md
│   ├── 02-image-commands.md
│   ├── 03-container-commands.md
│   ├── 04-container-lifecycle.md
│   ├── 05-logs-and-debugging.md
│   ├── 06-exec-and-shell.md
│   ├── 07-network-commands.md
│   ├── 08-volume-commands.md
│   ├── 09-docker-compose-commands.md
│   ├── 10-system-cleanup.md
│   └── docker-command-cheatsheet.md
│
├── 03-dockerfile/
├── 04-docker-compose/
├── 05-networking/
├── 06-volumes/
├── 07-security/
├── 08-real-world-projects/
├── 09-docker-hacks/
├── 10-troubleshooting/
├── 11-interview-preparation/
│
├── cheatsheets/
│   ├── docker-commands.md
│   ├── dockerfile-cheatsheet.md
│   └── compose-cheatsheet.md
│
├── .dockerignore
├── .gitignore
└── LICENSE
```

---

# 🚀 Quick Start

Make sure Docker is installed.

Check:

```bash
docker --version
```

Pull an Nginx image:

```bash
docker pull nginx
```

Run it:

```bash
docker run -d --name my-nginx -p 8080:80 nginx
```

Check:

```bash
docker ps
```

Open:

```text
http://localhost:8080
```

View logs:

```bash
docker logs my-nginx
```

Stop:

```bash
docker stop my-nginx
```

Remove:

```bash
docker rm my-nginx
```

---

# 🧠 Core Docker Concept

The most important flow to remember:

```text
Dockerfile
     ↓
docker build
     ↓
Docker Image
     ↓
docker run
     ↓
Docker Container
```

And the corporate deployment flow:

```text
Developer
     ↓
Git
     ↓
CI/CD
     ↓
Docker Build
     ↓
Image Scan
     ↓
Container Registry
     ↓
Kubernetes / Cloud
     ↓
Production
```

---

# 📌 Docker Command Quick Reference

```bash
# Version
docker --version
docker version

# Information
docker info

# Images
docker pull nginx
docker images
docker image ls
docker image inspect nginx
docker rmi nginx

# Build
docker build -t myapp:1.0 .

# Containers
docker run nginx
docker run -d nginx
docker run -d --name my-nginx -p 8080:80 nginx
docker ps
docker ps -a

# Lifecycle
docker start <container>
docker stop <container>
docker restart <container>
docker rm <container>

# Logs
docker logs <container>
docker logs -f <container>

# Debugging
docker exec -it <container> sh
docker inspect <container>
docker top <container>
docker stats

# Network
docker network ls
docker network create app-network
docker network inspect app-network

# Volumes
docker volume ls
docker volume create mydata
docker volume inspect mydata

# Compose
docker compose up
docker compose up -d
docker compose up -d --build
docker compose ps
docker compose logs -f
docker compose down

# Cleanup
docker system df
docker container prune
docker image prune
docker network prune
docker volume prune
docker system prune
```

---

# 🎯 Final Goal

The objective of this repository is to progress from:

```text
"I know Docker commands"
```

to:

```text
"I can containerize, run, debug, secure,
optimize and deploy a real application."
```

---

## 📈 Learning in Public

This repository is part of my ongoing journey into:

```text
Python
   ↓
SQL
   ↓
Docker
   ↓
Cloud / DevOps
   ↓
Kafka
   ↓
PySpark
   ↓
Big Data
   ↓
Kubernetes
```

I will continuously add practical experiments, projects, troubleshooting scenarios, and interview-oriented notes as I learn.

---

## ⭐ Repository Highlights

🐳 Docker Fundamentals
💻 Command Reference
📦 Dockerfile Practicals
🔗 Networking Labs
💾 Volume & Persistence Labs
⚙️ Docker Compose
🔐 Security Practices
🔥 Docker Hacks
🛠️ Troubleshooting
🚀 Real-World Projects
🔄 CI/CD Concepts
☸️ Kubernetes Integration
🎯 Interview Preparation

---

## 🤝 Contributions

Suggestions, corrections, and improvements are welcome.

If you find something useful or have a better approach, feel free to open an issue or submit a pull request.

---

## ⭐ If This Repository Helps You

Consider giving the repository a ⭐ and following along as the learning journey continues.

**Learn → Build → Break → Debug → Improve → Repeat.** 🐳🚀
