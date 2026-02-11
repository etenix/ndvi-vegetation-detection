import numpy as np


def min_max_normalize(data):
    min_val = np.min(data)
    max_val = np.max(data)

    normalized = (data - min_val) / (max_val - min_val)

    return normalized


if __name__ == "__main__":
    test = np.random.rand(100, 100)

    result = min_max_normalize(test)

    print("Normalized:", result.min(), result.max())