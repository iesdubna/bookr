import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
def function_book_analysis(book_a, book_b):
    our_book_analysis = {}
    result = list(set(book_a)&set(book_b))
    for i in range(len(result)):
        key = str(result[i])
        n_book_a = book_a[key]
        n_book_b = book_b[key]
        n = min(n_book_a, n_book_b)
        our_book_analysis[key] = n
    n = len(our_book_analysis)
    m = 2
    arr = [[0] * m for i in range(n)]
    for i in range(n):
        key = str(result[i])
        for j in range(m):
            if(j == 0):
                arr[i][j] = our_book_analysis[key]
    print(result)
    print(arr)
    X = np.array(arr)
    linked = linkage(X, 'single')
    labelList = range(0, len(our_book_analysis))

    plt.figure(figsize=(10, 7))
    dendrogram(linked,
                orientation='top',
                labels=labelList,
                distance_sort='descending',
                show_leaf_counts=True)
    plt.show()

