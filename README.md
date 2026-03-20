# HE-MOD: Hybrid Explainable Multi-Object Tracking Framework

**Candidate:** Vinod Ramanathan  
**Supervisor:** Prof. Dr. Habibollah Haron  
**Institution:** University Malaysia of Computer Science & Engineering (UNIMY)  
**Location:** Puchong, Selangor, Malaysia  
**Date:** March 2026

**First framework (7,166 paper SLR = 0 prior art):**  
Detector XAI + Sanity Checks + Temporal Analysis + Failure Prediction

## 📊 KEY NOVELTY (Table 6.1)

| Criteria | Papers | % |
|----------|--------|---|
| **All 4 criteria** | **0/7,166** | **0.00%** |
| Detector XAI | 12 | 0.17% |
| Tracking + XAI | 3 | 0.04% |
| **Temporal XAI** | **0** | **0.00%** |
| **Failure Prediction** | **0** | **0.00%** |

## 🏗️ SIX-LAYER FRAMEWORK [Figure 7.1]
Layer 1: YOLOv8 → Real-time detection
Layer 2: DeepSORT → Track association
Layer 3: Grad-CAM++ → Per-object XAI
Layer 4: Adebayo → Sanity (SSIM≥40%)
Layer 5: Temporal → Entropy/Focus/Variation ✨
Layer 6: Logistic → Failure Prediction (H₁) 💎

text

## 🎯 DEPLOYMENT MODES

| Mode | Layers | FPS Target (RTX 3060) |
|------|--------|----------------------|
| Mode 1 | 1-2 | 40 FPS |
| Mode 2 | 1-4 | 22 FPS |
| **Mode 3** | **1-6** | **≥20 FPS** |

## 📋 EVALUATION PROTOCOL

| Metric | Success Threshold |
|--------|------------------|
| MOTA drop | **<20%** |
| IDF1 drop | **<25%** |
| IDSW increase | **<30%** |
| XAI Sanity | **SSIM ≥40%** |
| Prediction | **AUC >0.7** |

---

**Universiti Malaysia of Computer Science & Engineering (UNIMY)**  
**Level 1 & 2, VSQ@PJ City Centre, Jalan Utara, Section 14**  
**46200 Petaling Jaya, Selangor, Malaysia**  
**Research: Puchong, Selangor**  
**First Publication: March 21, 2026**
