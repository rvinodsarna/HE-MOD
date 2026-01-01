"""
HE-MOD: Hybrid Explainable Moving Object Detection
PhD Defense Project - Complete Implementation
"""

__version__ = "1.0.0"
__author__ = "Vinod Ramanathan"
__email__ = "vinod@unimy.edu"

from .model import HEMOD
from .fusion import WeightedFusion
from .xai import GradCAMPlusPlus
from .kalman_tracker import KalmanTracker
from .optical_flow import FarnebackFlow

__all__ = [
    'HEMOD',
    'WeightedFusion', 
    'GradCAMPlusPlus',
    'KalmanTracker',
    'FarnebackFlow'
]