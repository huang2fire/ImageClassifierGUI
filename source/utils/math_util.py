import numpy as np


def softmax(logits: np.ndarray) -> np.ndarray:
    e_x = np.exp(logits - np.max(logits, axis=-1, keepdims=True))

    return e_x / np.sum(e_x, axis=-1, keepdims=True)
