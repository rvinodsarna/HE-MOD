# HE-MOD: Hybrid Explainable Multi-Object Tracking Framework

**Candidate:** Vinod Ramanathan  
**Supervisor:** Prof. Dr. Habibollah Haron  
**Institution:** University Malaysia of Computer Science & Engineering (UNIMY)  
**Location:** Puchong, Selangor, Malaysia  
**Date:** March 2026

## 🚀 **Focus: Real-Time Validated XAI Pipeline**

HE-MOD delivers a **production-ready MOT system** with **consumer-grade deployment** (RTX 3060, ≥20 FPS target) featuring **Grad-CAM++ explanations** validated via **Adebayo sanity checks**.

## 🏗️ **HE-MOD Deployment Modes**

| **Mode** | **Layers** | **FPS Target** | **Use Case** |
|----------|------------|----------------|--------------|
| **Mode 1** | Detection + Tracking | **40 FPS** | Pure real-time MOT |
| **Mode 2** | + Validated XAI | **22 FPS** | Explainable tracking |
| **Mode 3** | Full pipeline | **≥20 FPS** | Production deployment |

## ⚙️ **Tech Stack**
Layer 1: YOLOv8-s (80 FPS baseline)
Layer 2: DeepSORT (Kalman + appearance)
Layer 3: Grad-CAM++ (per-object heatmaps)
Layer 4: Adebayo sanity (SSIM ≥40%)
Deployment: RTX 3060 12GB (RM1,800)

text

## 📊 **Target Performance**

| **Metric** | **Target** | **Hardware** |
|------------|------------|--------------|
| End-to-End FPS | **≥20** | RTX 3060 |
| Sanity Check | **SSIM ≥40%** | Adebayo validation |
| Latency | **<50ms** | Frame processing |

## 🎯 **Smart City Applications**

- **Traffic monitoring** (UA-DETRAC benchmark)
- **CCTV surveillance** (Malaysian urban proxy)
- **Automated toll collection**
- **Public safety analytics**

## 🔬 **Research Questions**

1. Can validated XAI maintain real-time MOT performance?
2. Does explanation quality correlate with tracking stability?
3. How do sanity checks impact deployment latency?

## 🔗 **Resources**

- **Repository:** [github.com/rvinodsarna/HE-MOD](https://github.com/rvinodsarna/HE-MOD)
- **Institution:** UNIMY Computing PhD Programme
- **Location:** Puchong, Selangor, Malaysia
- **Contact:** `vinod.ramanathan@unimy.edu.my`

---

**UNIMY | Universiti Malaysia of Computer Science & Engineering**  
**Level 1 & 2, VSQ@PJ City Centre, Jalan Utara, Section 14**  
**46200 Petaling Jaya, Selangor, Malaysia**
