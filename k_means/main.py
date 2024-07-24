import math

def find_centroid(cluster: list[tuple]):
    centroid = [0] * len(cluster[0])
    for point in cluster:
        for i in range(len(cluster[0])):
            centroid[i] += (1 / len(cluster)) * point[i]
    
    return tuple(centroid)

def euclidean_distance(point1, point2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(point1, point2)))

def k_means_clustering(points: list[tuple[float, float]], k: int, initial_centroids: list[tuple[float, float]], max_iterations: int) -> list[tuple[float, float]]:
    if max_iterations == 0:
        return [tuple(round(coord, 4) for coord in centroid) for centroid in initial_centroids]

    clusters = [[] for _ in range(k)]

    for point in points:
        distances = [euclidean_distance(point, centroid) for centroid in initial_centroids]
        closest_centroid = distances.index(min(distances))
        clusters[closest_centroid].append(point)

    updated_centroids = [find_centroid(cluster) for cluster in clusters]
    
    return k_means_clustering(points, k, updated_centroids, max_iterations - 1) 

print(k_means_clustering(points = [(1, 2), (1, 4), (1, 0), (10, 2), (10, 4), (10, 0)], k = 2, initial_centroids = [(1, 1), (10, 1)], max_iterations = 10))