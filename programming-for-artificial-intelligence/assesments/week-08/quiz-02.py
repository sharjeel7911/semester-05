# %%
from datetime import datetime

import numpy as np


class BaseBatch:
    def __init__(self):
        pass


class LoggingMixin:
    def log_operation(self, message: str) -> None:
        timestamp = datetime.now()
        print(f"Time: [{timestamp}] {message}")


class ImageBatch(LoggingMixin, BaseBatch):
    def __init__(self, images: np.ndarray, labels: np.ndarray):
        if images.ndim != 4:
            raise ValueError("Error: Images array not 4D")

        if labels.ndim != 1:
            raise ValueError("Error: Labels array not 1D")

        if images.shape[0] != labels.shape[0]:
            raise ValueError("Error: Number of images and labels don't match")

        self.images = images
        self.labels = labels

    def __add__(self, other: "ImageBatch") -> "ImageBatch":
        if not isinstance(other, ImageBatch):
            raise TypeError("Error: Objects types are not same")

        if self.images.shape[1:] != other.images.shape[1:]:
            raise ValueError("Error: Image dimensions mismatch")

        images = np.concatenate((self.images, other.images), axis=0)
        labels = np.concatenate((self.labels, other.labels), axis=0)

        self.log_operation(
            f"Concatenating two batches of size "
            f"{len(self.labels)} and {len(other.labels)}."
        )
        return ImageBatch(images, labels)

    def display_metadata(self) -> None:
        print("Shape:", self.images.shape)
        print("Data Type:", self.images.dtype)

        unique_labels, counts = np.unique(self.labels, return_counts=True)

        print("Unique Label Counts:")
        for label, count in zip(unique_labels, counts):
            print(label, ":", count)


i1 = np.random.rand(5, 64, 64, 3)
l1 = np.array([0, 1, 0, 1, 2])

i2 = np.random.rand(3, 64, 64, 3)
l2 = np.array([2, 1, 0])

batch1 = ImageBatch(i1, l1)
batch2 = ImageBatch(i2, l2)

batch3 = batch1 + batch2

batch3.display_metadata()

# ====================================================================================================

# i used np.concatenate(axis=0) to combine samples from both batches and checked image dimensions to avoid shape mismatch.
# images and labels are concatenated separately to maintain alignment and a new object is returned to preserve the original batches.
