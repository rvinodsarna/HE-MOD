# HE-MOD: Hybrid Explainable Multi-Object Tracking Framework

**First framework** (7,166 paper SLR = 0 prior art):
- Detector XAI + Sanity Checks + Temporal Analysis + Failure Prediction

## 📊 KEY NOVELTY (Table 6.1)
| Criteria | Papers | %
|----------|--------|---|
| **All 4 criteria** | **0/7,166** | **0.00%** |
| Detector XAI | 12 | 0.17% |

## 🏗️ SIX-LAYER FRAMEWORK
Layer 1: YOLOv8 → Detection
Layer 2: DeepSORT → Tracking
Layer 3: Grad-CAM++ → Explanations
Layer 4: Adebayo → Sanity (SSIM≥40%)
Layer 5: Temporal Metrics → Entropy/Focus/Variation
Layer 6: Logistic → Failure Prediction (H1)


## 🎯 DEPLOYMENT MODES
- Mode 1: Layers 1-2 (40 FPS target)
- Mode 2: Layers 1-4 (22 FPS target) 
- Mode 3: Layers 1-6 (≥20 FPS target)

**UNIMY PhD Computing | March 21, 2026**
