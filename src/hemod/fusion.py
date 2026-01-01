class WeightedFusion:
    """Weighted fusion of CNN, optical flow, and Kalman predictions"""
    
    def __init__(self, weights=(0.6, 0.25, 0.15)):
        self.weights = weights
        print(f"Fusion initialized with weights: CNN={weights[0]}, Flow={weights[1]}, Kalman={weights[2]}")
    
    def fuse(self, cnn_scores, flow_scores, kalman_scores):
        """Fuse scores with weighted combination"""
        return (self.weights[0] * cnn_scores + 
                self.weights[1] * flow_scores + 
                self.weights[2] * kalman_scores)