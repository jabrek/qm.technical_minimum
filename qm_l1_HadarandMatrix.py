import numpy as np

phi = np.array([0.866, 0.353 + 0.353j])

hadarand_matrix = (1 / np.sqrt(2)) * np.array([[1, 1], [1, -1]])

transformed_phi = np.dot(hadarand_matrix, phi)  # hadarand_matrix @ phi
print("Transformed phi:", transformed_phi)
