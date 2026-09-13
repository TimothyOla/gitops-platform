# GitOps Platform

A complete GitOps platform built with **ArgoCD** and **Kubernetes** (Kind).

This project demonstrates modern GitOps practices where **Git is the single source of truth**. All applications are automatically synchronized and self-healed by ArgoCD.

---

## Features

- Local Kubernetes cluster using Kind
- ArgoCD for continuous delivery
- App of Apps pattern
- Automated sync and self-healing
- Three sample microservices (Product, Order, User)
- Clean and scalable project structure

---

## Architecture
GitHub Repository (Source of Truth)
│
▼
ArgoCD
│
├── root-app (App of Apps)
│     ├── product-service
│     ├── order-service
│     └── user-service
│
▼
Kubernetes Cluster (Kind)
text---

## Project Structure

```bash
gitops-platform/
├── apps/
│   ├── product-service/
│   ├── order-service/
│   └── user-service/
├── argocd/
│   ├── applications/          
│   └── app-of-apps/           
├── infrastructure/            
└── README.md

Prerequisites

Docker
Kind
kubectl
Git


Getting Started
1. Clone the repository
Bashgit clone https://github.com/TimothyOla/gitops-platform.git
cd gitops-platform
2. Create Kind cluster
Bashkind create cluster --name gitops
3. Install ArgoCD
Bashkubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
4. Access ArgoCD UI
Bashkubectl port-forward svc/argocd-server -n argocd 8080:443
Open: https://localhost:8080

Username: admin
Password:Bashkubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | ForEach-Object { [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($_)) }

5. Deploy the Root Application
Bashkubectl apply -f argocd/app-of-apps/root-app.yaml
ArgoCD will automatically deploy all applications.

Verify Deployment
Bashkubectl get applications -n argocd
kubectl get pods
You should see all applications as Synced and Healthy.

How GitOps Works in This Project

You make a change in the Git repository
ArgoCD detects the change
ArgoCD automatically syncs the desired state to the cluster
If someone manually changes the cluster, ArgoCD self-heals it back to the Git state


Author
Timothy Ola

DevOps Learning Portfolio Project

License
This project is for educational and portfolio purposes.
text---

```powershell
git add README.md
git commit -m "Add professional README"
git push