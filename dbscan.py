def next_id(cluster_id):
    return cluster_id + 1

UNCLASSIFIED = -1
NOISE = 0
import math
def metric(x, y):
    return math.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)

def region_query(pcd, i, eps):
    p = i
    s = set()
    for point in pcd:
        r = metric(p, point)
        if  r <= eps and r > 0:
            s.add(point)
    return s

def expand_cluster(point_cloud, labels, i, cluster_id, eps, minPts):
    labels[cluster_id] = set(point_cloud[i])
    seed = region_query(point_cloud, point_cloud[i], eps)
    if len(seed) < minPts:
        labels[NOISE].add(point_cloud[i])
        return False
    for p in seed:
        labels[cluster_id].add(p)
    while len(seed) != 0:
        curr = seed.pop()
        result = region_query(point_cloud, curr, eps)
        if len(result) >= minPts:
            for k in result:
                if k in labels[NOISE]:
                    if k not in labels.items():
                        seed.add(k)
                    # unija svih
                    labels[cluster_id].add(k)
    return True





    
"""
DBSCAN : POINT_CLOUD -> CLUSTERING
input:      point_cloud: tuple
            eps:    double
            minPts: int
output:     clustering: dictionary

"""
def dbscan(point_cloud, eps, minPts):
    cluster_id = next_id(NOISE)
    labels = {}
    labels[NOISE] = set()
    labeled = set()
    for i in range(0, len(point_cloud)):
        if i in labeled:
            continue
        labeled.add(i)
        if expand_cluster(point_cloud, labels, i, cluster_id, eps, minPts):
            cluster_id = next_id(cluster_id)
    return labels

#TODO: dozvoliti promjenu metrike, implementirati R*, dozvoliti arbitrarne labele
#PROBLEM: O(n^2) i osjeti se