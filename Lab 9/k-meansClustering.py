# K-Means Clustering

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Sample data
X = [[1, 2], [2, 3], [3, 3], [8, 7], [8, 8], [9, 8]]

# Create K-Means model
kmeans = KMeans(n_clusters=2, random_state=0)

# Train the model
kmeans.fit(X)

# Cluster labels
print("Cluster Labels:", kmeans.labels_)

# Cluster centers
print("Cluster Centers:")
print(kmeans.cluster_centers_)

# Plot clusters
plt.scatter([i[0] for i in X], [i[1] for i in X], c=kmeans.labels_)
plt.scatter(kmeans.cluster_centers_[:,0],
            kmeans.cluster_centers_[:,1],
            color='red', marker='X', s=200)

plt.title("K-Means Clustering")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()