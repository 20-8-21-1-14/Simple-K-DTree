# Simple-K-DTree
## For advance data structure course in University of Information and technology.

This implementation only supports Euclidean distance. 
The points can be any array-like type, e.g: lists, tuples, numpy arrays.
Usage:
1. Make the KD-Tree:
    '''kd_tree = KDTree(points, dim)'''
2. You can then use `get_knn` for k nearest neighbors or 
    '''get_nearest for the nearest neighbor'''
    points are be a list of points: [[0, 1, 2], [12.3, 4.5, 2.3], ...]