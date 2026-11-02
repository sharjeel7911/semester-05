# %%
class ModelLayer:
    def __init__(
        self,
        layer_name: str,
        learning_rate: float = 0.01,
        initial_weights: list[float] = None,
    ) -> None:
        self.layer_name = layer_name  # public
        self._learning_rate = learning_rate  # protected

        if initial_weights is None:
            initial_weights = []

        self.__weights = initial_weights  # private

    def get_weights(self) -> list[float]:
        return self.__weights.copy()

    def set_weights(self, new_weights: list[float]) -> None:
        if (
            not isinstance(new_weights, list)
            or len(new_weights) == 0
            or not all(
                isinstance(w, (int, float)) and not isinstance(w, bool)
                for w in new_weights
            )
        ):
            raise ValueError("Invalid weight values provided")

        self.__weights = new_weights.copy()


layer = ModelLayer("Dense_1", initial_weights=[0.25, -0.15, 0.40])

# Display public and protected attributes
print("Layer Name:", layer.layer_name)
print("Learning Rate:", layer._learning_rate)

# Access weights using the getter
print("Weights:", layer.get_weights())

# Attempt direct access to the private attribute
try:
    print(layer.__weights)
except AttributeError:
    print("Direct access to __weights is not allowed")

# Print the name-mangled attribute directly
print("Mangled Weights:", layer._ModelLayer__weights)

# Test the setter
layer.set_weights([0.5, 0.6, 0.7])
print("Updated Weights:", layer.get_weights())

# ====================================================================================================


# %%
class DatasetBatcher:
    def __init__(self, data: list, batch_size: int = 2) -> None:
        self.data = data
        self.batch_size = batch_size
        self.current_idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_idx >= len(self.data):
            raise StopIteration

        batch = self.data[self.current_idx : self.current_idx + self.batch_size]

        self.current_idx += self.batch_size
        return batch


# Given dataset
samples = [101, 102, 103, 104, 105, 106, 107]

# Create the batcher
batcher = DatasetBatcher(samples, batch_size=3)

# Manually extract the first two batches
print("First batch:", next(batcher))
print("Second batch:", next(batcher))

# Extract the remaining batches using a for loop
print("Remaining batches:")
for batch in batcher:
    print(batch)


# ====================================================================================================

# %%

from collections.abc import Iterator


def stream_sensor_data(
    signal_readings: list[float], threshold: float = 50.0
) -> Iterator[tuple[int, float, str]]:
    for index, reading in enumerate(signal_readings):
        if reading > threshold:
            yield (index, reading, "ANOMALY")
        else:
            yield (index, reading, "NORMAL")


def filter_anomalies(
    generator_stream: Iterator[tuple[int, float, str]],
) -> Iterator[tuple[int, float, str]]:
    for record in generator_stream:
        if record[2] == "ANOMALY":
            yield record


readings: list[float] = [23.4, 55.1, 48.9, 72.3, 12.0, 99.8, 30.5]

anomalies = filter_anomalies(stream_sensor_data(readings))

for anomaly in anomalies:
    print(anomaly)

# ====================================================================================================

# %%

from collections.abc import Callable


def create_feature_scaler(min_val: float, max_val: float) -> Callable[[float], float]:
    def scale(x: float) -> float:
        return (x - min_val) / (max_val - min_val)

    return scale


# Create two independent scalers
age_scaler: Callable[[float], float] = create_feature_scaler(min_val=18, max_val=65)

grade_scaler: Callable[[float], float] = create_feature_scaler(min_val=0, max_val=20)

# Call the scaler functions
print("Scaled age:", age_scaler(30))
print("Scaled grade:", grade_scaler(15))

# Inspect the closure's preserved variables
print("Closure variable 1:", age_scaler.__closure__[0].cell_contents)
print("Closure variable 2:", age_scaler.__closure__[1].cell_contents)

# ====================================================================================================

# %%


import time
from collections.abc import Callable
from functools import wraps
from typing import Any


def validate_and_time(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        # Validation: reject negative numeric arguments
        for value in (*args, *kwargs.values()):
            if isinstance(value, (int, float)) and not isinstance(value, bool):
                if value < 0:
                    raise ValueError("Negative input parameters are not allowed.")

            # Also validate numeric values inside lists or tuples
            elif isinstance(value, (list, tuple)):
                for item in value:
                    if (
                        isinstance(item, (int, float))
                        and not isinstance(item, bool)
                        and item < 0
                    ):
                        raise ValueError("Negative input parameters are not allowed.")

        # Start timer
        start_time: float = time.perf_counter()

        # Execute the original function
        result: Any = func(*args, **kwargs)

        # Stop timer and print elapsed time
        end_time: float = time.perf_counter()
        elapsed_ms: float = (end_time - start_time) * 1000

        print(f"Execution time: {elapsed_ms:.4f} ms")

        return result

    return wrapper


@validate_and_time
def compute_batch_loss(predictions: list[float], targets: list[float]) -> float:
    if len(predictions) != len(targets):
        raise ValueError("Predictions and targets must have equal lengths.")

    if len(predictions) == 0:
        raise ValueError("Predictions and targets cannot be empty.")

    squared_errors: list[float] = [
        (pred - target) ** 2 for pred, target in zip(predictions, targets)
    ]

    return sum(squared_errors) / len(squared_errors)


# Valid input
loss: float = compute_batch_loss([1.2, 2.5, 3.1], [1.0, 2.0, 3.0])
print("Batch Loss:", loss)

# Invalid input
try:
    compute_batch_loss([-1.0, 2.0], [1.0, 2.0])
except ValueError as error:
    print("Error:", error)
