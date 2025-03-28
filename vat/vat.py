import numpy as np
from scipy.spatial.distance import pdist, squareform

def compute_dissimilarity_matrix(X, metric='euclidean'):
    """
    Compute the dissimilarity matrix for a dataset.
    
    """
    # Compute pairwise distances
    distances = pdist(X, metric=metric)
    
    # Convert to a square matrix
    R = squareform(distances)
    return R

def vat_ordering(R):
    """
    Reorder the dissimilarity matrix according to the VAT algorithm.
    
    """
    n = R.shape[0]
    
    # Initialize the permutation array
    P = np.zeros(n, dtype=int)
    
    # Find the maximum dissimilarity pair to start
    i, j = np.unravel_index(np.argmax(R), R.shape)
    P[0] = i
    
    # Initialize I and J sets
    I = {i}
    J = set(range(n)) - I
    
    # Build the ordering
    for r in range(1, n):
        min_val = float('inf')
        min_i = min_j = -1
        
        # Find the minimum distance between points in I and J
        for i in I:
            for j in J:
                if R[i, j] < min_val:
                    min_val = R[i, j]
                    min_i = i
                    min_j = j
        
        # Add the next point to the ordering
        P[r] = min_j
        I.add(min_j)
        J.remove(min_j)
    
    # Reorder the dissimilarity matrix
    R_ordered = R[np.ix_(P, P)]
    
    return P, R_ordered