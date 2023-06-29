import numpy as np

adjacency_matrix_normalized = np.array([
    [0, 0, 1/2, 0, 0],
    [1/3, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1/3, 0, 0, 0, 1],
    [1/3, 1/2, 1, 0, 0]
])

eigenvalues, eigenvectors = np.linalg.eig(adjacency_matrix_normalized)

positive_eigenvector = None
for i in range(len(eigenvalues)):
    autovector = eigenvectors[:, i]
    if all(coord > 0 for coord in autovector):
        positive_eigenvector = autovector
        break

if positive_eigenvector is not None:
    normalized_positive_eigenvector = positive_eigenvector / np.sum(positive_eigenvector)
    real_normalized_positive_eigenvector = np.real(normalized_positive_eigenvector)
    print("Autovetor normalizado com soma igual a 1 e coordenadas estritamente positivas:")
    print(real_normalized_positive_eigenvector)
else:
    print("Nenhum autovetor com todas as coordenadas estritamente positivas foi encontrado.")
