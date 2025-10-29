# 🧠 Project Title

**FaceFeel: Federated Emotion Analysis and Learning Platform**
*(A privacy-conscious, web-based AI system for real-time facial emotion detection and continual model improvement through user-contributed data)*

---

## 🎯 1. Project Overview

### Objective

Build a **real-time facial emotion recognition web application** that:

* Detects human emotions from webcam/video frames.
* Runs inference efficiently in-browser using **ONNX Runtime Web**.
* Allows users to **opt-in to share anonymized data** (images + inferred labels) for improving model accuracy over time.
* Supports **continuous fine-tuning** and **federated-style updates** on the server side.

---

### Motivation

Emotion recognition systems often rely on static datasets (e.g., FER2013, AffectNet), which limits generalization to real-world faces, lighting, and angles.
This project aims to:

* Enhance real-world performance via **user-contributed, opt-in data**.
* Demonstrate **privacy-preserving learning** and **efficient model deployment** for emotion analysis.
* Serve as an educational and research project bridging **AI ethics**, **frontend engineering**, and **ML ops**.

---

## 🧩 2. System Workflow

### Step-by-Step Workflow

#### **A. Frontend (Next.js + ONNX Runtime Web)**

1. User accesses the web app.
2. The model runs **fully in-browser** using **ONNX Runtime Web** for real-time emotion recognition.
3. Emotions are displayed live via webcam stream (e.g., emoji overlay + emotion label).
4. User is prompted with an **opt-in data sharing toggle**:

   * If enabled → anonymized image frames + predicted labels are queued for upload.
   * If disabled → everything stays local; no data leaves the browser.

---

#### **B. Data Sharing Pipeline (Server)**

1. Shared frames are compressed, stripped of metadata, and optionally face-blurred or hashed.
2. Data is uploaded to the backend API (FastAPI).
3. Stored securely in **Google Cloud Storage (GCS)**.
4. Metadata (timestamp, confidence score, emotion class, hash ID) stored in **Firestore / Cloud SQL**.

---

#### **C. Fine-tuning Loop (Backend ML Pipeline)**

1. Periodically, a **training pipeline (on GCP Vertex AI or Colab)** fetches opt-in user data.
2. Data is validated, cleaned, and added to a fine-tuning dataset.
3. Fine-tuning occurs on the base model (e.g., `nateraw/fer`) to adapt to real-world diversity.
4. New model version is exported to **ONNX**, **quantized**, and **deployed back to CDN** for browsers.
5. The app automatically fetches the **latest model** via version tag (e.g., `model_v2.1.onnx`).

---

#### **D. Analytics Dashboard (Admin View)**

* Shows aggregated emotion distribution from shared data.
* Displays number of contributors, model accuracy trends, and version changelogs.
* Hosted on a secure internal route (e.g., `/admin`).

---

## 🧠 3. Tech Stack (may subject to change)

| Layer           | Technology                     | Description                          |
| --------------- | ------------------------------ | ------------------------------------ |
| **Frontend**    | **Next.js 15 (React)**         | UI, routing, webcam integration      |
|                 | **ONNX Runtime Web**           | Browser-side inference engine        |
|                 | **TailwindCSS / ShadCN UI**    | Styling and components               |
|                 | **Chart.js / Recharts**        | Emotion visualization charts         |
|                 | **face-api.js / Mediapipe**    | Face detection + tracking            |
| **Backend**     | **FastAPI (Python)**           | REST API for data upload, model info |
|                 | **Google Cloud Run**           | Containerized backend deployment     |
|                 | **Firestore / Cloud SQL**      | Metadata and consent management      |
|                 | **Google Cloud Storage (GCS)** | User-shared data storage             |
| **ML Pipeline** | **PyTorch + Hugging Face**     | Base model training (FER dataset)    |
|                 | **Optimum / ONNX**             | Model conversion and optimization    |
|                 | **Vertex AI / Colab**          | Fine-tuning + re-deployment          |
| **DevOps**      | **Docker + GCP Build**         | CI/CD container automation           |
|                 | **GitHub Actions**             | Model rebuild and redeploy triggers  |

---

## 🔁 4. Data Flow Diagram (Textual)

```
 [User Webcam]
      │
      ▼
 [Next.js Frontend + ONNX Model]
      │
      ├──► Emotion Prediction (Local)
      │
      ├──► (If user consents)
      │        │
      │        ▼
      │   [FastAPI Data API] ──► [GCS + Firestore (may subject to change)]
      │                             │
      │                             ▼
      │                      [Training Pipeline]
      │                             │
      │                             ▼
      └───────────────────────► [Updated ONNX Model vX.Y]
                                     │
                                     ▼
                              [Frontend Model Loader]
```

---

## ⚙️ 5. Milestones & Roles

| Milestone                            | Tasks                                              | Assigned Roles | Deliverables                     | 
| ------------------------------------ | -------------------------------------------------- | -------------- | -------------------------------- | 
| **1️⃣ Setup & Research**             | Dataset exploration (FER2013), baseline testing    | Seniors        | Research doc + baseline notebook | 
| **2️⃣ Model Fine-tuning (v1)**       | Fine-tune `nateraw/fer` on FER2013, export ONNX    | ML Team        | `model_v1.onnx`                  | 
| **3️⃣ Web Inference Prototype**      | Build Next.js page with webcam + emotion overlay   | Frontend Team  | Working live demo                |
| **4️⃣ Backend Data Pipeline**        | FastAPI endpoints for opt-in data upload           | Backend Team   | `/upload` & `/model` APIs        | 
| **5️⃣ Cloud Deployment**             | Deploy FastAPI on Cloud Run, setup GCS & Firestore | DevOps Team    | Deployed API + DB schema         | 
| **6️⃣ Analytics Dashboard**          | Create admin emotion trends dashboard              | Data/Frontend  | `/admin` route + charts          | 
| **7️⃣ Continuous Fine-tuning (v2)**  | Aggregate user data → retrain + redeploy model     | ML Team        | `model_v2.onnx`                  | 
| **8️⃣ Testing & Optimization**       | Quantization, FPS test, latency profiling          | All            | Report + updated pipeline        | 
| **9️⃣ Documentation & Presentation** | Write final report + host demo                     | All            | Docs, pitch deck, demo link      | 
---
