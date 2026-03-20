# 📥 HE-MOD_README.md 

# HE-MOD: Hybrid Explainable Multi-Object Tracking Framework

**Candidate:** Vinod Ramanathan  
**Supervisor:** Prof. Dr. Habibollah Haron  
**Institution:** University Malaysia of Computer Science & Engineering (UNIMY)  
**Location:** Puchong, Selangor, Malaysia  
**Date:** March 2026

**First framework (7,166 paper SLR = 0 prior art):**  
Validated Detector XAI + Sanity Checks + Temporal Analysis + Failure Prediction

## 📊 KEY NOVELTY - SLR CONFIRMED

**PRISMA 2020: 7,166 papers → 0 integrated systems**

| Database | Query | Total Hits | 4-Criteria Intersection |
|----------|-------|------------|-------------------------|
| **IEEE Xplore** | XAI ∧ MOT ∧ Temporal | 61,094 | **5 papers** |
| **ACM DL** | XAI ∧ MOT ∧ Temporal | 829K corpus | **249→3 relevant** |
| **arXiv cs.CV** | "explainable object detection" | **375** | **2 relevant** |
| **Google Scholar** | Full 3-way query | **~6,910** | **<20 relevant** |
| **TOTAL** | **7,166 screened** | - | **0/7,166** |

| Criteria | Papers | % |
|----------|--------|----|
| **All 4 criteria** | **0** | **0.00%** |
| **Detector XAI** | **12** | **0.17%** |
| **Tracking + XAI** | **3** | **0.04%** |
| **Temporal XAI** | **0** | **0.00%** |
| **Predictive Failure** | **0** | **0.00%** |

**arXiv VALIDATION:**
```

Q1: "explainable object detection" → 375 hits
Q2: XAI + (detection/tracking) → ~200 hits
Q3: "object detector" "saliency map" → 8 hits
→ 0 papers meet all 4 criteria

```

## 🏗️ SIX-LAYER FRAMEWORK

```

Layer 1: YOLOv8 → Real-time detection (RTX 3060: 80 FPS)
Layer 2: DeepSORT → Track association (Kalman + Hungarian)
Layer 3: Grad-CAM++ → Per-object XAI heatmaps
Layer 4: Adebayo → Sanity checks (SSIM≥40%, ECI≥0.7)
Layer 5: Temporal → Explanation metrics (Entropy/Focus/Variation) ✨
Layer 6: Logistic → Failure Prediction (H₁: AUC>0.7) 💎

```

## 🎯 DEPLOYMENT MODES

| Mode | Layers | FPS Target | Use Case |
|------|--------|------------|----------|
| Mode 1 | 1-2 | 40 FPS | Real-time tracking |
| Mode 2 | 1-4 | 22 FPS | Validated XAI |
| **Mode 3** | **1-6** | **≥20 FPS** | **Full HE-MOD** |

## 📋 EVALUATION PROTOCOL

| Metric | HE-MOD Target | Rationale |
|--------|---------------|-----------|
| MOTA drop | **<20%** | Tracking stability |
| IDF1 drop | **<25%** | Identity preservation |
| IDSW increase | **<30%** | Switch tolerance |
| XAI Sanity | **≥40%** | Adebayo validation |
| Prediction AUC | **>0.7** | H₁ confirmation |

## 🔬 RESEARCH QUESTIONS

1. Can Grad-CAM++ explanations be validated inside MOT pipelines?
2. Do temporal explanation metrics correlate with tracking stability?
3. Can explanation behavior predict identity switches/fragmentation?
4. Does integrated XAI-MOT maintain ≥20 FPS real-time?

## 🔗 RESOURCES

- **Repository:** https://github.com/rvinodsarna/HE-MOD
- **TechRxiv:** DOI forthcoming (March 21, 2026)
- **Supervisor:** Prof. Dr. Habibollah Haron
- **UNIMY:** Computing & Digital Innovation

---

**Universiti Malaysia of Computer Science & Engineering (UNIMY)**  
Level 1 & 2, VSQ@PJ City Centre, Jalan Utara, Section 14  
46200 Petaling Jaya, Selangor, Malaysia  
**Research Base:** Puchong, Selangor  
**First Publication:** March 21, 2026 | 00:52 AM +08
```

