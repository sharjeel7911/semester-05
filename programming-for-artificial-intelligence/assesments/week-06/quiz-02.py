# %%
# Task - 01
def compress_sparse_vector(dense_vector: list[float], threshold: float = 0.01) -> list:
    result = [(i, x) for i, x in enumerate(dense_vector) if abs(x) > threshold]
    return result


dense_vector = [0.0, 0.85, -0.002, 1.45, 0.0, -0.62, 0.009]
print(compress_sparse_vector(dense_vector))

# ====================================================================================================


# %%
# Task - 02
def build_vocab_index(corpus: list[str]) -> dict[str, dict[str, int]]:
    unique_tokens = sorted({token for doc in corpus for token in doc.lower().split()})
    result = {
        token: {"token_id": idx, "char_len": len(token)}
        for idx, token in enumerate(unique_tokens)
    }
    return result


corpus = ["AI is transformative", "data is fuel for AI"]
vocab = build_vocab_index(corpus)
for token, info in vocab.items():
    print(f"{token!r}: {info}")

# ====================================================================================================


# %%
# Task - 03


def clamp_and_label_signals(
    readings: list, lower_bound: float = -1.0, upper_bound: float = 1.0
) -> list:
    result = [
        "UPPER_CLAMP"
        if x > upper_bound
        else "LOWER_CLAMP"
        if x < lower_bound
        else round(x, 2)
        for x in readings
    ]
    return result


signals = [-2.5, -0.456, 0.123, 1.89, 0.999, -1.05]
print(clamp_and_label_signals(signals))

# ====================================================================================================


# %%
# Task - 04
def categorize_student_records(student_ids: list, final_scores: list) -> dict:
    result = {
        student_id: {
            "score": score,
            "tier": (
                "Distinction"
                if score >= 85
                else "Satisfactory"
                if score >= 60
                else "Remedial"
            ),
        }
        for student_id, score in zip(student_ids, final_scores)
    }
    return result


student_ids = ["ST_101", "ST_102", "ST_103", "ST_104", "ST_105"]
final_scores = [92, 45, 78, 58, 81]
records = categorize_student_records(student_ids, final_scores)

print(records["ST_102"]["tier"])  # Remedial
print(records["ST_101"]["tier"])  # Distinction

# ====================================================================================================

# %%
# Task - 05
from typing import Any, Callable


def init_model(
    model_type: str, learning_rate: float = 0.01, epochs: int = 100, **options: Any
) -> dict:
    result = {
        "model_type": model_type,
        "learning_rate": learning_rate,
        "epochs": epochs,
        "options": options,
    }
    return result


def audit_wrapper(func: Callable, *args: Any, **kwargs: Any) -> Any:
    args = list(args)

    # learning_rate is the 2nd positional parameter of init_model (after model_type)
    if "learning_rate" in kwargs:
        lr = kwargs["learning_rate"]
        if not (0.0 < lr <= 1.0):
            print(
                f"Warning: learning_rate = {lr} out of range (0.0, 1.0]. Clamped to 0.01."
            )
            kwargs["learning_rate"] = 0.01
    elif len(args) > 1:
        lr = args[1]
        if not (0.0 < lr <= 1.0):
            print(
                f"Warning: learning_rate = {lr} out of range (0.0, 1.0]. Clamped to 0.01."
            )
            args[1] = 0.01
    kwargs.update({"audit_logged": True})
    return func(*args, **kwargs)


result = audit_wrapper(
    init_model, "GradientBoost", learning_rate=3.5, epochs=250, subsample=0.8
)
print(result)

# ====================================================================================================

# %%
# Task - 06
from functools import wraps
from typing import Any, Callable


def retry_on_failure(max_retries: int = 3, fallback_value: Any = None) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as err:
                    print(f"Attempt {attempt}/{max_retries} failed: {err}")
            return fallback_value

        return wrapper

    return decorator


call_attempt = 0


@retry_on_failure(max_retries=3, fallback_value=[])
def fetch_remote_weights() -> list:
    global call_attempt
    call_attempt += 1
    if call_attempt < 3:
        raise ConnectionError("Server reset connection.")
    return [0.12, 0.45, 0.89]


print(fetch_remote_weights())

# ====================================================================================================

# %%
# Task - 07
from functools import wraps
from typing import Any, Callable


def memoize_predictions(func: Callable) -> Callable:
    cache: dict[tuple, Any] = {}

    @wraps(func)
    def wrapper(*args: Any) -> Any:
        key = tuple(tuple(a) if isinstance(a, list) else a for a in args)
        if key in cache:
            print("[CACHE HIT] Returning cached inference result")
            return cache[key]
        result = func(*args)
        cache[key] = result
        print("[COMPUTE] Calculating fresh result")
        return result

    return wrapper


@memoize_predictions
def compute_feature_distance(vector_a: list, vector_b: list) -> float:
    return sum((x - y) ** 2 for x, y in zip(vector_a, vector_b)) ** 0.5


print(compute_feature_distance([1, 2, 3], [4, 5, 6]))  # first call
print(compute_feature_distance([1, 2, 3], [4, 5, 6]))  # second call

# ====================================================================================================

# %%
# Task - 08
import sys
import time
from typing import Generator


def generate_matrix_eager(n: int) -> list:
    vectors = []
    for i in range(n):
        vectors.append([i, i * 0.5, i**2])
    return vectors


def stream_matrix_lazy(n: int) -> Generator:
    for i in range(n):
        yield [i, i * 0.5, i**2]


N = 1_000_000

# Eager: measure build time (the delay before the first element is available)
start = time.perf_counter()
eager_matrix = generate_matrix_eager(N)
eager_delay = time.perf_counter() - start

# Lazy: measure time to get the first element
start = time.perf_counter()
lazy_matrix = stream_matrix_lazy(N)
first_vector = next(lazy_matrix)
lazy_delay = time.perf_counter() - start

print(f"Eager list size:     {sys.getsizeof(eager_matrix):,} bytes")
print(f"Generator size:      {sys.getsizeof(lazy_matrix):,} bytes")
print(f"Eager first-element delay: {eager_delay:.6f} s")
print(f"Lazy first-element delay:  {lazy_delay:.6f} s")

# ====================================================================================================

# %%
# Task - 09
from typing import Any


class SlidingWindowIterator:
    def __init__(self, sequence: list, window_size: int, step: int = 1) -> None:
        self.sequence = sequence
        self.window_size = window_size
        self.step = step
        self.start_idx = 0

    def __iter__(self) -> "SlidingWindowIterator":
        return self

    def __next__(self) -> list:
        if self.start_idx + self.window_size > len(self.sequence):
            raise StopIteration
        window = self.sequence[self.start_idx : self.start_idx + self.window_size]
        self.start_idx += self.step
        return window


timeseries = [10, 20, 30, 40, 50, 60, 70, 80]
for window in SlidingWindowIterator(timeseries, window_size=3, step=2):
    print(window)

# ====================================================================================================

# %%
# Task - 10
from typing import Any, Generator, Iterable


def stream_raw_images(image_records: list) -> Generator:
    for record in image_records:
        yield record


def augment_stream(generator_source: Iterable) -> Generator:
    for record in generator_source:
        if record["pixels"]:  # drop records with an empty pixel list
            yield {**record, "augmented": True}


def normalize_stream(generator_source: Iterable) -> Generator:
    for record in generator_source:
        yield {**record, "pixels": [pixel / 255.0 for pixel in record["pixels"]]}


raw_batch = [
    {"image_id": 1, "pixels": [0, 128, 255]},
    {"image_id": 2, "pixels": []},
    {"image_id": 3, "pixels": [64, 192, 32]},
]

pipeline = normalize_stream(augment_stream(stream_raw_images(raw_batch)))

for record in pipeline:
    print(record)
